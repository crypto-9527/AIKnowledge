#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AIKnowledge 统一排版基线注入器 v1.0
在每份文档的 </style> 前追加一层"统一排版基线"，仅覆盖设计令牌与版式几何，
不触碰任何交互逻辑 / DOM id / 既有 JS。
"""
import re, os

D = "/Users/yangkejin/Documents/Openai/AIKnowledge"

FILES = {
    "FDE":      f"{D}/20260903_Anthropic前沿部署工程师FDE面试指南.html",
    "Uber":     f"{D}/20260903_Uber超大规模软件工厂落地指南.html",
    "AI工作流":  f"{D}/20260904_AI编程工作流与上下文工程体系指南.html",
    "Ulike":    f"{D}/20260904_Ulike-Agent经营分析统一优化迭代方案.html",
    "设计工程":  f"{D}/20260907_设计工程审美体系与Agent界面审查架构白皮书.html",
}

# ---------------------------------------------------------------- 统一基线令牌
LIGHT = """
  --aike-bg:#FAF7F2;
  --aike-bg-soft:#F3EFEA;
  --aike-surface:#FFFFFF;
  --aike-surface-2:#F3EFEA;
  --aike-surface-3:#EAE5DE;
  --aike-text:#2D2A26;
  --aike-text-muted:#6B655E;
  --aike-text-faint:#968F85;
  --aike-border:#E5DFD5;
  --aike-border-soft:#EFEBE4;
  --aike-accent:#D97757;
  --aike-accent-hover:#B55A3C;
  --aike-accent-soft:rgba(217,119,87,.12);
  --aike-accent-contrast:#FFFFFF;
  --aike-emerald:#10B981;
  --aike-emerald-bg:#ECFDF5;
  --aike-rose:#EF4444;
  --aike-rose-bg:#FEF2F2;
  --aike-amber:#F59E0B;
  --aike-amber-bg:#FFFBEB;
  --aike-cyan:#06B6D4;
  --aike-cyan-bg:#ECFEFF;
  --aike-code-bg:#F2ECE2;
  --aike-font-sans:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;
  --aike-font-serif:"Songti SC","SimSun","Newsreader",Georgia,serif;
  --aike-font-mono:ui-monospace,"SF Mono",Menlo,Consolas,"JetBrains Mono",monospace;
  --aike-sidebar-w:280px;
  --aike-container-max:1360px;
  --aike-content-max:1180px;
  --aike-radius-sm:6px;
  --aike-radius-md:10px;
  --aike-radius-lg:16px;
  --aike-shadow-sm:0 1px 3px rgba(90,70,50,.06);
  --aike-shadow-md:0 4px 12px rgba(90,70,50,.08);
  --aike-shadow-lg:0 12px 32px rgba(90,70,50,.12);
  --aike-shadow:none;
"""

DARK = """
  --aike-bg:#181715;
  --aike-bg-soft:#1F1D1A;
  --aike-surface:#22201D;
  --aike-surface-2:#2C2925;
  --aike-surface-3:#38342F;
  --aike-text:#EDEAE5;
  --aike-text-muted:#A6A096;
  --aike-text-faint:#706B63;
  --aike-border:#36332E;
  --aike-border-soft:#2F2C28;
  --aike-accent:#E2886A;
  --aike-accent-hover:#F0A58C;
  --aike-accent-soft:rgba(226,136,106,.18);
  --aike-accent-contrast:#181715;
  --aike-emerald:#34D399;
  --aike-emerald-bg:#064E3B;
  --aike-rose:#F87171;
  --aike-rose-bg:#450A0A;
  --aike-amber:#FBBF24;
  --aike-amber-bg:#451A03;
  --aike-cyan:#38BDF8;
  --aike-cyan-bg:#083344;
  --aike-code-bg:#14120F;
  --aike-shadow-sm:0 1px 3px rgba(0,0,0,.30);
  --aike-shadow-md:0 4px 12px rgba(0,0,0,.40);
  --aike-shadow-lg:0 12px 32px rgba(0,0,0,.50);
  --aike-shadow:none;
"""

# ------------------------------------------------- 各文件历史变量名 → 统一基线值
LEGACY = {
    "FDE": ("""
  --bg:#FAF7F2; --bg-elev:#FFFFFF; --surface-1:#FFFFFF; --surface-2:#F3EFEA; --surface-3:#EAE5DE;
  --border:#E5DFD5; --border-soft:#EFEBE4;
  --text-primary:#2D2A26; --text-secondary:#6B655E; --text-muted:#968F85;
  --accent:#D97757; --accent-soft:rgba(217,119,87,.12);
  --emerald:#10B981; --rose:#EF4444; --amber:#F59E0B; --cyan:#06B6D4;
  --code-bg:#F2ECE2; --shadow:0 1px 2px rgba(90,70,50,.06),0 8px 26px rgba(90,70,50,.10);
  --radius-sm:6px; --radius-md:10px; --radius-lg:16px;
  --sidebar-w:280px; --maxw:1180px;""",
            """
  --bg:#181715; --bg-elev:#22201D; --surface-1:#22201D; --surface-2:#2C2925; --surface-3:#38342F;
  --border:#36332E; --border-soft:#2F2C28;
  --text-primary:#EDEAE5; --text-secondary:#A6A096; --text-muted:#706B63;
  --accent:#E2886A; --accent-soft:rgba(226,136,106,.18);
  --emerald:#34D399; --rose:#F87171; --amber:#FBBF24; --cyan:#38BDF8;
  --code-bg:#14120F; --shadow:0 1px 2px rgba(0,0,0,.40),0 8px 28px rgba(0,0,0,.28);"""),

    "Uber": ("""
  --bg:#FAF7F2; --bg-soft:#F3EFEA; --card-bg:#FFFFFF; --card-hover:#FCFAF7;
  --text-primary:#2D2A26; --text-secondary:#6B655E; --text-muted:#968F85;
  --border:#E5DFD5; --border-subtle:#EFEBE4;
  --accent:#D97757; --accent-hover:#B55A3C; --accent-soft:rgba(217,119,87,.12);
  --emerald:#10B981; --emerald-soft:rgba(16,185,129,.12);
  --amber:#F59E0B; --amber-soft:rgba(245,158,11,.12);
  --rose:#EF4444; --rose-soft:rgba(239,68,68,.12);
  --cyan:#06B6D4; --cyan-soft:rgba(6,182,212,.12);
  --code-bg:#F2ECE2;
  --radius-sm:6px; --radius-md:10px; --radius-lg:16px;
  --sidebar-width:280px; --content-max-width:1180px;""",
             """
  --bg:#181715; --bg-soft:#1F1D1A; --card-bg:#22201D; --card-hover:#2C2925;
  --text-primary:#EDEAE5; --text-secondary:#A6A096; --text-muted:#706B63;
  --border:#36332E; --border-subtle:#2F2C28;
  --accent:#E2886A; --accent-hover:#F0A58C; --accent-soft:rgba(226,136,106,.18);
  --emerald:#34D399; --emerald-soft:rgba(52,211,153,.18);
  --amber:#FBBF24; --amber-soft:rgba(251,191,36,.18);
  --rose:#F87171; --rose-soft:rgba(248,113,113,.18);
  --cyan:#38BDF8; --cyan-soft:rgba(56,189,248,.18);
  --code-bg:#14120F;"""),

    "AI工作流": ("""
  --bg-canvas:#FAF7F2; --bg-card:#FFFFFF; --bg-card-subtle:#F3EFEA; --bg-card-hover:#EAE5DE;
  --border-color:#E5DFD5; --border-subtle:#EFEBE4;
  --text-primary:#2D2A26; --text-secondary:#6B655E; --text-tertiary:#968F85;
  --accent:#D97757; --accent-hover:#B55A3C; --accent-light:rgba(217,119,87,.12);
  --emerald:#10B981; --emerald-light:rgba(16,185,129,.12);
  --amber:#F59E0B; --amber-light:rgba(245,158,11,.12);
  --rose:#EF4444; --rose-light:rgba(239,68,68,.12);
  --cyan:#06B6D4; --cyan-light:rgba(6,182,212,.12);
  --font-sans:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;
  --font-serif:"Songti SC","SimSun","Newsreader",Georgia,serif;
  --font-mono:ui-monospace,"SF Mono",Menlo,Consolas,"JetBrains Mono",monospace;
  --radius-sm:6px; --radius-md:10px; --radius-lg:16px;
  --toc-width:280px; --container-max:1360px;""",
                """
  --bg-canvas:#181715; --bg-card:#22201D; --bg-card-subtle:#2C2925; --bg-card-hover:#38342F;
  --border-color:#36332E; --border-subtle:#2F2C28;
  --text-primary:#EDEAE5; --text-secondary:#A6A096; --text-tertiary:#706B63;
  --accent:#E2886A; --accent-hover:#F0A58C; --accent-light:rgba(226,136,106,.18);
  --emerald:#34D399; --emerald-light:rgba(52,211,153,.18);
  --amber:#FBBF24; --amber-light:rgba(251,191,36,.18);
  --rose:#F87171; --rose-light:rgba(248,113,113,.18);
  --cyan:#38BDF8; --cyan-light:rgba(56,189,248,.18);"""),

    "Ulike": ("""
  --bg:#FAF7F2; --panel:#FFFFFF; --panel2:#F3EFEA;
  --ink:#2D2A26; --muted:#6B655E; --faint:#968F85;
  --line:#E5DFD5;
  --accent:#D97757; --accent2:#0F766E; --blue:#06B6D4;
  --ok:#10B981; --warn:#F59E0B; --bad:#EF4444; --purple:#7C5CBF;
  --shadow:0 8px 30px rgba(90,70,50,.06); --code:#F2ECE2;""",
              """
  --bg:#181715; --panel:#22201D; --panel2:#2C2925;
  --ink:#EDEAE5; --muted:#A6A096; --faint:#706B63;
  --line:#36332E;
  --accent:#E2886A; --accent2:#55D4C8; --blue:#38BDF8;
  --ok:#34D399; --warn:#FBBF24; --bad:#F87171; --purple:#B294FF;
  --shadow:none; --code:#14120F;"""),

    "设计工程": ("""
  --bg:#FAF7F2; --bg-translucent:rgba(250,247,242,.85);
  --surface:#FFFFFF; --surface-secondary:#F3EFEA; --surface-tertiary:#EAE5DE;
  --text:#2D2A26; --text-muted:#6B655E; --text-faint:#968F85;
  --border:#E5DFD5; --border-focus:#D97757;
  --accent:#D97757; --accent-light:#F4DCD3; --accent-dark:#B55A3C;
  --emerald:#10B981; --emerald-bg:#ECFDF5;
  --rose:#EF4444; --rose-bg:#FEF2F2;
  --amber:#F59E0B; --amber-bg:#FFFBEB;
  --cyan:#06B6D4; --cyan-bg:#ECFEFF;
  --sidebar-w:280px;""",
                """
  --bg:#181715; --bg-translucent:rgba(24,23,21,.85);
  --surface:#22201D; --surface-secondary:#2C2925; --surface-tertiary:#38342F;
  --text:#EDEAE5; --text-muted:#A6A096; --text-faint:#706B63;
  --border:#36332E; --border-focus:#E2886A;
  --accent:#E2886A; --accent-light:#3D261E; --accent-dark:#F0A58C;
  --emerald:#34D399; --emerald-bg:#064E3B;
  --rose:#F87171; --rose-bg:#450A0A;
  --amber:#FBBF24; --amber-bg:#451A03;
  --cyan:#38BDF8; --cyan-bg:#083344;"""),
}

SCOPE = ":is(body,main,.content,.page,.article-section,.app-layout,.layout,.doc-hero,.wrap,.container,.content-area)"

SHARED = """
/* ------------------------------------------------------------------ 3. 统一字体栈 */
html{ -webkit-text-size-adjust:100%; }
body{
  font-family:var(--aike-font-sans);
  font-size:16px;
  line-height:1.75;
  letter-spacing:.005em;
  background-color:var(--aike-bg);
  color:var(--aike-text);
}
code,kbd,pre,samp,.mono{ font-family:var(--aike-font-mono); }

/* -------------------------------------------------------- 4. 统一字号阶梯与间距节奏 */
""" + SCOPE + """ h1{
  font-family:var(--aike-font-serif);
  font-size:clamp(30px,3.2vw,42px);
  line-height:1.24; font-weight:700; letter-spacing:.01em;
  color:var(--aike-text); margin:0 0 1.1rem;
}
""" + SCOPE + """ h2{
  font-family:var(--aike-font-serif);
  font-size:clamp(23px,2.1vw,28px);
  line-height:1.36; font-weight:700; letter-spacing:.01em;
  color:var(--aike-text); margin:2.8rem 0 1.05rem;
}
""" + SCOPE + """ h3{
  font-family:var(--aike-font-serif);
  font-size:clamp(18px,1.5vw,20px);
  line-height:1.45; font-weight:700;
  color:var(--aike-text); margin:2rem 0 .8rem;
}
""" + SCOPE + """ h4{
  font-family:var(--aike-font-sans);
  font-size:16px; line-height:1.5; font-weight:700;
  color:var(--aike-text); margin:1.5rem 0 .6rem;
}
""" + SCOPE + """ p{ margin:0 0 1.05rem; }
""" + SCOPE + """ li{ margin:.34rem 0; }
""" + SCOPE + """ a{ color:var(--aike-accent); }
""" + SCOPE + """ hr{ border:none; border-top:1px solid var(--aike-border); margin:2.4rem 0; }

/* ----------------------------------------------------------- 5. 统一栅格与容器几何 */
.sidebar,.side,.sidebar-nav,.sidebar-toc{
  width:var(--aike-sidebar-w)!important;
  flex-basis:var(--aike-sidebar-w)!important;
}
.layout,.app-layout{ max-width:var(--aike-container-max); }
.content,.page,.wrap,.container,.content-area{ max-width:var(--aike-container-max); }
section{ scroll-margin-top:24px; }

/* --------------------------------------------------------------- 6. 统一组件表面 */
""" + SCOPE + """ table{
  width:100%; border-collapse:collapse; font-size:14.5px;
  margin:1.2rem 0 1.6rem;
}
""" + SCOPE + """ th{
  background:var(--aike-surface-2); color:var(--aike-text);
  font-weight:700; text-align:left;
  border:1px solid var(--aike-border); padding:10px 14px;
  line-height:1.55;
}
""" + SCOPE + """ td{
  border:1px solid var(--aike-border); padding:10px 14px;
  line-height:1.6; vertical-align:top;
}
""" + SCOPE + """ tbody tr:nth-child(even){ background:var(--aike-surface-2); }
""" + SCOPE + """ pre{
  background:var(--aike-code-bg); color:var(--aike-text);
  border:1px solid var(--aike-border); border-radius:var(--aike-radius-md);
  padding:14px 16px; overflow-x:auto; font-size:13.5px; line-height:1.7;
  margin:1.2rem 0 1.6rem;
}
""" + SCOPE + """ code{
  background:var(--aike-code-bg); color:var(--aike-accent-hover);
  border-radius:var(--aike-radius-sm); padding:.12em .4em; font-size:.875em;
}
""" + SCOPE + """ pre code{ background:transparent; padding:0; color:inherit; font-size:1em; }
""" + SCOPE + """ blockquote{
  border-left:3px solid var(--aike-accent);
  background:var(--aike-surface-2);
  border-radius:0 var(--aike-radius-md) var(--aike-radius-md) 0;
  padding:.9rem 1.15rem; margin:1.2rem 0 1.6rem; color:var(--aike-text-muted);
}
""" + SCOPE + """ blockquote p:last-child{ margin-bottom:0; }

/* --------------------------------------------------------------- 7. 统一响应式 */
@media (max-width:1080px){
  .sidebar,.side,.sidebar-nav,.sidebar-toc{
    position:static!important; width:100%!important; flex-basis:100%!important;
    height:auto!important; max-height:none!important;
    border-right:none!important; border-bottom:1px solid var(--aike-border);
  }
  .layout,.app-layout{ grid-template-columns:minmax(0,1fr)!important; }
  .content,.page,.wrap,.container,.content-area{ padding-left:20px!important; padding-right:20px!important; }
}
@media (max-width:640px){
  body{ font-size:15px; }
  """ + SCOPE + """ table{ font-size:13.5px; }
  """ + SCOPE + """ th,""" + SCOPE + """ td{ padding:8px 10px; }
}

/* ---------------------------------------------------------------- 8. 统一打印样式 */
@media print{
  .sidebar,.side,.sidebar-nav,.sidebar-toc,.topbar,.site-header,.header-nav,
  .reading-progress,.reading-progress-bar,#read-progress,#progress,
  .theme-toggle-btn,.tbtn,.nav-actions,.aike-theme-btn{
    display:none!important;
  }
  body{ background:#FFFFFF!important; color:#000000!important; font-size:11pt; }
  .layout,.app-layout{ display:block!important; max-width:100%!important; }
  .content,.page,.wrap,.container,.content-area{
    max-width:100%!important; padding:0!important; margin:0!important;
  }
  """ + SCOPE + """ table,""" + SCOPE + """ pre,""" + SCOPE + """ blockquote{ page-break-inside:avoid; }
  """ + SCOPE + """ h1,""" + SCOPE + """ h2,""" + SCOPE + """ h3{ page-break-after:avoid; color:#000000!important; }
  a{ color:#000000!important; text-decoration:none!important; }
}
"""


def build_baseline(key):
    lgt, drk = LEGACY[key]
    return f"""
/* ==========================================================================
   AIKnowledge 统一排版基线层 v1.0 · Unified Typography & Layout Baseline
   统一维度：设计令牌 / 双主题机制 / 字号阶梯 / 栅格几何 / 组件表面 / 打印响应式
   暖羊皮纸 #FAF7F2  ·  黑曜石 #181715  ·  陶土强调色 #D97757
   ========================================================================== */

/* ---- 1. 统一设计令牌（浅色 · 暖羊皮纸） + 历史变量兼容映射 ---- */
:root{{{LIGHT}
{lgt}
}}

/* ---- 2. 统一设计令牌（深色 · 黑曜石）：data-theme / .dark / 系统偏好 三者等价 ---- */
html[data-theme="dark"],html.dark{{{DARK}
{drk}
}}
@media (prefers-color-scheme:dark){{
  html:not([data-theme="light"]):not([data-theme="dark"]):not(.dark){{{DARK}
{drk}
  }}
}}
html[data-theme="light"]{{{LIGHT}
{lgt}
}}
{SHARED}
/* =========================== 统一排版基线层结束 =========================== */
"""


def main():
    for key, path in FILES.items():
        s = open(path, encoding="utf-8").read()
        m = re.search(r"</style>", s)
        assert m, f"{key}: 未找到 </style>"
        # 幂等：若已注入则先剥离旧基线层
        s = re.sub(r"\n?/\* =+\n   AIKnowledge 统一排版基线层.*?统一排版基线层结束 =+ \*/\n?",
                   "\n", s, flags=re.S)
        m = re.search(r"</style>", s)
        block = build_baseline(key)
        s = s[:m.start()] + block + s[m.start():]
        open(path, "w", encoding="utf-8").write(s)
        print(f"[OK] {key}: 已注入统一排版基线  ({os.path.basename(path)})")


if __name__ == "__main__":
    main()
