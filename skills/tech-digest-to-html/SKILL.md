---
name: tech-digest-to-html
description: 针对前沿论文/技术长文/深度复盘的端到端消化、数学建模与单文件交互式 HTML 白皮书交付。触发场景：(1) 深度消化前沿论文或工程实战长文，(2) 将定性技术架构推导为可计算模型（排队论/USL/盈亏平衡），(3) 生成零外部依赖、自包含的高保真单文件 HTML 总结或白皮书，(4) 包含原生 CSS 数学排版与动态交互沙盘，(5) 运行自动化静态自检验证 HTML 结构、坐标一致性与唯一存储目录规范。唯一存储路径：/Users/yangkejin/Documents/Openai/AIKnowledge/，命名规范：YYYYMMDD_核心要义一眼就知道主题是啥.html。
agent_created: true
---

# Tech Digest to HTML: 前沿技术消化与单文件交互白皮书交付规范

## 1. 核心定位与解决痛点

本 Skill 提炼自前沿学术论文（如 JIT-Agent: arXiv:2608.25593）与工业界高强度工程实战（如 2000 小时 Agentic Engineering 工作台复盘）的完整推演交付经验。它致力于彻底解决 AI 在技术消化与专著输出中的 **五大核心通病**：

1. **资产杂乱散落与命名失序（Storage Chaos & Transience Traps）**：产出物随意散落在临时会话目录，文件名充斥“最终版”、“最新版”、“合并版”、“总结归纳”等模糊修饰词，导致后期难以检索与溯源。
2. **假核验（Hallucinatory Verification）**：直接复述二次加工稿件中的失真数字或遗失图表（如 `[image here]`），未追溯作者真实口径与学术对照组消融数据。
3. **隐喻泛滥（Metaphor-Only Architecture）**：用“操作系统”、“沙箱”、“自愈循环”等模糊定性叙事掩盖量化空洞，缺乏精确的可计算数学模型支撑决策。
4. **沙盘造假（Interactive Fabrication）**：交互控件为了演示效果输出编造的准确率（如“提高 91.2%”）、降低时延等无出处假数据，赋予控件虚假权威感。
5. **脆弱交付（Fragile Delivery）**：依赖外部 Google Fonts / KaTeX CDN 导致离线白屏、LaTeX 公式未渲染裸露 `$$` 源码、手写 SVG 曲线点阵与刻度脱节漂移。

---

## 2. 全局硬约束：唯一存储位置与文档命名规范

为根除知识资产杂乱无章的现状，所有由本 Skill 产出、消化或衍生的最终成果物，必须严格遵循以下**存储与命名铁律**：

### 2.1 唯一合法存储路径 (Canonical Storage Location)
- **唯一落地目录**：
  ```
  /Users/yangkejin/Documents/Openai/AIKnowledge/
  ```
- **执行原则**：
  - 本地会话的 `outputs/` 或临时目录仅作为生成构建过程中的暂存区。
  - **交付给用户的最终成果物，必须统一且唯一落盘至 `/Users/yangkejin/Documents/Openai/AIKnowledge/`**。
  - 严禁交付物散落在项目根目录、下载文件夹或未受治理的临时路径。

### 2.2 统一文档命名规范 (First-Glance Naming Standard)
- **标准格式模板**：
  ```
  [YYYYMMDD]_[核心要义一眼看出主题].[html|md]
  ```
- **四大命名守则**：
  1. **统一日期前缀（Standardized Date Stamp Prefix）**：
     - 必须以 8 位公历年月日开头并紧随下划线（`YYYYMMDD_`，如 `20260902_`），表示文档定稿或版本基准日。
     - **天然支持时序检索**：使得所有资产在文件系统、IDE 资源管理器及终端列表内按自然字典序呈现严格的时间线演进，便于快速定位与版本归档。
  2. **核心要义后置（First-Glance Semantic Clarity）**：
     - 文件名后半部分在 8~25 个字以内，高度凝练地概括**技术实体、核心架构/方法论、应用体裁**（如“白皮书”、“实施指南”、“量化模型”）。
     - 读者只需扫视文件名，即可秒懂该文档的基准发布日、实质内容与技术层级，杜绝任何空泛词（如单用 `20260902_Agent.html`、`20260903_量化.html`）。
  3. **反模式与黑名单词库（严厉禁止）**：
     - ❌ **绝对禁止任何临时性修饰词**：严禁出现 `最终`、`合并版`、`最新`、`总结归纳`、`修改版`、`完整版`、`草稿`、`副本`、`temp`、`draft`、`final`、`latest`、`new`。
     - ❌ **绝对禁止营销号/自媒体长标题**：长句、悬念句、感叹句必须重构为严谨的技术专著主题。
     - ❌ **绝对禁止无日期或日期后置文件**：缺少 8 位日期前缀的文件一律判定为不合格交付物。
  4. **演进重命名原则**：
     - 若同一主题在不同日期产生重大架构重构或成果合并，直接通过更新日期前缀（或在核心要义中体现演进特征）区分，严禁通过追加“-最终”、“-合并”来区分版本。

### 2.3 规范对照示例表

| 状态 | 违规/旧文件名（反模式） | 规范化命名（日期_一眼知主题） | 改进理由 |
| :--- | :--- | :--- | :--- |
| ❌ 违规 | `Agent工程体系-最终合并版.html` | `20260902_JIT-Agent与Fleet双螺旋架构工程白皮书.html` | 剔除“最终合并版”临时词，点明 JIT-Agent 与 Fleet 双螺旋核心要义，日期前置保障时序检索 |
| ❌ 违规 | `Harness与Fleet Agent工程体系综合.html` | `20260902_JIT-Harness动态演进与Fleet并发调度综合架构.html` | 去除空格，提炼 JIT 动态演进与并发调度要义，日期前置 |
| ❌ 违规 | `AI 原生 SDLC（软件开发生命周期）实施指南.html` | `20260903_AI原生SDLC工程化落地与实践指南.html` | 规范括号与空格，凝练工程化主题，日期前置 |
| ❌ 违规 | `写了2000小时AI代码后-他把效率问题改写成了调度问题.html` | `20260903_2000小时Agentic工程实战与并发调度治理.html` | 将营销标题转为高辨识度的技术专著主题，日期前置 |
| ❌ 违规 | `每天用AI的人更需要学会二阶思考.html` | `20260903_AI辅助研发的二阶思考与心智模型.html` | 消除口语化表达，提炼研发心智模型要义，日期前置 |
| ❌ 违规 | `Claude-Fable-5.1提示指南-Agent运行时迁移清单.html` | `20260903_Claude-Fable-5.1提示架构与运行时迁移指南.html` | 规范用词，消除清单口吻，采用统一日期前缀 |

### 2.4 自包含单文件原则 (Self-Contained Single-File Rule)
- **单一交付物约束**：每次任务必须且仅交付一个完全自包含的 `.html` 文件，所有内容、数据、图表、交互逻辑均集成在内部。
- **严禁页面跳转依赖**：严禁产生跨页面相对跳转或外部页面依赖。
- **严禁生成附属解释文档**：严禁伴生生成多余的 `.md` 说明文档、README、临时提取脚本或镜像副本文件，成果物保持绝对单一与干净。
- **零外部网络依赖**：断网离线 100% 完整可用，禁止外链 CDN 脚本、外部 CSS、外部图片文件夹（全部内联或矢量化）或远程字体。

---

## 3. 五阶段标准化作业流 (The 5-Stage Pipeline)

```
[Stage 1: 事实核验与逆向校准]
          │ 区分一手源/分析稿、消融数据对齐、安全边界勘误
          ▼
[Stage 2: 理论压力测试与可计算建模]
          │ 识别演化信号断层、USL 拐点推导 (N*)、CONWIP 准入控制模型
          ▼
[Stage 3: 纯内联零依赖架构设计]
          │ 纯系统字体栈降级、KaTeX-Free CSS 原生数学引擎、双主题五色语义
          ▼
[Stage 4: 动态交互沙盘构建 (防造假)]
          │ 任务装配切换、排队论雪崩滑块、USL 动态曲线、期权反解决策器
          ▼
[Stage 5: 自动化全栈静态自检与唯一归档]
          │ 运行 validate_html.py 阻断 8 项工程缺陷（含存储路径与命名规则）
```

### Stage 1: 事实核验与逆向校准 (Fact Verification & Source Grounding)
1. **区分一手源与第三方稿件**：
   - 检查输入材料是论文预印本、作者直接陈述，还是第三方二次分析稿。
   - 若为第三方转述，主动在报告中区隔“作者实测口径”与“分析者推测”，对断言进行降级标注。
2. **硬指标与消融基准核实**：
   - 使用 WebFetch/WebSearch 查证源论文，锁定硬数据（如 Qwen3.6-27B 底座、18/18 配对提升、GLM-5.2 74.1→81.8、成本降 36.0%）。
   - **禁止推测遗漏数据**：若原图表缺失（如出现 `[image here]`），明确标注“数字不可考”，严禁脑补填数。
3. **关键边界勘误**：
   - 查证底层依赖的安全事实（例如：Pi 官方明确声明“非沙箱”，不能与隔离容器等同；严查凭据泄露等真实事故）。

### Stage 2: 理论压力测试与可计算建模 (Mathematical Formalization)
必须将定性架构命题抽象为**可计算的数学约束**，拒绝空洞概念：

1. **演化信号断层（Ground Truth Gap）**：
   - 明确标注短程基准与长程工程的断裂点：论文基准有即时自动判分（Ground Truth），而实际工程长达数天且无真值，反馈回路在人类审查处断裂。
2. **通用可扩展性定律（USL 建模）**：
   - 形式化吞吐能力：
     $$C(N) = \frac{N}{1 + \sigma(N-1) + \kappa N(N-1)}$$
   - 反解峰值拐点：
     $$N^* = \sqrt{\frac{1-\sigma}{\kappa}}$$
   - 明确 $\sigma$（人类评审锁 + 本机资源争抢）与 $\kappa$（跨 Agent 语义写偏序与冲突）。
   - **有效参数膨胀现象**：由于返工率随并发激增，测得的“有效 $\sigma/\kappa$”通常比静态值高出 2 倍以上，实际可用并发将大幅萎缩（如 13.6 降至 7.8）。
3. **动态排队论与准入控制（CONWIP）**：
   - 否定无量纲的“权重相乘”式调度；定义服务率衰减模型（上下文切换压力 $\gamma$）：
     $$\mu_{\text{eff}} = \frac{60}{T \cdot (1 + \gamma(N-1))}$$
   - 指出调度器的首要职责是**准入控制（限流）**而非事后重排。
4. **JIT 盈亏平衡点与期权定价**：
   - 建立 AOT 固定流水线与 JIT 动态装配的摊销成本曲线，求解平衡点 $n^*$（精确值为 11 次）。
   - 基于实物期权模型反解预发送（投机执行）的临界命中率 $p^*$ 与最大允许预排条数 $N_{\text{msg}}$。

### Stage 3: 纯内联零依赖架构设计 (Zero-Dependency Frontend)
交付文件必须做到**双击即开、断网可用、全自包含**：

1. **零外部依赖数学排版引擎 (MathML Core + 纯 CSS 优雅降级)**：
   - 严禁引入外部 KaTeX/MathJax CDN，严禁在 HTML 裸露未渲染的 `$$`。
   - **首选 HTML5 原生 MathML Core**（全现代浏览器内置支持）：对嵌套分式、加减符号与根式具有完美的矢量中轴对齐与自适应字号降级。
   - 纯 CSS 降级（简单单层分式）：遵循 `references/css_math_typography.md` 规范（`.mfrac`, `.msqrt`, 原生 `<sub>/<sup>`），利用 `currentColor` 自动自适应深浅色。
2. **纯系统字体降级栈**：
   - 无需请求 Google Fonts，保障绝对安全与隐私：
     - 正文栈：`-apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;`
     - 标题栈：`"Songti SC", "SimSun", "Newsreader", Georgia, serif;`
     - 代码栈：`ui-monospace, "SF Mono", Menlo, Consolas, "JetBrains Mono", monospace;`
3. **双主题与五色语义系统**：
   - 浅色底：暖羊皮纸 `#FAF7F2`；深色底：黑曜石 `#181715`。
   - 五色状态令牌：`--accent` (陶土 `#D97757`), `--emerald` (成功/通过), `--rose` (警戒/断层), `--amber` (告警/瓶颈), `--cyan` (推导/数据)。

### Stage 4: 动态交互沙盘构建原则 (Sandbox & Interactive Rules)
1. **四大经典交互模块**：
   - **模块 1：任务类型装配沙盘**（Tab 切换动态显示 Memory/Planning/Action/Fleet 协议与参数流）。
   - **模块 2：排队论雪崩滑块**（双向绑定评审耗时 $T$、并发数 $N$、切换惩罚 $\gamma$，实时对比朴素 $\rho$ 与实际 $\rho$，反解极限并发 $N_{\text{max}}$）。
   - **模块 3：USL 动态并发曲线**（滑块调整 $\sigma$ 与 $\kappa$，实时重绘 SVG 折线并更新峰值 $N^*$ 与倒挂区域）。
   - **模块 4：预发送期权决策器**（调整回滚成本与等待时长，反解临界胜率 $p^*$ 与可预排数）。
2. **防造假铁律（Anti-Hallucination Guardrail）**：
   - **严禁虚构数值**：绝对禁止为了页面生动而随意编造“Token 浪费压减 74%”、“准确率 91.2%”等无源数据。
   - **控件公式强绑定**：所有回显数值必须严格由 Stage 2 推导出的数学公式实时运算得出。
   - **参数假设透明化**：若为演示设置基准参数（如人类评审耗时 35 分钟），必须显式在界面中注明“此为基线假设值”。

### Stage 5: 自动化全栈静态自检与唯一归档 (Automated Verification & Archival)
**Stage 4.5 · 数值常量单一真值源（Numeric Single Source of Truth）**：
所有写入正文段落的数值常量（如“当 W = 4·T½ 时 w̄ 降至 0.3381”这类推导结论），必须先由 Python 脚本实算，再从脚本 stdout 复制粘贴进 HTML。严禁心算、估算或凭记忆回填——自检第 6 项只校验静态 SVG 点阵坐标，对散文中的算术错误**完全无感知**。交付前用脚本回归复核全文所有常量。

**常量脚本禁止跨模型复用单字母变量名**（2026-09-04 实例）：一个脚本内串算 M1–M6 六个模型时，后段 `for m in (3, 6, 10, 15)`（会议人数）污染了前段 M1 的模型智能变量 `m`，使最终汇总表导出错误的「最弱项 ÷ 模型智能 = 21.43x」（正确值为 **1.214x**）。同一脚本内的分节打印正确、只有末尾汇总表出错，极难察觉。防御：常量脚本内所有模型级变量一律带模型前缀（`M1_m`、`M6_m`），或在每个模型段用独立函数封装，禁止模块级单字母标量。

在交付用户前，**必须**调用配套脚本执行 8 项阻断式检查，且目标文件必须位于唯一存储库：

```bash
python3 ~/.workbuddy/skills/tech-digest-to-html/scripts/validate_html.py /Users/yangkejin/Documents/Openai/AIKnowledge/<YYYYMMDD>_<核心要义>.html
```

**8 项静态自检清单**：
- [ ] **1. 存储位置与命名合规**：目标路径必须为 `/Users/yangkejin/Documents/Openai/AIKnowledge/`，命名符合 `[YYYYMMDD]_[核心要义].html`，无任何临时反模式词汇。
- [ ] **2. 零外部依赖**：外链 CSS、外链 JS、CDN、远程字体、`@import`、远程 `url()` 数量必须为 0。
- [ ] **3. 标签平衡栈**：DOM 树完全闭合；SVG 特殊标签（`path`, `circle`, `rect`, `line`, `polyline`）正确自闭合。
- [ ] **4. 锚点与目录可达性**：侧边目录所有 `#id` 在正文中 100% 存在对应的物理标签 ID。
- [ ] **5. 原生 JS 语法**：内联 `<script>` 经由 `node --check` 抽象语法树解析通过，无语法错误。
- [ ] **6. SVG 几何与坐标映射**：折线点阵坐标落在 viewBox 内；严查点阵 $x$ 轴间距与坐标轴刻度文本间距是否完全一致（防止 $N=30$ 画在 $N=26.5$ 刻度的视觉欺骗）。
- [ ] **7. 交互控件完整接线**：页面内所有 `<input type="range">`、`<button>`、`<select>` 及显示槽位在 JS 中均有事件监听与回写逻辑，无悬空组件。
- [ ] **8. 排版规范与防泄漏**：无未渲染 LaTeX 宏代码（`\frac`, `\sqrt`）；货币符号（如 `$0.075`）不被误判；包含响应式与 `@media print` 打印适配。

### Stage 5.5: 运行时冒烟测试与结论稳健性复检 (Runtime Smoke Test & Robustness Re-test)

8 项静态自检只做**语法层**校验（`node --check` 仅验证 AST，不执行代码），无法发现运行期空引用、NaN 回显与死控件。交付前必须补两步：

**① 最小 DOM 垫片运行时冒烟测试**
写一个 ~40 行的 Node 垫片（`getElementById` 返回 mock 元素、`createElementNS` 返回 mock 节点、`addEventListener` 记录到 `_h[type]` 并提供 `fire(type)`、`querySelectorAll` 返回桩数组），然后 `eval()` 抽取出的内联脚本，逐项断言回显值：

```bash
python3 -c "import re; s=open(F,encoding='utf-8').read(); open('/tmp/inline.js','w').write(re.findall(r'<script>(.*?)</script>',s,re.S)[0])"
node -e "require('/tmp/shim.js'); eval(require('fs').readFileSync('/tmp/inline.js','utf8')); /* 断言各 stat-* / out-* 槽位 */"
```
要点：垫片里的 `data-*` 属性映射**必须从生成好的 HTML 里正则抽取**，不要手工录入——手工录入一旦错位，会把页面本身的正确逻辑误判为错误。测试完删除 `/tmp` 下的垫片与抽取脚本，保持交付物唯一。

**垫片必须提供的 DOM 表面（缺失即误报为页面 bug）**：`el.style = {}`（阅读进度条写 `style.width`）、`el.setAttribute/getAttribute`、`el.classList.toggle(cls, force)` 双参形式、`el.parentElement.classList`（清单类组件会改父级 `<li>` 样式）、按 id 全局注册的单元素表（同一 id 多次 `getElementById` 必须返回同一对象）、`document.createElement/createElementNS`、`document.execCommand`（剪贴板降级分支）、以及**预置 `documentElement.attrs['data-theme']` 为 HTML 中的初始值**（主题切换断言依赖起始态）。`window` 侧给 `addEventListener/print/scrollTo`，`IntersectionObserver` 置 undefined 以走跳过分支。

**同一 IIFE 内禁止重复 `var` 名**（2026-09-04 实例）：监控沙盘的 `statWeek`（每周检查次数）与清单沙盘的 `statWeek`（完成步数）重名，`var` 提升到同一函数作用域后被后者劫持，页面表现为“每周检查次数”槽位显示 `0 / 5`。静态自检第 5 项（`node --check`）与第 7 项（接线）**均无法发现**，只有运行时冒烟能暴露。命名规范：所有显示槽位按所属沙盘加前缀（如 `statMon-*`、`statWeek-*`）。

**② 数值模型双路交叉校验**
Python 侧（生成器内）与前端 JS 侧用**同一份数据集**独立实现同一个公式，比较到小数点后 4 位。两者不一致即说明某一侧的映射或聚合写错了。

**③ 结论稳健性复检（最容易被跳过、也最容易打脸的一步）**
在正文里写下任何「A 导致 B」的定性结论后，**必须先跑一次分组 / 阈值敏感性检验，再定稿**。
- 实例（2026-09-03 Grok Bot 模板篇）：凭直觉写下「风险→约束条数 的相关性由 Copay Compass 单个离群点撑起」。实测把 R<sub>min</sub> 提到 1、剔除 10 份零风险样本后，Pearson r 从 0.7865 **升到** 0.8437、斜率从 1.7697 **升到** 2.3651——假设被自己的数据证伪。
- 正确写法：把被推翻的假设连同实测数字一起写进正文（「该检验推翻了……的直觉假设」），并给出真正成立的形状（该例中是**凸性加速**：R=0→0.30 条、R=1→0.69、R=2→3.50、R=5→10.00，跃迁点在 R≈2）。
- 同时标注自由度警告（该例 R≥2 仅 3 个样本，不可外推）。
- 实例（2026-09-04 持久 AI 同事篇）：假设「文档 70% 征询点是反馈价值与返工成本的**无约束最优**」。构造目标函数后做 β ∈ [2, 5000] 全域扫描，d\* 上确界恒为 **0.6569 < 0.70**（β→∞ 时 `d^β → 0`，目标收敛到 `d/(d+d₀) − r₀d^γ`，其解析上确界 0.657）——**假设被自己的数据证伪**。正确解释是 70% 为**约束绑定解** `d* = max(d_think, d*_unc)`，其约束即同一受访者的另一句规则「思考型写作由自己开始，也由自己结束」。教训：当经验数字怎么调参都够不着时，**优先怀疑自己漏了一项约束，而不是去调参数凑数字**（凑参数就是沙盘造假）。

**④ 静态初值必须与 JS 默认重算值逐槽位一致**
HTML 里手写的所有回显槽位初始文本（`<div id="out-x">???</div>`）、SVG 静态 `points`、verdict 静态文案，本质都是「默认滑块位置下 JS 会算出的值」的**预演**。手写初值与 JS 重算值不一致时，8 项静态自检**全绿也发现不了**，页面一加载却在默认值附近闪跳成另一个数。
- 2026-09-04 实例：三处不一致——`out-m2-kmaxno` 写「3 步」而 JS 算 `3.46 步`；`out-m2-kmaxrec` 写「187 步」而 JS 算 `186.6 步`；`out-m5-sup` 写「0.000」而 JS 算 `0.657`。全部由运行时冒烟发现。
- 防御：冒烟测试第一阶段**先只断言初始态**（不触发任何事件），逐槽位比对手写初值与 JS 输出；第二阶段再 `fire('input')` 验交互。

**⑤ 双路交叉校验的期望值禁止手工转录**
期望值若由人从 Python stdout 抄进 Node 断言，抄错一次就会把页面的正确逻辑判为错误（或反向漏过）。正确做法：Python 侧在**同一脚本内**独立实现同一组公式，直接 `json.dump` 成 `/tmp/expect.json`；Node 侧读入该文件做比对。这样才是真双路，而不是「一次实算 + 一次手抄」。

---

## 4. 典型工程陷阱与防御边界

| 序号 | 陷阱分类 | 典型错误表现 | 防御方案与正确实践 |
| :--- | :--- | :--- | :--- |
| **1** | **存储散落失控** | 生成的文件随意保存在 `./outputs/` 或临时目录，未汇总归档 | 强制唯一存储至 `/Users/yangkejin/Documents/Openai/AIKnowledge/`，自检脚本强制拦截非标路径。 |
| **2** | **命名临时泛化** | 使用“最终版”、“合并版”、“总结归纳”等模糊词汇 | 采用“YYYYMMDD_核心要义一眼看出主题”规范，阻断黑名单词汇，保障资产可检索性与时序排布。 |
| **3** | **排队论优先级** | 使用 `Impact × Risk × ...` 连乘公式对任务排序 | 维度未归一化且极易产生“一票归零”；改用 WSJF（延误成本/工时），且调度器首要职能是 CONWIP 准入控制。 |
| **4** | **可扩展性盲区** | 认为 Agent 越多越好（线性扩展思维） | 引入 USL，指出当跨 Agent 存在语义写偏序（$\kappa > 0$）时，超过峰值 $N^*$ 后总产出单调倒挂（30 个还不如 14 个）。 |
| **5** | **有效参数膨胀** | 直接使用单机理想测得的 $\sigma$ 与 $\kappa$ | 并发升高会导致任务返工率上升，实测“有效损耗参数”放大 2 倍以上，真实可用并发萎缩近半。 |
| **6** | **SVG 刻度错位** | 手写 SVG 时，曲线点间距与刻度文本间距不一致 | 必须用反查脚本复核映射公式：$x = x_0 + \frac{i}{M} \times W$，严禁用肉眼估算。 |
| **7** | **公式 CDN 劫持** | 习惯性引入 `<script src="cdn/katex...">` | 断网或离线无法渲染；采用本 Skill 配套的 MathML Core / 纯 CSS 原生数学系统彻底解决。 |
| **8** | **沙盘虚假数字** | 为了动效丰富，给滑块输出编造的百分比 | 严禁捏造数据！无确定事实时，提供“物理公式实时反解”而非静态虚构结论。 |
| **9** | **静态自检的虚假安全感** | 八项自检全绿就宣布交付，未跑运行时冒烟测试 | 补充 Stage 5.5：最小 DOM 垫片 + Node 运行时冒烟，覆盖每个沙盘的全分支。 |
| **10** | **结论先于稳健性检验** | 拿到一个相关系数或提升幅度就写进结论 | 结论定稿前必须跑敏感性检验（剔除离群点、换子集、变换模型形状）再定调。 |
| **11** | **正文中手算常量失真** | 把推导出的数值凭心算写进散文段落（如把 0.338 写成 0.271），自检脚本完全查不出来 | **单一真值源铁律**：自检第 6 项只校验静态 SVG 点阵坐标，**不校验散文中的算术常量**。凡写入正文的数字常量，必须先由 Python 脚本实算、再从脚本输出粘贴，严禁心算或凭记忆回填。定稿前用脚本回归复核全文所有常量。 |
| **9** | **静态自检的虚假安全感** | 8 项自检全绿就宣告完成，但 `node --check` 只校验 AST 不执行代码，运行期空引用与 NaN 回显照样漏网 | 补 Stage 5.5 的最小 DOM 垫片运行时冒烟测试，逐槽位断言回显值；数值模型做 Python / JS 双路交叉校验到 4 位小数。 |
| **10** | **结论先于稳健性检验** | 凭直觉写下「A 导致 B」并美化措辞，从未跑分组或阈值敏感性检验 | 定稿前必须跑一次敏感性检验。若假设被数据推翻，把被推翻的假设与实测数字一并写进正文（如「该检验推翻了……的直觉假设」），而不是悄悄删掉结论。 |

---

## 5. 输入、输出与验收标准

### 5.1 输入要求
- **核心材料**：待消化的论文 PDF/链接/文本，或工程复盘文档。
- **目标受众**：架构师/研发负责人/研究员（要求深度、数学硬核、逻辑严密）。
- **风格偏好**：经典出版级排版（如 Claude 暖羊皮纸风格、学术白皮书）。

### 5.2 交付物落地规范
- **最终物理文件**：必须保存至 `/Users/yangkejin/Documents/Openai/AIKnowledge/<YYYYMMDD>_<核心要义>.html`。
- **结构绝对自包含**：完整单文件 HTML，内嵌纯 CSS 样式与原生 JS 逻辑，零外部网络请求。
- **严禁伴生文件与外部依赖**：严禁生成额外的附属解释文档（如伴生 `.md`、临时脚本），严禁生成别名软链接（symlink），内部锚点严格自闭合、严禁外部页面跳转依赖。

### 5.3 验收黄金标准
1. **归档与命名合规**：落盘于 `/Users/yangkejin/Documents/Openai/AIKnowledge/`，命名符合 `YYYYMMDD_核心要义`，无任何违禁词。
2. **零外部网络请求**：在完全断网环境下双击打开，排版、字体、公式、SVG 图表、交互沙盘 100% 完整可用。
3. **静态校验零错误**：执行 `python3 ~/.workbuddy/skills/tech-digest-to-html/scripts/validate_html.py <文件路径>` 输出 `全部 8 项静态自检通过！Exit Code: 0`。
4. **计算模型对齐**：前端 JS 沙盘计算出的拐点、服务率、平衡点与后端 Python/数学推导一致至小数点后 4 位。
5. **运行时冒烟零失败**：Stage 5.5 的 DOM 垫片冒烟测试断言全绿（逐槽位比对，含边界钳制与 NaN/Infinity 扫描）。

---

## 6. 编码期必须规避的两个自检误报（已实证）

写码时就避开，不要等自检报错再返工：

| 误报 | 触发写法 | 报错原文 | 正确写法 |
| :--- | :--- | :--- | :--- |
| **第 8 项 LaTeX 误判** | 把 DOM 选择器助手命名为 `$`，写成 `$("id")` 或 `var el = $(id);` | `检测到未渲染的行内 LaTeX 占位符，如 '$("chk-refuse") &&$'` | 助手改名为 `byId`，全文用 `byId("id")`。检测器按 `$...$` 成对匹配，JS 里的 `&&` 与 `$(` 会拼成假占位符 |
| **第 7 项悬空组件误判** | 只承载**静态规则说明**的元素也用 `out-` 前缀 ID（如 `id="out-m1-note"` 存公式说明） | `数据显示容器 #out-m1-note 未在 JavaScript 中发现回写逻辑` | 前缀分级：**`out-` 只给 JS 真实回写的槽位**；静态说明文本用 `rule-`（或 `note-`）前缀。检测器靠 `out-` 前缀识别槽位，不区分是否被写 |

## 7. DOM 垫片冒烟测试的必备表面（Node 侧）

垫片必须实现下列成员，否则内联脚本一执行就抛错，测不出真实问题。`data-*` 与控件初始状态一律**从生成好的 HTML 正则抽取**，禁止手工录入（手工录入一旦错位，会把页面正确逻辑误判为错误）：

> **抽取正则的嵌套陷阱（2026-09-10 实证，必看）**：用**全局**元素正则
> `/<(\w+)[^>]*\bid=["']([^"']+)["'][^>]*>([\s\S]*?)<\/\1>/g` 批量抽静态文本，
> 外层容器（`<div id="main">`、`<aside id="sidebar">`）会**先命中并吞掉全部子节点**，
> `lastIndex` 直接跳到容器尾部，导致所有内层槽位的静态初值抽成空串 ——
> 表现为「36 个槽位 36 处不一致」的**假阳性**，实际页面完全正确。
> **正确做法：先收集全部 id，再逐个 id 单独构造正则定位**
> （`new RegExp('<(\\w+)([^>]*)\\bid="' + esc(id) + '"([^>]*)>([\\s\\S]*?)<\\/\\1>')`），
> 利用 `\bid="<具体id>"` 锚定到最内层元素。

- `document.getElementById` → **自动建桩**（`ensure` 而非 `get`）。只预注册 input/select 的 ID 会导致所有 `out-*` 显示槽位静默返回 null，写入被丢弃，表现为满屏 `missing`。应从 HTML 抽取**全部** `id="..."` 统一注册。
- `document.documentElement` → 需 `getAttribute` / `setAttribute` / `scrollHeight` / `clientHeight` / `scrollTop`（阅读进度条与主题切换依赖）。
- `document.querySelectorAll(sel)` → 侧栏高亮用；返回**真数组**（脚本内会 `Array.prototype.slice.call`）。
- `document.querySelector` → 锚点目标可一律返回 `null`（验证不抛异常即可）。
- `document.body.scrollTop`、`window.addEventListener`、`window.localStorage` → 后者**故意留 undefined**，用于验证隐私模式 `try/catch` 分支。
- 元素桩：需 `textContent` 读写、`className` + `classList`（`add/remove/toggle/contains`）、`value`、`checked` getter/setter、`style`、`open`、`getAttribute/setAttribute`、`closest()`、`getBoundingClientRect()`、`addEventListener` 收集 + `fire(type)` 触发。

断言清单模板：① 每个沙盘的初始态；② 每个分支（含边界钳制，如 k > N、改善后 > 改善前）；③ 结果串扫描 `NaN` / `Infinity` / `undefined`；④ 主题切换、目录开关、进度条写入。

**垫片用 `require()` 加载时，必须显式发布全局（2026-09-10 实例）**：
把垫片写成 `shim.js` 再 `require()`，其中的 `var document = {...}` 是**模块作用域**，
在另一个文件里 `eval()` 内联脚本会直接抛 `ReferenceError: document is not defined`。
垫片末尾必须补：

```js
global.document = document;
global.window = window;
global.IntersectionObserver = undefined;
```

**改 Skill 只能改单一真值源，改运行时的副本会被 `--apply` 反向覆盖（2026-09-10 实例）**：
三处作用域中，`AIKnowledge/skills/tech-digest-to-html` 是 SOURCE，另外两处是运行时副本。
直接编辑全局或项目级 SKILL.md 后再跑 `sync_skill.py --apply`，改动会被源版本**静默回滚**
（只是生成一份 `.bak_<时间戳>`）。正确顺序：先改 SOURCE → 再 `--apply` → 再 `--check`。
`--apply` 生成的 `.bak_*` 目录位于 `skills/` 同级会被误当作独立 Skill 扫描，须及时清理。

**静态初值与 `toFixed` 位数不一致的真实捕获（2026-09-10 实例）**：
手写槽位 `<span id="out-rl-sneed">0.9947</span>`，而 JS 侧是 `sNeed.toFixed(5)` → `0.99475`。
8 项静态自检**全绿**（它不比对静态文本与 JS 重算值），只有冒烟测试阶段 1 的逐槽位比对能抓到。
防御：凡是写进 HTML 的静态回显初值，一律先在 Python 侧用**完全相同的格式化表达式**（`%.5f` 对应 `toFixed(5)`）算出再粘贴，
不要靠目测截断小数位。

---

## 8. 存量文档排版基线统一（Batch Layout Baseline Unification）

需要对**已存在的多份 HTML**统一视觉风格时，严禁逐份手改 CSS（成本高、必然漂移）。
统一流水线：**先基线注入 → 再静态自检 → 最后反证零回归**。

### 8.1 配套脚本（`scripts/`）

| 脚本 | 作用 |
| :--- | :--- |
| `unify_layout_baseline.py` | 在每份文档 `</style>` 前追加「统一排版基线层」，**幂等**（靠首尾注释识别，可重复执行） |
| `runtime_smoke.js` | Node 最小 DOM 垫片运行时冒烟：扫全量 id 槽位的 NaN/undefined，含主题控件点击分支 |
| `check_js_dom_bindings.py` | 反向核验 JS 里 `getElementById/querySelector('#id')` 的目标在 HTML 中真实存在（自检第 4 项只验「锚点→DOM」正向，不覆盖此方向）。**用法**：`python3 check_js_dom_bindings.py <file.html>` 显式指定文件（推荐，单文档交付流程用这个）；无参数时自动扫描唯一存储目录全部 `YYYYMMDD_*.html`。历史上曾硬编码 6 份文档清单导致新文档不被检查、且硬编码路径失效直接崩溃（2026-09-10 已修复），凡内置清单式脚本一律要求支持 argv 参数 |

#### 8.1.1 大媒体资产的内嵌裁决规则（图片/视频混合文档）

「零外部依赖」与「单文件可控体积」冲突时的裁决顺序（2026-09-10 Astra 建筑可视化案例实证）：

1. **先探测体积再定策略**：用 `curl -sI` 读 `Content-Length`，逐资产列出字节量，禁止拍脑袋。
2. **图片（单张 ≤ 800KB）→ Base64 data URI 全量内嵌**：先 `file` 命令校验 RIFF/WEBP 等文件签名防下载损坏，再注入 `data:image/webp;base64,...`。22 张图（2.82 MB 原始 → 3.83 MB 成品）实测可用。
3. **视频（单段 > 10MB）→ 严禁内嵌**：4 段 1080p WebM/MP4 合计 53.6 MB，base64 膨胀 1.33x 后 ~71 MB，文件双击打开会卡死浏览器、编辑器无法加载。改用「官方海报帧（内嵌）+ `<a>` 新窗口直链 + 视频未内嵌说明卡（含体积与需联网提示）」承载，语义与信息量不丢失。
4. **验证闭环追加两步**：① Python 侧 `base64.b64decode` 后校验 `RIFF/WEBP` magic bytes（防 base64 转写损坏）；② 对占位符替换脚本断言「无 leftover `@@IMG:` 残留」，否则静默漏图。

### 8.2 基线层的四个设计要点（踩过的坑）

1. **令牌映射，而非令牌替换**：存量文档历史变量名千差万别（`--bg-canvas`/`--bg-card`/`--panel`/`--surface-1`…）。
   注入层同时定义统一令牌 `--aike-*` **与**「该文件历史变量名 → 统一基线色值」的兼容映射，
   既有 CSS 一行不改即可吃到新配色。**禁止**把历史变量写成 `var(--x)` 自引用（同名必 undefined）。
2. **三种主题机制必须等价覆盖**：`html[data-theme="dark"]`、`html.dark`（class 方案）、
   `@media (prefers-color-scheme:dark)`。系统偏好那条务必带
   `:not([data-theme="light"]):not([data-theme="dark"]):not(.dark)`，否则显式指定会被系统偏好反向覆盖。
   只匹配 `[data-theme]` 会漏掉 class 方案的文档（实战中已踩）。
3. **用 `:is()` 抬特异性**：`body h2` 仅 (0,0,2)，打不过文件内的 `.content h2` (0,1,1)。
   基线层的标题/组件规则统一写成 `:is(body,main,.content,.page,…) h2`，抬到 (0,1,1) 再靠源码顺序取胜。
4. **只动样式层，不碰 DOM id 与 JS**：这是零回归的前提。确需新增控件（如补齐缺失的主题切换按钮）时，
   JS 必须 IIFE + 前缀变量名（`uBtn`/`UKEY`）封装，避免与宿主脚本 `var` 提升到同一作用域互相劫持。

### 8.3 零回归判定 = 反证，不能只看自检全绿

静态 8 项自检只校验语法层，**证明不了没有引入回归**。改动前先留档，同一垫片跑两份对比：

```bash
cp <原文件> /tmp/backup/
python3 scripts/unify_layout_baseline.py && node scripts/runtime_smoke.js <改后文件>
node scripts/runtime_smoke.js /tmp/backup/<原文件>
```

两份输出必须**逐条一致**：备份上也复现的告警属既有问题，不得记到本次改动头上；
只有「备份通过、改后失败」的差异项才是真回归。

### 8.4 垫片的保真度边界（误报来源）

`runtime_smoke.js` 用 Node 模拟 DOM，以下浏览器原生行为复现不了，出告警先对照此表排除假阳性：

- `localStorage` **故意留空**用于验证隐私模式 try/catch 分支；宿主脚本裸写 `localStorage.getItem()`
  会抛 `ReferenceError`。这同时也是真实健壮性缺陷 —— 应给**宿主脚本**补 try/catch，而不是给垫片打补丁。
- `<input type="range">` 未显式写 `value` 时浏览器取 min/max 中值，垫片只能退化为 `min`（或 0）。
- `<select>` 默认值依赖 option 解析，选项若无 `value` 属性则取不到。

### 8.5 AIKnowledge 统一配色基线（暖羊皮纸 / 黑曜石）

浅色 `#FAF7F2` / 深色 `#181715`；强调色陶土 `#D97757`（深色态提亮为 `#E2886A`）。
任何新文档若强调色偏离此值（如靛蓝 `#4f46e5`、砖红 `#C95D3B`），一律判定为风格漂移，须由基线层校正。

### 8.6 默认主题 = 深色（Default Dark）

知识库所有文档默认以**深色（黑曜石）**呈现。切换默认主题必须「静态属性 + JS 初始化」**双向都改**：

| 只改一边 | 后果 |
| :--- | :--- |
| 只改 JS 初始化 | 首屏闪白（FOUC）—— 脚本在 DOM 解析后才执行，属性落地前已按浅色绘制一帧 |
| 只改 `<html>` 属性 | 运行时被 JS 初始化覆盖回去 —— 无存储偏好时普遍回落系统偏好或硬编码的 light |

按主题机制分别处理：

- **`[data-theme]` 方案**（多数）：`<html data-theme="dark">`。
- **`html.dark` class 方案**（如 Uber）：`<html class="dark">`，**且**须把 JS 中「无存储偏好」分支从
  `if (matchMedia("(prefers-color-scheme: dark)").matches) add("dark")` 改为**无条件** `add("dark")`；
  否则系统为浅色时仍会被判定成浅色。
- **纯 `@media` 方案**：补 `data-theme="dark"`，并把 JS 默认从 `null`（跟随系统）改为 `'dark'`。

**自查**：改完用 `runtime_smoke.js` 触发主题控件点击，回显应从 `dark` 切到 `light`；
若反从 `light` 切到 `dark`，说明默认深色没生效。

**踩坑（正则替换已存在的属性）**：模式 `(\sattr=")[^"]*"` 的匹配串**包含结尾引号**，
替换模板必须补回 `'"'`，否则产出 `data-theme="dark data-page-node-id="…` 这类**畸形标签**。
替换后务必校验 `<html>` 标签的引号成对。

### 8.7 侧栏贴左 · 正文在剩余区域居中（消除右侧多余留白）

在桌面宽屏（1440px / 1920px / 2K / 4K）环境下，针对带有侧栏目录的文档，**严禁将正文仅凭固定 `margin-left` 贴着侧栏排布**，否则正文右侧会留下巨大的荒废空白区（严重失衡）。

#### ① 视觉与布局目标
- **左边侧栏目录**：稳固贴在屏幕最左侧（宽度 $S = \text{var(--aike-sidebar-w)}$，默认 280px）。
- **正文阅读内容**：在除去侧栏后的**剩余视口区域**中，**绝对水平居中展示**，最大宽度 $C = \text{var(--aike-content-max)}$（1180px）。
- **左右留白恒等**：侧栏右边缘到正文左边缘的留白，严格等于正文右边缘到屏幕右边界的留白。

#### ② 数学模型与 CSS 盒模型实现
令包含块（视口）宽度为 $100\%$，侧栏宽为 $S$，正文最大宽为 $C$：
$$\text{autoMargin} = \max\left(0\text{px}, \frac{100\% - S - C}{2}\right)$$
$$\text{marginLeft} = S + \text{autoMargin}$$
$$\text{marginRight} = \text{autoMargin}$$

实证推导：
$$\text{左侧空白} = \text{marginLeft} - S = \text{autoMargin} = \text{marginRight} = \text{右侧空白}$$

```css
/* 统一排版基线注入层：纯 CSS 自动对称居中 */
body:has(> .app-sidebar, > aside.app-sidebar, > .sidebar, > aside.sidebar, > .sidebar-nav){
  display: block !important;
}

body:has(> .app-sidebar, > aside.app-sidebar, > .sidebar, > aside.sidebar, > .sidebar-nav)
  > :is(.app-main, main, .main, .content-area, .main-content, .page-wrap, .main-wrapper){
  display: block !important;
  max-width: var(--aike-content-max) !important;
  width: auto !important;
  flex: none !important;
  margin-left: calc(var(--aike-sidebar-w) + max(0px, (100% - var(--aike-sidebar-w) - var(--aike-content-max)) / 2)) !important;
  margin-right: max(0px, calc((100% - var(--aike-sidebar-w) - var(--aike-content-max)) / 2)) !important;
  box-sizing: border-box !important;
}

@media (max-width: 1080px){
  body:has(> .app-sidebar, > aside.app-sidebar, > .sidebar, > aside.sidebar, > .sidebar-nav)
    > :is(.app-main, main, .main, .content-area, .main-content, .page-wrap, .main-wrapper){
    margin-left: 0 !important;
    margin-right: 0 !important;
    max-width: 100% !important;
    width: 100% !important;
    padding-left: 20px !important;
    padding-right: 20px !important;
  }
}
```

#### ③ 为什么禁止改用 `position: sticky`？（深坑防御）
很多实现倾向于将侧栏改为 `position: sticky`，但这在以下场景会直接崩塌：
- 若页面祖先元素（包括 `body` 或 `html`）声明了 `overflow-x: hidden`（长文排版防溢出的常见写法），CSS 规范规定 `sticky` 将**彻底失效退化为相对定位**，滚动时侧栏直接滚出屏幕！
- 保留 `position: fixed` + 经典块级盒模型（`display: block`），完全免疫任何祖先的 `overflow-x: hidden`，同时零破坏移动端的抽屉滑出交互。

