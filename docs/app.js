/* Interactive daily lesson; no external scripts or backend. */
(() => {
  'use strict';
  const payload = document.getElementById('lesson-data');
  if (!payload) return;
  const {id, questions} = JSON.parse(payload.textContent);
  const key = 'sengoidelc:v3:' + id;
  const empty = () => ({solved: [], completed: false, minutes:'', difficulty:'', note:'', completionDate:''});
  let state = empty();
  let storageAvailable = true;
  const $ = x => document.getElementById(x);
  try {
    const prior = localStorage.getItem(key);
    if (prior) state = Object.assign(empty(), JSON.parse(prior));
  } catch (_err) {storageAvailable=false;}
  state.solved = Array.from({length:questions.length}, (_,i) => !!state.solved?.[i]);
  const persist = () => {
    if (!storageAvailable) return;
    try {localStorage.setItem(key, JSON.stringify(state));}
    catch (_err) {storageAvailable=false; show('Browser storage unavailable. Export your record.');}
  };
  const show = msg => {$('status').textContent=msg;};
  function dateJST(){
    const parts = new Intl.DateTimeFormat('en-US',{timeZone:'Asia/Tokyo',year:'numeric',month:'2-digit',day:'2-digit'}).formatToParts(new Date());
    const x=Object.fromEntries(parts.map(p=>[p.type,p.value]));
    return x.year+'-'+x.month+'-'+x.day;
  }
  const safe = t => String(t || '—').replace(/[\r\n]+/g,' ').replaceAll('|','\\|').trim() || '—';
  function lineFor(lesson, st){
    return '| '+[lesson,st.completionDate||dateJST(),'completed',safe(st.minutes),safe(st.difficulty),safe(st.note)].join(' | ')+' |';
  }
  function recordText(){
    const rows=[];
    for(let i=1;i<=28;i++){
      const day='OI-D'+String(i).padStart(3,'0');
      try {
        const d=day===id ? state : JSON.parse(localStorage.getItem('sengoidelc:v3:'+day) || 'null');
        if(d && d.completed) rows.push(lineFor(day,d));
      } catch (_err) { /* if corrupt data, skip this day */ }
    }
    return '# Old Irish — learner progress (browser export)\n\n'+
      'This is a copy of completed sessions saved in this browser. It does not automatically update the canonical GitHub PROGRESS.md file.\n\n'+
      '| Lesson | Date (JST) | Status | Minutes | Difficulty / 5 | Note |\n|---|---|---|---:|---:|---|\n'+
      rows.join('\n') + '\n';
  }
  function paint(){
    $('minutes').value=state.minutes;
    $('difficulty').value=state.difficulty;
    $('note').value=state.note;
    const correct=state.solved.filter(Boolean).length;
    $('score').textContent=correct+' / '+questions.length+' correct';
    $('fill').style.width=(100*correct/questions.length)+'%';
    $('scorebar').setAttribute('aria-valuenow',String(correct));
    questions.forEach((q,i)=>{
      const fb=$('feedback-'+i);
      if(state.solved[i]){
        fb.classList.remove('bad');
        fb.textContent=q.explanation || 'Correct.';
      }
      document.querySelectorAll('.option[data-question="'+i+'"]').forEach(btn=>{
        btn.disabled=state.solved[i];
        btn.setAttribute('aria-pressed',String(state.solved[i] && Number(btn.dataset.option)===Number(q.correct)));
      });
    });
    $('mark-complete').disabled=correct!==questions.length;
    $('copy-record').disabled=!state.completed;
    $('download-record').disabled=!state.completed;
    if(state.completed)show('Saved in this browser · '+(state.completionDate||'date unknown')+' JST. Export or report your results in chat.');
    else if(correct===questions.length)show('All correct. Enter a time/difficulty (optional), then mark complete.');
    else show('Answer all questions to unlock completion.');
  }
  document.querySelectorAll('.option').forEach(btn=>btn.addEventListener('click',()=>{
    const i=Number(btn.dataset.question);
    if(state.solved[i])return;
    const isCorrect=Number(btn.dataset.option)===Number(questions[i].correct);
    const fb=$('feedback-'+i);
    if(isCorrect){state.solved[i]=true;persist();paint();}
    else{fb.textContent='Not quite — try again.';fb.classList.add('bad');}
  }));
  $('toggle-forms').addEventListener('click',()=>{
    const hidden=$('paradigm').classList.toggle('forms-hidden');
    $('toggle-forms').textContent=hidden?'Show forms':'Hide forms for recall';
    $('toggle-forms').setAttribute('aria-pressed',String(hidden));
  });
  ['minutes','difficulty','note'].forEach(x => $(x).addEventListener('input',()=>{state[x]=$(x).value;persist();}));
  $('mark-complete').addEventListener('click',()=>{
    if(state.solved.every(Boolean)){
      state.completed=true;
      state.completionDate=state.completionDate || dateJST();
      persist();paint();
    }
  });
  $('copy-record').addEventListener('click',async()=>{
    if(!state.completed)return;
    const row=lineFor(id,state);
    try {
      if(!navigator.clipboard?.writeText)throw new Error('Clipboard unavailable');
      await navigator.clipboard.writeText(row);
      show('Copied the Markdown progress row. Paste it into ChatGPT or your record.');
    } catch (_err) {
      $('manual-box').hidden=false;
      $('manual-text').value=row;
      $('manual-text').focus();$('manual-text').select();
      show('Clipboard blocked. Select and copy the row below.');
    }
  });
  $('download-record').addEventListener('click',()=>{
    if(!state.completed)return;
    const blob=new Blob([recordText()],{type:'text/markdown;charset=utf-8'});
    const link=document.createElement('a');
    link.download='PROGRESS.md';link.href=URL.createObjectURL(blob);
    document.body.appendChild(link);link.click();link.remove();
    setTimeout(()=>URL.revokeObjectURL(link.href),1000);
    show('Exported PROGRESS.md from this browser. Server record is not updated by this download.');
  });
  $('reset-practice').addEventListener('click',()=>{
    if(!confirm('Reset this day\'s answers and local progress record?'))return;
    state=empty();state.solved=Array.from({length:questions.length},()=>false);
    persist();
    questions.forEach((_q,i)=>{$('feedback-'+i).textContent='';});
    $('manual-box').hidden=true;
    paint();
  });
  paint();
})();