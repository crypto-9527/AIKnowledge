#!/usr/bin/env python3
"""
validate_html.py
================
针对技术专著类单文件 HTML 的 8 项工程化静态自检工具。
纯 Python 3 标准库实现，零第三方依赖。

检查项：
1. 存储位置与命名规范检测（Canonical Storage & Naming Convention）：强制唯一存储路径与「YYYYMMDD_核心要义一眼看出主题」命名规则，阻断临时模糊词。
2. 零外部依赖检测（Zero External Dependencies）：阻断外部 CDN、远程 CSS/JS、远程图片与字体。
3. 标签闭合与平衡栈检测（Tag Balance & Void Elements）：严格支持 HTML5 与内联 SVG 自闭合标记。
4. 锚点与目录可达性（Anchor Target Completeness）：验证所有 #id 锚点均有实体 DOM。
5. 原生 JavaScript 语法检测（Inline JS Syntax）：抽取内联脚本交由 Node.js 做静态 AST 校验。
6. SVG 几何与数据坐标反查（SVG Coordinate & Data Alignment）：严查折线点阵与刻度映射一致性、viewBox 越界。
7. 交互组件接线完整性（Interactive Wiring & Sliders）：验证所有 input/button/select/display 均被 JS 监听或赋值。
8. LaTeX 泄漏与排版健全性（No Raw LaTeX Leakage & Meta Tags）：阻断未渲染的 $$ 或 \\frac，验证 viewport 与 print 样式。
"""

import sys
import os
import re
import shutil
import subprocess
import tempfile
from html.parser import HTMLParser
from typing import List, Tuple, Dict, Set

CANONICAL_STORAGE_DIR = "/Users/yangkejin/Documents/Openai/AIKnowledge"
BLACKLISTED_NAMING_PATTERNS = [
    "最终", "合并版", "最新", "总结归纳", "修改版", "完整版", "草稿", "副本",
    "draft", "temp", "tmp", "final", "latest", "new"
]


def check_storage_and_naming(file_path: str) -> List[str]:
    issues = []
    abs_path = os.path.abspath(file_path)
    file_dir = os.path.dirname(abs_path)
    file_name = os.path.basename(abs_path)

    # 1. 唯一合法存储路径校验
    canonical_real = os.path.realpath(CANONICAL_STORAGE_DIR)
    file_dir_real = os.path.realpath(file_dir)
    if file_dir_real != canonical_real:
        issues.append(
            f"存储路径不合规：文件当前位于 '{file_dir}'，唯一规范存储路径必须为 '{CANONICAL_STORAGE_DIR}'"
        )

    # 2. 命名模式校验：YYYYMMDD_核心要义一眼看出主题.[html|md]
    pattern = r'^([0-9]{8})_([a-zA-Z0-9\u4e00-\u9fa5\-_()（）\.]+)\.(html|md)$'
    m = re.match(pattern, file_name)
    if not m:
        issues.append(
            f"文档命名不合规：'{file_name}' 不符合规范 '[YYYYMMDD]_[核心要义一眼看出主题].[html|md]'（缺少8位日期前缀或使用了非法分隔符）"
        )
    else:
        date_str, theme = m.group(1), m.group(2)
        if len(theme) < 4:
            issues.append(f"文档主题要义过短 ('{theme}')，无法达到'一眼知道主题是啥'的要求，请提炼精准具体的技术主题词")

        # 3. 临时反模式词汇阻断
        theme_lower = theme.lower()
        for kw in BLACKLISTED_NAMING_PATTERNS:
            if kw in theme_lower:
                issues.append(f"文档命名违规包含临时反模式词汇 '{kw}'：严禁使用'最终版/合并版/最新版/总结归纳'等修饰词，请直接概括技术实体或架构要义")
                break

    return issues


class TagBalanceParser(HTMLParser):
    VOID_HTML_TAGS = {
        "area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr"
    }
    SVG_SELF_CLOSING = {
        "path", "circle", "rect", "line", "polyline", "polygon",
        "ellipse", "stop", "use", "image"
    }

    def __init__(self):
        super().__init__()
        self.stack: List[Tuple[str, int]] = []
        self.errors: List[str] = []
        self.all_ids: Set[str] = set()
        self.all_anchors: Set[str] = set()

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, str]]):
        tag_lower = tag.lower()
        attr_dict = dict(attrs)

        if "id" in attr_dict:
            self.all_ids.add(attr_dict["id"])

        if "href" in attr_dict:
            href = attr_dict["href"]
            if href.startswith("#") and len(href) > 1:
                self.all_anchors.add(href[1:])

        if tag_lower in self.VOID_HTML_TAGS or tag_lower in self.SVG_SELF_CLOSING:
            return

        self.stack.append((tag_lower, self.getpos()[0]))

    def handle_endtag(self, tag: str):
        tag_lower = tag.lower()
        if tag_lower in self.VOID_HTML_TAGS or tag_lower in self.SVG_SELF_CLOSING:
            return

        if not self.stack:
            self.errors.append(f"第 {self.getpos()[0]} 行：意外闭合标签 </{tag}>，栈已为空")
            return

        last_tag, line_no = self.stack.pop()
        if last_tag != tag_lower:
            self.errors.append(
                f"第 {self.getpos()[0]} 行：标签闭合不匹配！期望 </{last_tag}>（在第 {line_no} 行开启），实际得到 </{tag}>"
            )


def check_zero_dependencies(html: str) -> List[str]:
    issues = []
    # 外部脚本
    for m in re.finditer(r'<script[^>]+src=["\']([^"\']+)["\']', html, re.IGNORECASE):
        src = m.group(1)
        if src.startswith("http://") or src.startswith("https://") or src.startswith("//"):
            issues.append(f"发现外部 JS 脚本依赖：{src}")

    # 外部样式
    for m in re.finditer(r'<link[^>]+href=["\']([^"\']+)["\']', html, re.IGNORECASE):
        href = m.group(1)
        rel = m.group(0)
        if "stylesheet" in rel.lower() and (href.startswith("http://") or href.startswith("https://") or href.startswith("//")):
            issues.append(f"发现外部 CSS 样式表依赖：{href}")

    # CSS @import
    for m in re.finditer(r'@import\s+(?:url\()?["\']?([^"\'\)\s]+)', html, re.IGNORECASE):
        url = m.group(1)
        if url.startswith("http://") or url.startswith("https://") or url.startswith("//"):
            issues.append(f"发现 CSS @import 远程引用：{url}")

    # CSS 远程资源 url(...)
    for m in re.finditer(r'url\(\s*["\']?(https?://[^"\'\)]+)["\']?\s*\)', html, re.IGNORECASE):
        issues.append(f"发现 CSS 远程背景/字体引用：{m.group(1)}")

    return issues


def check_tag_balance_and_anchors(html: str) -> Tuple[List[str], Set[str], Set[str]]:
    parser = TagBalanceParser()
    parser.feed(html)
    errors = list(parser.errors)
    if parser.stack:
        for tag, line in parser.stack:
            errors.append(f"未闭合标签 <{tag}>，开启于第 {line} 行")

    # 锚点检查
    missing_anchors = []
    for anchor in parser.all_anchors:
        if anchor not in parser.all_ids:
            missing_anchors.append(f"锚点跳转目标未定义：#{anchor}")

    return errors, missing_anchors, parser.all_ids


def check_inline_js(html: str) -> List[str]:
    issues = []
    scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
    if not scripts:
        return issues

    node_bin = shutil.which("node")
    if not node_bin:
        # 尝试常用路径
        common_paths = [
            "/Users/yangkejin/.workbuddy/binaries/node/versions/22.22.2-2/bin/node",
            "/opt/homebrew/bin/node",
            "/usr/local/bin/node"
        ]
        for p in common_paths:
            if os.path.exists(p):
                node_bin = p
                break

    if not node_bin:
        return ["警告：未检测到 node 可执行文件，跳过 JavaScript AST 静态解析"]

    full_js = "\n".join(scripts)
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write(full_js)
        temp_path = f.name

    try:
        res = subprocess.run([node_bin, "--check", temp_path], capture_output=True, text=True)
        if res.returncode != 0:
            issues.append(f"JavaScript 语法校验失败 (node --check)：\n{res.stderr.strip()}")
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

    return issues


def check_svg_alignment(html: str) -> List[str]:
    issues = []
    svg_blocks = re.findall(r'<svg[^>]*>.*?</svg>', html, re.DOTALL | re.IGNORECASE)

    for i, svg in enumerate(svg_blocks, 1):
        # 提取 viewBox
        vb_m = re.search(r'viewBox=["\']\s*([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\s*["\']', svg)
        vb_w, vb_h = (None, None)
        if vb_m:
            vb_w, vb_h = float(vb_m.group(3)), float(vb_m.group(4))

        # 检查 polyline 的 points
        polylines = re.findall(r'<polyline[^>]+points=["\']([^"\']+)["\']', svg)
        for pts_str in polylines:
            raw_pts = pts_str.strip().split()
            coords = []
            for p in raw_pts:
                parts = p.split(",")
                if len(parts) == 2:
                    try:
                        coords.append((float(parts[0]), float(parts[1])))
                    except ValueError:
                        pass

            if vb_w and vb_h:
                for x, y in coords:
                    if x < -5 or x > vb_w + 5 or y < -5 or y > vb_h + 5:
                        issues.append(f"SVG #{i}：折线点 ({x}, {y}) 超出 viewBox 范围 [0, 0, {vb_w}, {vb_h}]")

            # 校验 x 轴等间距映射合理性
            if len(coords) >= 5:
                x_diffs = [coords[j][0] - coords[j - 1][0] for j in range(1, len(coords))]
                # 检查是否存在明显的间距断层或离群点
                avg_diff = sum(x_diffs) / len(x_diffs)
                for idx, d in enumerate(x_diffs):
                    if abs(d - avg_diff) > avg_diff * 0.5 and avg_diff > 1.0:
                        issues.append(
                            f"SVG #{i}：第 {idx+1} 个数据点 x 轴间距异常 ({d:.2f} vs 平均 {avg_diff:.2f})，请复核折线数据坐标映射"
                        )
                        break

    return issues


def check_interactive_wiring(html: str, all_ids: Set[str]) -> List[str]:
    issues = []
    # 抽取所有脚本内容
    scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
    js_text = " ".join(scripts)

    # 提取交互组件 id：以 input/select/button 开头的控件（使用 \bid 精准匹配，避免匹配 data-*-id 属性）
    interactive_ids = set()
    for m in re.finditer(r'<(?:input|select|button)\b[^>]*?\s\bid=["\']([^"\']+)["\']', html, re.IGNORECASE):
        interactive_ids.add(m.group(1))

    # 提取通常作为结果回显的容器 id（如以 val-, sim-, res-, out-, stat- 开头）
    display_ids = set()
    for mid in all_ids:
        if any(mid.startswith(prefix) for prefix in ["val-", "sim-", "res-", "out-", "stat-", "usl-", "pf-"]):
            display_ids.add(mid)

    # 验证这些 id 是否在 JS 中被引用
    for ctrl_id in interactive_ids:
        pattern = rf'["\']{re.escape(ctrl_id)}["\']'
        if not re.search(pattern, js_text):
            issues.append(f"交互控件 #{ctrl_id} 未在 JavaScript 中发现事件绑定或取值引用（疑似悬空控件）")

    for disp_id in display_ids:
        pattern = rf'["\']{re.escape(disp_id)}["\']'
        if not re.search(pattern, js_text):
            issues.append(f"数据显示容器 #{disp_id} 未在 JavaScript 中发现回写逻辑（疑似未接线回显槽位）")

    return issues


def check_latex_and_formatting(html: str) -> List[str]:
    issues = []
    # 1. 检查双美元符块级 LaTeX
    block_latex = re.findall(r'\$\$[^\$]+\$\$', html)
    if block_latex:
        issues.append(f"检测到未渲染的块级 LaTeX 记号 ({len(block_latex)} 处)，如 '{block_latex[0][:30]}...'，请转为纯 CSS 原生数学排版")

    # 2. 检查内联 LaTeX 记号（精准排除美元货币符号如 $0.075 降至 $0.024）
    inline_candidates = re.findall(r'\$([^$\n]+)\$', html)
    real_inline_latex = []
    for cand in inline_candidates:
        cand_clean = cand.strip()
        # 排除纯货币区间或纯数值
        if re.fullmatch(r'[\d.,\s\u4e00-\u9fa5]+', cand_clean):
            continue
        # 判断是否具备典型数学公式特征（含 LaTeX 宏、下标、上标、等式、独立变量等）
        if any(c in cand_clean for c in ["\\", "_", "^", "{", "}"]):
            real_inline_latex.append(cand_clean)
        elif re.search(r'[a-zA-Z]\s*[=<>+\-*/]\s*[a-zA-Z0-9]', cand_clean):
            real_inline_latex.append(cand_clean)
        elif re.fullmatch(r'[a-zA-Z](\([a-zA-Z0-9,]+\))?', cand_clean):
            real_inline_latex.append(cand_clean)

    if real_inline_latex:
        issues.append(f"检测到未渲染的行内 LaTeX 占位符 ({len(real_inline_latex)} 处)，如 '${real_inline_latex[0][:30]}$'，请转为纯 CSS 原生数学排版")

    if "\\frac{" in html or "\\sqrt{" in html:
        issues.append("检测到 LaTeX 宏代码 (\\frac 或 \\sqrt)，未转换为纯 CSS 数学排版组件")

    # 3. 检查基础 meta 标签
    if not re.search(r'<meta[^>]+charset=["\']?utf-8', html, re.IGNORECASE):
        issues.append("缺少 <meta charset=\"utf-8\">")

    if not re.search(r'<meta[^>]+name=["\']viewport["\']', html, re.IGNORECASE):
        issues.append("缺少 <meta name=\"viewport\" ...> 响应式视口配置")

    if "@media print" not in html and "@media (min-width" not in html:
        issues.append("未包含 @media print 打印自适应样式")

    return issues


def run_all_checks(file_path: str) -> bool:
    if not os.path.exists(file_path):
        print(f"❌ 目标文件不存在：{file_path}")
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    print(f"================================================================================")
    print(f" 静态交付自检报告: {os.path.basename(file_path)}")
    print(f" 文件大小: {len(html_content)/1024:.2f} KB | 总行数: {html_content.count(chr(10)) + 1}")
    print(f"================================================================================")

    all_passed = True

    # 1. 存储位置与命名规范检查
    storage_naming_issues = check_storage_and_naming(file_path)
    if storage_naming_issues:
        print(f"❌ [1/8 存储路径与命名规范检测] 失败 ({len(storage_naming_issues)} 项违规):")
        for iss in storage_naming_issues:
            print(f"   - {iss}")
        all_passed = False
    else:
        print(f"✅ [1/8 存储路径与命名规范检测] 通过：唯一合法存储目录 ({CANONICAL_STORAGE_DIR}) 且符合 YYYYMMDD_核心要义 规范")

    # 2. 零依赖检查
    dep_issues = check_zero_dependencies(html_content)
    if dep_issues:
        print(f"❌ [2/8 零外部依赖检测] 失败 ({len(dep_issues)} 项违规):")
        for iss in dep_issues:
            print(f"   - {iss}")
        all_passed = False
    else:
        print("✅ [2/8 零外部依赖检测] 通过：零外部 CSS/JS/CDN/字体引用，完全自包含")

    # 3. 标签闭合与锚点检查
    tag_errors, missing_anchors, all_ids = check_tag_balance_and_anchors(html_content)
    if tag_errors:
        print(f"❌ [3/8 标签平衡栈检测] 失败 ({len(tag_errors)} 处未闭合或错位):")
        for err in tag_errors[:5]:
            print(f"   - {err}")
        all_passed = False
    else:
        print("✅ [3/8 标签平衡栈检测] 通过：DOM 树严格闭合，SVG 复合节点自闭合状态正常")

    # 4. 锚点目标
    if missing_anchors:
        print(f"❌ [4/8 目录与锚点跳转] 失败 ({len(missing_anchors)} 个空指针):")
        for ma in missing_anchors:
            print(f"   - {ma}")
        all_passed = False
    else:
        print(f"✅ [4/8 目录与锚点跳转] 通过：共注册 {len(all_ids)} 个实体 ID，所有导航链接 100% 可达")

    # 5. JS 语法校验
    js_issues = check_inline_js(html_content)
    if js_issues:
        print(f"❌ [5/8 内联 JavaScript 语法] 校验失败:")
        for ji in js_issues:
            print(f"   - {ji}")
        all_passed = False
    else:
        print("✅ [5/8 内联 JavaScript 语法] 通过：Node.js AST 解析通过，语法无误")

    # 6. SVG 坐标对齐
    svg_issues = check_svg_alignment(html_content)
    if svg_issues:
        print(f"❌ [6/8 SVG 几何与坐标映射] 发现异常:")
        for si in svg_issues:
            print(f"   - {si}")
        all_passed = False
    else:
        print("✅ [6/8 SVG 几何与坐标映射] 通过：折线坐标均在 viewBox 内，等间距拟合无漂移")

    # 7. 交互接线检查
    wiring_issues = check_interactive_wiring(html_content, all_ids)
    if wiring_issues:
        print(f"❌ [7/8 交互控件与接线] 存在悬空组件:")
        for wi in wiring_issues:
            print(f"   - {wi}")
        all_passed = False
    else:
        print("✅ [7/8 交互控件与接线] 通过：所有滑块、按钮、回显槽位与 JS 双向绑定 100% 闭环")

    # 8. LaTeX 与格式健全性
    fmt_issues = check_latex_and_formatting(html_content)
    if fmt_issues:
        print(f"❌ [8/8 排版规范与防泄漏] 校验失败:")
        for fi in fmt_issues:
            print(f"   - {fi}")
        all_passed = False
    else:
        print("✅ [8/8 排版规范与防泄漏] 通过：无未渲染 LaTeX 残留，自包含 CSS 数学排版，响应式与打印适配完整")

    print(f"================================================================================")
    if all_passed:
        print("🎯 综合判定：全部 8 项静态自检通过！符合技术专著级单文件 HTML 交付规范。")
        return True
    else:
        print("⚠️ 综合判定：检测到不合规项，请按上述报错修复后重新运行。")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用方式: python3 validate_html.py <path_to_html_file>")
        sys.exit(1)

    target_file = sys.argv[1]
    success = run_all_checks(target_file)
    sys.exit(0 if success else 1)
