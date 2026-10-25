/* Interactive daily lesson; no external scripts or backend. */
(() => {
  'use strict';
  const payload = document.getElementById('lesson-data');
  // Revised v0.7: each form cell is an independent accessible recall control.
  const panel=$('paradigm');
  if(panel && panel.querySelector('[data-recall]')){
    const cells=[...panel.querySelectorAll('[data-recall]')];
    const groups=[...panel.querySelectorAll('[data-table-toggle]')];
    function hide(cell,hidden){
      cell.classList.toggle('is-hidden',hidden);
      cell.setAttribute('aria-pressed',String(hidden));
      const answer=cell.querySelector('.form-answer');
      if(answer)answer.setAttribute('aria-hidden',String(hidden));
      const label=cell.closest('[data-cell-label]')?.dataset.cellLabel||'form';
      if(hidden)cell.setAttribute('aria-label','Reveal '+label);
      else cell.removeAttribute('aria-label');
    }
    function repaint(){
      const all=cells.every(x=>x.classList.contains('is-hidden'));
      const count=cells.filter(x=>x.classList.contains('is-hidden')).length;
      const button=$('toggle-forms');button.textContent=all?'Show all forms':'Hide all forms';
      button.disabled=false;button.setAttribute('aria-pressed',String(all));
      if($('recall-count'))$('recall-count').textContent=count+' / '+cells.length+' forms hidden';
      groups.forEach(b=>{
        const sub=[...document.getElementById(b.dataset.tableToggle).querySelectorAll('[data-recall]')];
        const concealed=sub.every(x=>x.classList.contains('is-hidden'));
        b.textContent=concealed?'Show this table':'Hide this table';
        b.disabled=false;b.setAttribute('aria-pressed',String(concealed));
      });
    }
    cells.forEach(x=>x.addEventListener('click',()=>{hide(x,!x.classList.contains('is-hidden'));repaint()}));
    $('toggle-forms').addEventListener('click',()=>{
      const next=!cells.every(x=>x.classList.contains('is-hidden'));
      cells.forEach(x=>hide(x,next));repaint();
    });
    groups.forEach(b=>b.addEventListener('click',()=>{
      const sub=[...document.getElementById(b.dataset.tableToggle).querySelectorAll('[data-recall]')];
      const next=!sub.every(x=>x.classList.contains('is-hidden'));
      sub.forEach(x=>hide(x,next));repaint();
    }));
    const effects=$('toggle-effects');
    if(effects){effects.disabled=false;effects.addEventListener('click',()=>{
      const hidden=panel.classList.toggle('effects-hidden');
      effects.textContent=hidden?'Show effect clues':'Hide effect clues';
      effects.setAttribute('aria-pressed',String(hidden));
      panel.querySelectorAll('.effect-badge').forEach(b=>{
        b.setAttribute('aria-hidden',String(hidden));
        if(!b.dataset.effectTitle)b.dataset.effectTitle=b.title;
        b.title=hidden?'':b.dataset.effectTitle;
      });
    });}
    repaint();
  }

  if (!payload) return;
  const {id, questions} = JSON.parse(payload.textContent);
  const key = 'sengoidelc:v3:' + id;
  const empty = () => ({solved: [], minutes:'', difficulty:'', note:''});
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
  function feedbackURL(){
    const clean = x => String(x ?? '').replace(/[\r\n|]+/g,' ').trim() || '—';
    const row = '| '+[id,dateJST(),'completed',clean(state.minutes),clean(state.difficulty),clean(state.note)].join(' | ')+' |';
    const body = ['Old Irish learner feedback','', '<!-- Structured row for feedback automation. -->',row,'','I explicitly confirm that I have completed this lesson.'].join('\n');
    return 'https://github.com/stflicker/old_irish_minicourse/issues/new?title='+encodeURIComponent('[Old Irish Feedback] '+id)+'&body='+encodeURIComponent(body);
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
    const ready=correct===questions.length;
    const submit=$('submit-feedback'); if(submit)submit.disabled=!ready;
    show(ready ? 'Quiz ready. Submit the GitHub Issue to record completion; opening the form alone does not count.' : 'Practice is not a completion record. Solve the questions, then explicitly submit via GitHub.');
  }
  document.querySelectorAll('.option').forEach(btn=>btn.addEventListener('click',()=>{
    const i=Number(btn.dataset.question);
    if(state.solved[i])return;
    const isCorrect=Number(btn.dataset.option)===Number(questions[i].correct);
    const fb=$('feedback-'+i);
    if(isCorrect){state.solved[i]=true;persist();paint();}
    else{fb.textContent='Not quite — try again.';fb.classList.add('bad');}
  }));
  if(!$('paradigm').querySelector('[data-recall]')) $('toggle-forms').addEventListener('click',()=>{$('paradigm').classList.toggle('forms-hidden')});
  ['minutes','difficulty','note'].forEach(x => $(x).addEventListener('input',()=>{state[x]=$(x).value;persist();}));
  // Compatibility with previously generated HTML until Pages is rebuilt.
  if(!$('submit-feedback')){
    ['mark-complete','copy-record','download-record','manual-box'].forEach(k=>{const el=$(k);if(el)el.hidden=true;});
    const oldNote=document.querySelector('#record .note');if(oldNote)oldNote.textContent='Completion is recorded only through the submitted GitHub Issue, never by copying back into ChatGPT.';
    const button=document.createElement('button');button.type='button';button.id='submit-feedback';button.className='btn btn-main';button.textContent='Submit completion via GitHub Issue ↗';
    $('reset-practice').parentElement.prepend(button);
  }
  $('submit-feedback').addEventListener('click',()=>{
    if(!state.solved.every(Boolean))return;
    window.open(feedbackURL(),'_blank','noopener,noreferrer');
    show('GitHub form opened. Click “Submit new issue” there to record completion; it is not yet recorded.');
  });
  $('reset-practice').addEventListener('click',()=>{
    if(!confirm('Reset this day\'s answers and local progress record?'))return;
    state=empty();state.solved=Array.from({length:questions.length},()=>false);
    persist();
    questions.forEach((_q,i)=>{$('feedback-'+i).textContent='';});
    paint();
  });
  paint();
})();