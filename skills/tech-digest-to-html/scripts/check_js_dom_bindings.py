#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""核验 JS 中 getElementById / querySelector('#id') 引用的 DOM 节点是否真实存在。"""
import re, os

D = "/Users/yangkejin/Documents/Openai/AIKnowledge"
FILES = {
    "FDE":      f"{D}/20260903_Anthropic前沿部署工程师FDE面试指南.html",
    "Uber":     f"{D}/20260903_Uber超大规模软件工厂落地指南.html",
    "AI工作流":  f"{D}/20260904_AI编程工作流与上下文工程体系指南.html",
    "Ulike":    f"{D}/20260904_Ulike-Agent经营分析统一优化迭代方案.html",
    "设计工程":  f"{D}/20260907_设计工程审美体系与Agent界面审查架构白皮书.html",
}

print(f"{'文档':<10} {'JS引用id':>8} {'缺失':>6}  断裂明细")
print("-" * 96)
for key, path in FILES.items():
    s = open(path, encoding="utf-8").read()
    m = re.search(r"<script[^>]*>(.*?)</script>", s, re.S)
    js = m.group(1) if m else ""
    html_ids = set(re.findall(r'\sid="([^"]+)"', s))

    refs = set(re.findall(r'getElementById\(\s*"([^"]+)"\s*\)', js))
    refs |= set(re.findall(r'getElementById\(\s*\'([^\']+)\'\s*\)', js))
    refs |= set(re.findall(r'querySelector\(\s*"#([^"]+)"\s*\)', js))
    # 排除 JS 内部动态拼接/变量名
    refs = {r for r in refs if re.fullmatch(r"[A-Za-z0-9_\-]+", r)}

    missing = sorted(refs - html_ids)
    flag = "!!" if missing else "OK"
    print(f"{key:<10} {len(refs):>8} {len(missing):>6}  {flag}")
    for x in missing[:14]:
        print(f"             - #{x}")
    if len(missing) > 14:
        print(f"             - ...({len(missing) - 14} more)")
