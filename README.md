# AIKnowledge 前沿工程白皮书与系统架构知识库

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Architecture: Zero-Dependency](https://img.shields.io/badge/Architecture-Zero--Dependency-success.svg)]()
[![Status: Production-Grade](https://img.shields.io/badge/Status-Verified-green.svg)]()

本知识库是一套专注于**多智能体工程化（Agentic Engineering）、自适应 Harness 演进、Fleet 调度治理、AI 原生软件工程（AI-Native SDLC）及企业级落地实证**的前沿白皮书与技术专著集合。

不同于二次转述与定性概述，本库所有成果均坚持**“实证核验（Primary Source Verification）、数学推导建模、零造假可计算沙盘与零外部依赖（Zero External Dependencies）”**的严谨工程交付标准。

---

## 一、知识库核心治理三大铁律

本知识库在资产组织、命名与交付形态上严格执行以下治理准则：

### 1. 唯一存储路径（Strict Single Directory）
- **根目录托管**：所有技术专著、架构白皮书及实施指南统一保存在仓库根目录，杜绝散落在临时目录、子文件夹或非标准路径中。

### 2. 语义与日期命名规范（Semantic & Date Standard）
- **统一命名模式**：`[YYYYMMDD]_[核心主题].html`
- **一目了然与时序检索原则**：文件名以 8 位公历年月日开头并紧随单个下划线（如 `20260903_`），后半部分控制在 8~30 字以内清晰标识技术核心领域与体裁。文件系统、资源管理器与终端按自然字典序呈现严格的时间线演进，严禁包含“最终版/临时版/草稿/修正版”等非规范修饰词。

### 3. 自包含单文件原则（Zero-Dependency Single-File Rule）
- **独立交付**：每个技术成果均为完全自闭环的单文件 HTML 文档。
- **绝对零外部依赖**：杜绝外部 CDN、远程 CSS/JS 及网络字体；图表全量采用原生内联 SVG，数学排版采用纯原生 CSS 排版引擎（KaTeX-Free），断网双击即可无损渲染与完整交互。
- **严禁伴生文件**：杜绝伴生副文件（无外部 `.md`、临时脚本或外链依赖），保证资产的可移植性与永久可归档性。

---

## 二、知识资产全景矩阵

知识库按技术领域解构为五大核心板块，涵盖 13 篇深度白皮书：

### 1. 软件工程与开发生命周期（AI-Native SDLC & Software Factory）

| 交付成果 | 核心理论与形式化模型 | 关键工程机制与交互沙盘 | 资产文件 |
| :--- | :--- | :--- | :--- |
| **Anthropic AI 原生 SDLC 实施指南** | • 阿姆达尔瓶颈迁移定律：$S_{\text{overall}} \le \frac{1}{(1-p) + p/s}$<br>• M/M/1 排队论与 CONWIP 准入控制<br>• USL 通用可扩展性与写偏序参数膨胀模型<br>• 假绿逃逸概率：$P_{\text{esc}} = d(1-c_1)m(1-c_2)$ | • 6 大双向绑定物理沙盘（阿姆达尔瓶颈推演、审查队列雪崩模拟、黄金 Eval 集反解器等）<br>• 渐进式扩权硬门控决策矩阵 | [`20260903_AI原生SDLC软件工程实施白皮书.html`](./20260903_AI原生SDLC软件工程实施白皮书.html) |
| **Uber 超大规模软件工厂落地指南** | • 业务周活 7x 下总支出趋稳的六乘数成本公式<br>• 帕累托前沿评测路由模型<br>• Prompt 缓存 TTL 节奏工程（主线程 1h vs 子智能体 5min） | • 3 大可计算沙盘（六乘数敏感度模拟器、TTL 盈亏平衡计算器、code-mode 宽表查询压降沙盘）<br>• 六大底座基础设施与 Inner-loop 前移验证 | [`20260903_Uber超大规模软件工厂落地指南.html`](./20260903_Uber超大规模软件工厂落地指南.html) |
| **两千小时 AI 代码工程与调度治理白皮书** | • Harness 动态装配成本方程与盈亏平衡点 $n^*$<br>• 注意力有效服务率衰减：$\mu_{\text{eff}} = \frac{60}{T \cdot (1 + \gamma(N-1))}$<br>• 投机执行预发送期权定价：$p^* = \frac{C_{\text{rollback}}}{V_{\text{time}} + C_{\text{rollback}}}$ | • 4 层调度系统解构（统一入口、状态调度、执行环境、工程治理）<br>• CONWIP 准入与 USL 峰值倒挂仿真沙盘 | [`20260903_两千小时AI代码工程与调度治理白皮书.html`](./20260903_两千小时AI代码工程与调度治理白皮书.html) |
| **CodexHarness 开源底座与业务集成指南** | • Harness 动态沙箱隔离与环境自愈<br>• 业务系统接入的渐进式适配拓扑 | • 开源底座接入架构与环境生命周期管理沙盘 | [`20260904_CodexHarness开源底座与业务集成指南.html`](./20260904_CodexHarness开源底座与业务集成指南.html) |

### 2. 多智能体架构与调度治理（Agent Architecture, Harness & Fleet Systems）

| 交付成果 | 核心理论与形式化模型 | 关键工程机制与交互沙盘 | 资产文件 |
| :--- | :--- | :--- | :--- |
| **JIT-Agent 与 Fleet 双螺旋架构工程白皮书** | • JIT（Just-In-Time）智能体自适应装配拓扑<br>• 双螺旋演进：运行时轻量派生与离线治理反馈<br>• Agent-Fleet 协同调度与分布式锁机制 | • Harness 动态装配流水线<br>• 跨智能体隔离沙箱与上下文精简过滤机制 | [`20260902_JIT-Agent与Fleet双螺旋架构工程白皮书.html`](./20260902_JIT-Agent与Fleet双螺旋架构工程白皮书.html) |
| **Google AI 挑战赛四大工程架构模式白皮书** | • 双向 MCP（Bidirectional MCP / Agent-as-a-Server）复杂度压降：$O(K^2+KM) \rightarrow O(K+M)$<br>• 事件驱动异步总线并发时延收敛<br>• 同标准回退校验一致性约束 | • 4 大动态物理沙盘（级联路由成本对比、事件驱动并发时延分析、回退质量门禁对比）<br>• 三级级联网关正则零 Token 拦截（降本 68%+） | [`20260903_GoogleAI挑战赛四大工程架构模式白皮书.html`](./20260903_GoogleAI挑战赛四大工程架构模式白皮书.html) |
| **Reef 持续学习闭环与自我改进架构** | • CAS 发布链自阻塞定点方程：$\rho = \frac{W(\lambda p D)}{D}$<br>• 经验漏斗陈旧衰减积分：$N_{\text{eff}} = R \cdot c \cdot a \cdot (1-d) \cdot \bar{w}$<br>• AIME 跨臂双比例 $z$ 检验与二项基线噪声分解 | • 4 大零假数据交互沙盘（MDE 与功效反解器、CAS 自阻塞 Lambert W 曲线、经验漏斗瀑布条）<br>• 一级源 GitHub 代码与基线实测勘误 | [`20260903_Reef持续学习闭环与Agent自我改进架构.html`](./20260903_Reef持续学习闭环与Agent自我改进架构.html) |
| **HarnessDev 自主基础设施演化评估白皮书** | • Harness 共适应惩罚模型与跨执行器迁移衰减<br>• 演化噪声滤波与真伪版本晋级决策器<br>• 贝叶斯真实物理完成检查门 | • 4 大可计算沙盘（迁移衰减模拟器、噪声滤波决策器、Token 黑洞沙盘、完成度校验门） | [`20260907_HarnessDev自主基础设施构建与演化评估白皮书.html`](./20260907_HarnessDev自主基础设施构建与演化评估白皮书.html) |
| **Meta 组织级第二大脑构建与专家经验闭环** | • 知识系统与推理配方双层解耦架构<br>• 专家纠错编译为文本补丁与双阶段防退步门禁 | • 3 大动态沙盘（根因归因决策器、渐进式披露 Token 优化仪、防退步门禁模拟器） | [`20260907_Meta组织级第二大脑构建与专家经验闭环.html`](./20260907_Meta组织级第二大脑构建与专家经验闭环.html) |
| **持久在线 AI 同事协作协议工程白皮书** | • 异步协同时序协议与状态持久化拓扑<br>• 知识分发与人机混合协作信道模型 | • 交互协作沙盒与协议状态机仿真器 | [`20260904_持久在线AI同事协作协议工程白皮书.html`](./20260904_持久在线AI同事协作协议工程白皮书.html) |
| **WikiSkill 持久经验库与 Agent 技能演进架构** | • 动态技能沉淀与版本化生命周期演进<br>• 组织知识蒸馏拓扑 | • 技能演化沙盘与知识检索效用计算器 | [`20260904_WikiSkill持久经验库与Agent技能演进架构.html`](./20260904_WikiSkill持久经验库与Agent技能演进架构.html) |

### 3. 垂直场景与参考架构（Domain Applications & Industry Architecture）

| 交付成果 | 核心理论与形式化模型 | 关键工程机制与交互沙盘 | 资产文件 |
| :--- | :--- | :--- | :--- |
| **Anthropic 电商 Agent 双端架构与落地指南** | • 缓存盈亏平衡反解：$h^* = \frac{0.25}{1.15} \approx 21.74\%$<br>• 易失性前缀错位代价：$0.9 \cdot (G+S)$<br>• 安全链串联失效率：$P_{\text{bypass}} = \prod \epsilon_i$<br>• 快照评测捕获概率方程：$P(n) = 1 - (1-q)^n$ | • 5 大零造假沙盘（缓存经济学反解、前缀错位堆叠对比、单轮延迟预算时间轴、写入后状态安全校验）<br>• 一手博客与仓库源码交叉勘误 | [`20260903_Anthropic电商Agent双端架构与工程落地指南.html`](./20260903_Anthropic电商Agent双端架构与工程落地指南.html) |
| **Anthropic 电商 Agent 参考架构深度拆解** | • 消费端（Shopping）与商家端（Merchant）双 Agent 模式<br>• 500~700 Token 延迟预算与流式 Eager Dispatch<br>• 读写权限分离与写入后状态幂等防护 | • 十大电商 Skills 模块化定义与运行时拓扑<br>• 架构对照表与部署环境演进清单 | [`20260903_Anthropic电商Agent参考架构与工程实践深度拆解.html`](./20260903_Anthropic电商Agent参考架构与工程实践深度拆解.html) |
| **Anthropic 电商与 Ulike-Agent 经营分析方案** | • 双端架构向经营分析场景的映射融合<br>• 指标诊断、归因推演与经营决策执行回路 | • 经营分析闭环沙盘与架构对照看板 | [`20260904_Anthropic电商Agent与Ulike-Agent架构与经营分析迭代方案.html`](./20260904_Anthropic电商Agent与Ulike-Agent架构与经营分析迭代方案.html) |
| **Ulike-Agent 经营分析统一优化迭代方案** | • 源码级事实对齐与设计实施路线<br>• Runtime-Diagnosis-Evidence-Handoff-Controlled Action | • 优化演进全景路线图与交付验证门禁 | [`20260904_Ulike-Agent经营分析统一优化迭代方案.html`](./20260904_Ulike-Agent经营分析统一优化迭代方案.html) |
| **Grok Bot 任务定义方法与 26 份双语模板集** | • 任务可行性维（C1–C4，92.3%）与共处性维（C5–C6，46.2%）失衡分布<br>• 风险面 $R$ 与禁止条款 $P$ 的 OLS 回归模型（$r = 0.7865$）<br>• 凸性加速跳跃稳健性检验 | • 4 大交互沙盘（形态筛选矩阵、OLS 散点拟合拟合器、12 字段岗位卡自检器、双语模板浏览器）<br>• 26 份完整中英双语提示词与导入 URI | [`20260903_GrokBot模板任务定义方法与26份双语模板集.html`](./20260903_GrokBot模板任务定义方法与26份双语模板集.html) |
| **Grok Bot 八大工作流模板与可复用 Agent 系统** | • 任务模块化与八大经典工作流拓扑<br>• 跨场景复用与输入输出契约 | • 八大模板交互浏览器与任务组装沙盒 | [`20260907_GrokBot八大工作流模板与可复用Agent系统.html`](./20260907_GrokBot八大工作流模板与可复用Agent系统.html) |
| **Grok Bot 跨会话持久 Agent 系统设计复盘** | • 跨会话状态持久化与上下文衰减补偿<br>• 记忆加载与增量更新拓扑 | • 状态流转沙盘与持久化存储校验器 | [`20260904_GrokBot跨会话持久Agent系统设计与交互架构复盘.html`](./20260904_GrokBot跨会话持久Agent系统设计与交互架构复盘.html) |
| **Grok Bot 十一条工作流搭建指南** | • 业务工作流拆解与 Agent 编排流水线 | • 工作流搭建 Checklist 与交互拓扑 | [`20260904_GrokBot十一条工作流与Agent工作系统搭建指南.html`](./20260904_GrokBot十一条工作流与Agent工作系统搭建指南.html) |
| **Grok Bot 五团队七步 Agent 组织落地指南** | • 组织微架构重组与 Agent 团队角色切分<br>• 七步渐进式落地 SOP | • 组织就绪度评估沙盘与团队协同拓扑 | [`20260904_GrokBot五团队七步Agent组织落地指南.html`](./20260904_GrokBot五团队七步Agent组织落地指南.html) |

### 4. 团队落地实战与开发者生态（Startup Best Practices & Developer Guides）

| 交付成果 | 核心理论与形式化模型 | 关键工程机制与交互沙盘 | 资产文件 |
| :--- | :--- | :--- | :--- |
| **Claude Code 初创企业实战落地指南 (20260903)** | • 15 家高增长初创公司落地路径对比<br>• 五大工程规则全景演进<br>• Agentic 团队就绪度与 ROI 测算模型 | • 15 家公司分类筛选与实践沙盘<br>• 官方 4 章 11 项 Checklist 交互勾选器（支持本地持久化）<br>• 7 幅高保真内联 SVG 架构图 | [`20260903_ClaudeCode初创企业实战落地指南.html`](./20260903_ClaudeCode初创企业实战落地指南.html) |
| **Claude Code 初创企业实战落地指南 (20260904)** | • 深度演进与多模态扩展落地清单 | • 初创企业全流程落地沙盘升级版 | [`20260904_ClaudeCode初创企业实战落地指南.html`](./20260904_ClaudeCode初创企业实战落地指南.html) |
| **Claude Code 会话管理与 Token 优化指南** | • 会话生命周期与上下文修剪机制<br>• Token 消耗精细化核算模型 | • Token 消耗敏感度沙盘与压缩模拟器 | [`20260904_ClaudeCode会话管理与Token优化指南.html`](./20260904_ClaudeCode会话管理与Token优化指南.html) |
| **Claude Fable 5.1 提示指南与运行时迁移** | • 16 种异常现象与 4 大控制面归因映射<br>• 前缀不可变（prefix immutability）事件日志模型<br>• 批处理工具调用时延压降方程 | • 3 大交互沙盘（16 类症状诊断矩阵、5 档 Effort 思考预算动态决策沙盘、网络 RTT 收益模拟器）<br>• 7 步风险排序运行时迁移清单 | [`20260903_ClaudeFable5.1提示词指南与Agent运行时迁移清单.html`](./20260903_ClaudeFable5.1提示词指南与Agent运行时迁移清单.html) |
| **Anthropic 前沿部署工程师（FDE）面试指南** | • 稳定性剪刀差模型：$\text{pass@}k$ 与 $\text{pass}^k$ 的非线性分离<br>• 置信区间反解样本量方程：$N \ge \frac{\ln(1-C)}{\ln(1-\epsilon)}$<br>• 动作边界 × 数据敏感度风险分级模型 | • 5 大工程交互沙盘（能力雷达闭合度计算器、稳定性剪刀差模拟器、风险分级决策器、43项备考看板）<br>• 官方职位数据与 Eval 官方术语一手核验 | [`20260903_Anthropic前沿部署工程师FDE面试指南.html`](./20260903_Anthropic前沿部署工程师FDE面试指南.html) |
| **GPT-6 Astra 实战工作法与人机协作再分配** | • Tooling for Inspectability 与 Direction vs Nuance 原则<br>• 产品反馈模式与专用预览播放器构建 | • 5 大工作法解构沙盘与人机职责再分配矩阵 | [`20260907_GPT6-Astra实战工作法与人机协作再分配指南.html`](./20260907_GPT6-Astra实战工作法与人机协作再分配指南.html) |
| **AI 编程工作流与上下文工程体系指南** | • 多维上下文空间编排拓扑<br>• 动态记忆注入与注意力带宽保护 | • 交互式上下文工作流沙盒 | [`20260904_AI编程工作流与上下文工程体系指南.html`](./20260904_AI编程工作流与上下文工程体系指南.html) |
| **Weaviate 上下文工程系统地图与六大能力** | • 混合检索与向量拓扑优化<br>• 上下文注入吞吐模型 | • 向量索引与上下文性能仿真沙盒 | [`20260904_Weaviate上下文工程系统地图与六大能力白皮书.html`](./20260904_Weaviate上下文工程系统地图与六大能力白皮书.html) |
| **Cursor 全天候代理团队架构约束与验证规范** | • 持续运行 Agent 的状态漂移防护<br>• 自动化测试与红线阻断门禁 | • 全天候代理沙盒仿真器 | [`20260904_Cursor全天候代理团队架构约束与验证规范.html`](./20260904_Cursor全天候代理团队架构约束与验证规范.html) |
| **设计工程审美体系与 Agent 界面审查架构** | • 同心圆角共形几何方程与调和字阶行高衰减<br>• OKLCH 感知亮度与 WCAG 对比度度量<br>• Git Diff 爆炸半径展开与三相缺陷裁决自动机 | • 4 大动态沙盘（圆角共形变形器、字阶带宽沙盘、OKLCH 度量仪、Diff 影响面沙盒）<br>• 12 条工程红线与时序审查管道 | [`20260907_设计工程审美体系与Agent界面审查架构白皮书.html`](./20260907_设计工程审美体系与Agent界面审查架构白皮书.html) |

### 5. 认知决策、商业战略与时代推演（Cognitive Models, Strategy & Future Deduction）

| 交付成果 | 核心理论与形式化模型 | 关键工程机制与交互沙盘 | 资产文件 |
| :--- | :--- | :--- | :--- |
| **AI 时代二阶思考决策模型白皮书** | • 水波外走五层涟漪效应推导模型<br>• 认知能力留存指数衰减方程<br>• 顶尖研究团队实证样本归纳（MIT、CMU、Harvard、柳叶刀临床） | • 3 大动态沙盘（涟漪穿透模拟器、六大微决策交互演练台、外包矩阵与认知留存评估器）<br>• 结构化思考脚手架与四步前置决策路径 | [`20260903_AI时代二阶思考决策模型白皮书.html`](./20260903_AI时代二阶思考决策模型白皮书.html) |
| **SaaS 巨头反扑与垂直 AI 终极护城河** | • 数据重力与工作流锁死模型<br>• 垂直 AI 价值链重构与防御深度推演 | • 竞争博弈仿真沙盘与价值捕获计算器 | [`20260904_SaaS巨头反扑与垂直AI终极护城河.html`](./20260904_SaaS巨头反扑与垂直AI终极护城河.html) |
| **商业竞争 80 种赢法与护城河策略图谱** | • 商业模式拓扑空间与 80 种战略赢法解构<br>• 多层护城河防御模型 | • 80 种赢法交互矩阵与竞争策略选择器 | [`20260904_商业竞争80种赢法与护城河策略图谱.html`](./20260904_商业竞争80种赢法与护城河策略图谱.html) |
| **数字文艺复兴人与一人企业能力栈指南** | • 超级个体全栈技术-商业闭环拓扑<br>• 边际成本归零与杠杆放大模型 | • 一人企业能力雷达与资产跃迁评估器 | [`20260904_数字文艺复兴人与一人企业能力栈指南.html`](./20260904_数字文艺复兴人与一人企业能力栈指南.html) |
| **无雇佣时代企业消融与超级个体资产跃迁** | • 科斯交易成本归零下的组织消融理论<br>• 个人算力杠杆与超级个体资产配置模型 | • 组织解构沙盒与资产跃迁推演器 | [`20260907_无雇佣时代企业消融与超级个体资产跃迁.html`](./20260907_无雇佣时代企业消融与超级个体资产跃迁.html) |
| **未来推演：当不再有大规模雇佣白皮书** | • 生产要素替代指数与科斯管理成本坍塌<br>• 经营能力资产化与逃逸速度模型<br>• 制度乌云与分配速率失配分析 | • 4 大动态沙盘（要素替代杠杆器、边界坍塌模拟器、逃逸速度计算器、双极化分配图谱） | [`20260907_未来推演当不再有大规模雇佣白皮书级深度消化.html`](./20260907_未来推演当不再有大规模雇佣白皮书级深度消化.html) |

---

## 三、技术规范与质量保证（QA Standards）

知识库内所有 HTML 白皮书均经过静态检查工具链的全量自动化校验，确保符合以下标准：

```
                 +------------------------------------------------+
                 |          HTML 成果自动化交付验证流水线           |
                 +------------------------------------------------+
                                          |
        +---------------------------------+-------------------------------+
        |                                 |                               |
        v                                 v                               v
[1. 结构与格式规范]              [2. 内容与排版引擎]             [3. 交互与运行时闭环]
• 严格文件名正则校验             • 原生 CSS 数学排版引擎         • 原生 JS AST 语法无错
• DOM 标签平衡栈检测             • 零外部网络字体与 CDN          • 控件与回显槽位 100% 闭环
• 全局实体锚点 100% 可达         • 内联原生 SVG 矢量图谱         • 双路 Python/JS 精度复算
• 媒体资产无损坏断链             • 零未渲染裸露 LaTeX            • 本地持久化与打印适配
```

1. **零外部依赖（Zero External Dependencies）**：不使用外链 CSS、JS、Web Font 或第三方图床；即便完全处于离线或断网环境，图表、排版与数学公式亦能 100% 正常显示。
2. **纯原生数学排版引擎（KaTeX-Free Native CSS Engine）**：摒弃体积庞大且易引发渲染时延的第三方数学库，采用原生 CSS Grid/Flex 与 Unicode 符号系统进行公式结构化排版，彻底消除公式加载闪烁与裸露 LaTeX 代码。
3. **真实公式双路交叉复算**：交互沙盘内的所有推导公式与回归方程（如 Lambert W 迭代、正态分布误差函数 erf、OLS 回归斜率等），均由 Python 脚本与前端原生 JavaScript 双路独立实现并交叉校验至小数点后 4 位，严禁伪造数据与虚假随机。
4. **全平台自适应与双主题系统**：每篇白皮书均预装“黑曜石暗夜（Obsidian Dark）”与“暖羊皮纸（Parchment Light）”双主题切换、系统级目录滚动监听及完备的打印排版样式（`@media print`）。

---

## 四、查阅与使用指南

### 本地阅读
- 本知识库专著均为独立 HTML 文档，**直接双击任何 `.html` 文件**即可在任意现代浏览器（Chrome、Safari、Edge、Firefox）中顺畅阅读并使用交互沙盘。

### 静态服务预览
如需通过本地 HTTP 服务统一浏览，可在仓库根目录下执行：

```bash
# Python 3 简易服务
python3 -m http.server 8080

# 或使用 Node.js http-server
npx http-server . -p 8080
```
启动后访问 `http://localhost:8080`，点击相应文件名即可查看。

---

## 五、工程工具链（Skills）

知识库的交付与治理由 `tech-digest-to-html` Skill 承载。该 Skill 依**作用域**分三处存放，缺一不可：

| 作用域 | 路径 | 加载时机 | 入库 |
| :--- | :--- | :--- | :--- |
| **全局 / 用户级** | `~/.workbuddy/skills/tech-digest-to-html` | 所有项目生效 | 否 |
| **项目级** | `.workbuddy/skills/tech-digest-to-html` | 仅本工作区生效，可覆写全局同名 Skill | 否（`.gitignore` 排除） |
| **可见权威副本** | `skills/tech-digest-to-html` | 不参与加载，供查看 / 评审 / 版本化 | **是** |

以仓库内可见副本 `skills/` 为**单一真值源**，改动后通过同步器分发到另外两处：

```bash
python3 skills/tech-digest-to-html/scripts/sync_skill.py --check   # 只读比对三处差异
python3 skills/tech-digest-to-html/scripts/sync_skill.py --apply   # 以可见副本为准同步（自动备份旧副本）
```

### 配套脚本

| 路径 | 说明 |
| :--- | :--- |
| `SKILL.md` | 五阶段作业流规范：事实核验 → 可计算建模 → 零依赖架构 → 交互沙盘 → 静态自检；另含第 8 章「存量文档排版基线统一」 |
| `scripts/validate_html.py` | 8 项阻断式静态自检：命名合规、零外部依赖、标签平衡、锚点可达、JS AST、SVG 坐标、控件接线、LaTeX 泄漏 |
| `scripts/unify_layout_baseline.py` | 向存量文档 `</style>` 前幂等注入「统一排版基线层」（暖羊皮纸 / 黑曜石 + 陶土强调色） |
| `scripts/runtime_smoke.js` | Node 最小 DOM 垫片运行时冒烟，扫描全量槽位的 `NaN` / `undefined` |
| `scripts/check_js_dom_bindings.py` | 反向核验 JS 中 `getElementById` 目标在 DOM 中真实存在 |
| `scripts/sync_skill.py` | 三副本一致性同步器（`--check` / `--apply`） |
| `references/css_math_typography.md` | KaTeX-Free 纯原生 CSS 数学排版规范 |

```bash
# 单篇交付自检
python3 skills/tech-digest-to-html/scripts/validate_html.py <YYYYMMDD>_<核心要义>.html

# 批量排版基线统一（改动前务必留档，改动后用 runtime_smoke.js 做反证对照）
python3 skills/tech-digest-to-html/scripts/unify_layout_baseline.py
```

---

## 六、版权与维护声明

- 本知识库中的原著内容与技术成果归各原著机构与作者（Anthropic、Google Cloud、Uber Engineering、x.ai 及业界资深研究者）所有。
- 深度拆解、数学建模推导、原生交互沙盘及自包含排版由技术团队基于一手源事实严格核验并独立开发。
- 欢迎通过 Issue 或 PR 提出实证勘误与架构推演改进建议。
