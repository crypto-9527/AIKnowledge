#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""核验 JS 中 getElementById / querySelector('#id') 引用的 DOM 节点是否真实存在。

用法：
  1. 显式指定文件：python3 check_js_dom_bindings.py <file1.html> [file2.html ...]
  2. 无参数时：自动扫描唯一存储目录下全部 YYYYMMDD_*.html（存在才检查，缺失自动跳过）
"""
import re, os, sys, glob

D = "/Users/yangkejin/Documents/Openai/AIKnowledge"
FALLBACK_FILES = {
    "FDE":      f"{D}/20260903_Anthropic前沿部署工程师FDE面试指南.html",
    "Uber":     f"{D}/20260903_Uber超大规模软件工厂落地指南.html",
    "AI工作流":  f"{D}/20260904_AI编程工作流与上下文工程体系指南.html",
    "设计工程":  f"{D}/20260907_设计工程审美体系与Agent界面审查架构白皮书.html",
    "Meta":     f"{D}/20260907_Meta组织级第二大脑构建与专家经验闭环.html",
}


def resolve_targets(argv):
    """命令行参数优先；无参数则扫描存储目录，目录为空时回落到历史清单（仅保留存在的文件）。"""
    if len(argv) > 1:
        return [(os.path.basename(p), p) for p in argv[1:]]
    pattern = os.path.join(D, "[0-9]" * 8 + "_*.html")
    found = sorted(glob.glob(pattern))
    if found:
        return [(os.path.basename(p), p) for p in found]
    return [(k, p) for k, p in FALLBACK_FILES.items() if os.path.exists(p)]


def main():
    targets = resolve_targets(sys.argv)
    if not targets:
        print("未找到任何待检查文件（目录为空且历史清单文件不存在）")
        sys.exit(1)

    had_missing = False
    print(f"{'文档':<10} {'JS引用id':>8} {'缺失':>6}  断裂明细")
    print("-" * 96)
    for key, path in targets:
        if not os.path.exists(path):
            print(f"{key:<10} {'-':>8} {'-':>6}  SKIP（文件不存在）")
            continue
        s = open(path, encoding="utf-8").read()
        scripts = re.findall(r"<script[^>]*>(.*?)</script>", s, re.S)
        js = "\n".join(scripts)
        html_ids = set(re.findall(r'\sid="([^"]+)"', s))

        refs = set(re.findall(r'getElementById\(\s*"([^"]+)"\s*\)', js))
        refs |= set(re.findall(r"getElementById\(\s*'([^']+)'\s*\)", js))
        refs |= set(re.findall(r'querySelector\(\s*"#([^"]+)"\s*\)', js))
        refs |= set(re.findall(r'byId\(\s*"([^"]+)"\s*\)', js))
        refs |= set(re.findall(r"byId\(\s*'([^']+)'\s*\)", js))
        # 排除 JS 内部动态拼接/变量名
        refs = {r for r in refs if re.fullmatch(r"[A-Za-z0-9_\-]+", r)}

        missing = sorted(refs - html_ids)
        flag = "!!" if missing else "OK"
        if missing:
            had_missing = True
        print(f"{key:<10} {len(refs):>8} {len(missing):>6}  {flag}")
        for x in missing[:14]:
            print(f"             - #{x}")
        if len(missing) > 14:
            print(f"             - ...({len(missing) - 14} more)")

    sys.exit(1 if had_missing else 0)


if __name__ == "__main__":
    main()
