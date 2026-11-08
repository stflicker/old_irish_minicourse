# 需要你亲自完成的配置（附步骤）

*给项目所有者看的清单。会话自己能做的配置不在这里，见 `CONTENT_DESIGN_HANDOFF.md` 的 §5b。*
*我没法在应用里点按钮，所以下面凡是涉及 Claude 应用界面的步骤，菜单名称是按一般规律写的，**以你屏幕上的实际名称为准**；涉及 GitHub 网页的步骤写的是我所知道的菜单路径。*

## 总览

| # | 事项 | 必须？ | 谁能做 | 状态 |
|---|---|---|---|---|
| 1 | 把 Stifter 的分课节选放进 Google Drive | 必须 | 只有你 | 文件已准备好（见下） |
| 2 | 把项目说明贴进 Claude Project | 必须 | 只有你 | 文本已准备好：`PROJECT_INSTRUCTIONS.md` |
| 3 | 新会话选对环境 | 必须 | 只有你 | 环境已建好 |
| 4 | 确认 Google Drive 连接器在新会话里可用 | 必须 | 只有你 | 已连接，新会话要自己看一眼 |
| 5 | GitHub Pages：决定分支能否部署，并合并到 `main` | 必须（想在线看到新页面就必须） | 只有仓库所有者 | 见第 5 节 |
| 6 | 把拿不到的文献存进 Drive（Stifter 2023 论文、Matasović 条目） | 可选 | 只有你 | 见第 6 节 |
| 7 | 保护 `main`、合并规则 | 可选 | 只有仓库所有者 | 见第 7 节 |

会话自己能完成的（环境设置脚本、申请新主机、给会话打标签、分支约定、安装依赖）已经写进交接文件，不需要你手动配置。

## 1. 把 Stifter 节选放进 Drive

**为什么：** Drive 连接器读不完整本书（只读前约 18 万字符，下载上限 10 MB）。拆成 10 份、每份几页到十几页后，每份都能完整读出（我核对过：每份文字量在 1.6–5.3 万字符，远低于上限）。

**文件：** 我生成了 10 份节选，文字层保留，每份 0.3–0.7 MB，打成了 `Stifter_excerpts.zip`（约 4.9 MB），随这条消息发给你。内容：

| 文件 | 内容 |
|---|---|
| `Stifter_S01_L04_mutations.pdf` | 第 4 课：初始变化（L/N/H 的定义） |
| `Stifter_S02_L06-07_o-stems_article.pdf` | 第 6–7 课：o-词干、升降、音节脱落、冠词 |
| `Stifter_S03_L08-09_verb_W1.pdf` | 第 8–9 课：动词、W1 |
| `Stifter_S04_L10-11_a-stems_article.pdf` | 第 10–11 课：a-词干、*ben*、阴性冠词 |
| `Stifter_S05_L12-14_W2_poss_io.pdf` | 第 12–14 课：W2、词尾史、所有格、诗、io-词干 |
| `Stifter_S06_L15-17_compound_ia_i.pdf` | 第 15–17 课：复合动词、ia-词干、i-词干 |
| `Stifter_S07_L18-20_preps_S1_i.pdf` | 第 18–20 课：带人称的介词、S1、i-词干 |
| `Stifter_S08_L21-22_S2_S3_texts.pdf` | 第 21–22 课：S2/S3、词尾史、三联句、测验 |
| `Stifter_S09_L23-24_u_numbers_copula.pdf` | 第 23–24 课：u-词干、数词、系词 |
| `Stifter_S10_AppendixF_tables.pdf` | 附录 F 表格（冠词总表、动词类） |

**步骤：**
1. 解压 zip。
2. 在 Google Drive 新建一个文件夹，例如 `Old Irish – Stifter (private)`。
3. 把 10 个 PDF 拖进去。**保持 PDF 格式，不要转成 Google 文档。**
4. **不要**设置“知道链接的人可查看”。这是有版权的书，只放在你私人的 Drive 里。
5. 文件名必须保持以 `Stifter_S` 开头，会话是用这个名字搜索的。

**验证：** 开一个新会话，说“用 Drive 连接器搜索 `Stifter_S02`，读出第 6.4 节开头的两句话”。能读到就对了。

**如果想自己生成：** 在你电脑上装 Python，然后

```
python -m pip install pypdf
python scripts/split_stifter_pdf.py /你的路径/Sengoidelc.pdf 输出文件夹
```
脚本在仓库里：`scripts/split_stifter_pdf.py`。页码偏移默认是 12（印刷页 + 12 = PDF 页），只适用于你给我的那份 402 页 PDF；别的版本用 `--offset` 调整。仓库的 `.gitignore` 已经排除了 `*.pdf`，不会误提交。

## 2. 把项目说明贴进 Claude Project

1. 打开 `PROJECT_INSTRUCTIONS.md`，复制两条横线之间的全部文字。
2. 在 Claude 应用里打开 Old Irish Mini-Course 项目，找到项目的“说明 / Instructions / Custom instructions”（具体名称以界面为准），粘贴并保存。
3. 效果：项目下新建的每个会话开头都会被要求先读 `CONTENT_DESIGN_HANDOFF.md`、检查环境、确认角色。

## 3. 新会话选对环境

环境 `old_irish_minicourse`（ID `env_013XVGzxJKc29J9Gc3qi5V3o`）已经建好，是你的个人环境。

1. 在项目下新建会话时，在选择环境的地方选 `old_irish_minicourse`。
2. 如果列表里没有：回到这个会话，让我运行 `list_environments` 确认它还在；仍不在就告诉我，我重新申请。
3. 验证：新会话里说“运行 `get_environment`”，应显示名称 `old_irish_minicourse` 和 8 个额外主机。
4. 用 `Default` 环境的会话读不到 EIEOL 等文献站点。

## 4. 确认 Google Drive 连接器在新会话里可用

1. claude.ai → 设置 → 连接器，确认 Google Drive 是“已连接”。目前它是已连接的。
2. 新会话里说“列出可用连接器”，看 Google Drive 是否“在当前会话启用”。没有的话，按界面提示在该会话里打开它。

## 5. GitHub Pages：让新页面真正上线

**事实：** 我推到分支 `claude/focused-newton-92w684` 的 4 次提交（run #97–#100）触发的工作流都在 1 秒内失败，一步都没执行。这很像 `github-pages` 环境的“部署分支”规则只允许 `main`。**这是我的推测，请你确认：**

1. 打开 https://github.com/stflicker/old_irish_minicourse/actions/runs/42400183296 ，点进失败的 job，看红色错误提示。如果写的是类似“Branch … is not allowed to deploy to github-pages due to environment protection rules”，推测成立。
2. 打开仓库 **Settings → Environments → github-pages → Deployment branches and tags**，看当前规则。

**两种做法，建议 A：**
- **A（推荐）：保持只允许 `main`，通过 PR 合并来发布。** 好处是只有你审核过的内容会上线。步骤：
  1. 仓库页面 → **Pull requests → New pull request**；
  2. base 选 `main`，compare 选 `claude/focused-newton-92w684`；
  3. 看一眼改动，点 **Create pull request → Merge pull request**；
  4. 到 **Actions** 看 “Old Irish daily publication” 是否成功（约一两分钟）；
  5. 打开 `https://stflicker.github.io/old_irish_minicourse/` 和 `…/days/001.html`（地址是按 GitHub Pages 惯例拼的，我没有验证）。
  - 也可以让我来开这个 PR，你说一声就行。
- **B：允许分支部署。** 在上面的 Deployment branches 规则里加 `claude/*`。代价：任何会话推送一次就会把未审核内容发布到公开站点，并且会互相覆盖。不推荐。

**另外：** 我已经把工作流里“检查线上 Day 005 页面是否含有旧句子”的一步换成了通用检查（检查线上 Day 001 页面和刚构建的版本一致）。原来那一步在 Day 5 重写后合并到 `main` 时一定会失败。这个修改在分支里，随 PR 一起合并。

首次使用 Pages 还需要确认 **Settings → Pages → Build and deployment → Source** 是 **GitHub Actions**（原先的说明就是这么要求的，大概率已设好）。

## 6.（可选）把拿不到的文献存进 Drive

有两处文献这个会话读不到（网站有人机验证或被权限分类器拒绝）：

- **Stifter 2023，《The rise of gemination in Celtic》**（Open Research Europe，开放获取）：用你自己的浏览器打开 https://pmc.ncbi.nlm.nih.gov/articles/PMC10446051/ ，把页面“下载 PDF”，存进同一个 Drive 文件夹，文件名 `Stifter2023_rise_of_gemination.pdf`。这样会话能核对“Day 2 的 [H] 证据”那段。
- **Matasović（2009）《Etymological Dictionary of Proto-Celtic》**：这是有版权的书，只在你有合法副本时才放。只把需要的条目（*\*ekʷo-*、*\*kʷenno-*、*\*u̯iro-* 等）截图或截取几页存成 PDF，放进同一个 Drive 文件夹，文件名以 `Matasovic_` 开头。

不放也行，课程里这些点会继续标成“未直接核对”。

## 7.（可选）保护 `main`

仓库 **Settings → Branches → Add branch ruleset**（或 “Add rule”），对 `main` 要求通过 PR 合并，禁止直接推送。这样多个会话并行工作时，不会有谁无意中直接改了 `main`。注意：工作流里自动提交 `docs/` 和 `PROGRESS.md` 的那一步需要权限推送到 `main`，设置规则时要允许 GitHub Actions 机器人绕过，否则每日发布的那一步会失败。如果拿不准，先不设。

## 附：没有出现在这份清单里的东西

- **GitHub 授权、密钥、令牌**：不需要，已经能读写仓库。
- **环境设置脚本（装依赖）、增加主机**：会话可以自己提出，你只需在弹出的审批里点同意，见交接文件 §5b。
