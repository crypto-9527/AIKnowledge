#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync_skill.py —— tech-digest-to-html 三处副本的一致性同步器（纯标准库，零依赖）

作用域分层（三者作用域不同，缺一不可）：
  [SOURCE]  AIKnowledge/skills/tech-digest-to-html
            可见、纳入版本库、可评审 —— 单一真值源 (Single Source of Truth)
  [PROJECT] AIKnowledge/.workbuddy/skills/tech-digest-to-html
            项目级运行时 —— 仅在本工作区生效，可覆写全局同名 Skill
  [GLOBAL]  ~/.workbuddy/skills/tech-digest-to-html
            全局运行时 —— 在所有项目生效

用法：
  python3 scripts/sync_skill.py --check   # 仅报告三处差异（默认，只读、安全）
  python3 scripts/sync_skill.py --apply   # 以 SOURCE 为准，同步到 PROJECT 与 GLOBAL（先自动备份）
"""
import argparse
import hashlib
import os
import shutil
import sys
import time
from pathlib import Path

SKILL_NAME = "tech-digest-to-html"


def _here() -> Path:
    return Path(__file__).resolve().parent          # <SRC>/scripts


def _repo_root(start: Path) -> Path:
    """自下而上定位仓库根：首个同时具备 .git 或 .workbuddy 的祖先目录。
    不假设 SOURCE 位于 <root>/skills 还是 <root>/.workbuddy/skills，避免上溯级数写死。"""
    for p in [start] + list(start.parents):
        if (p / ".git").is_dir() or (p / ".workbuddy").is_dir():
            return p
    return start.parent.parent


def resolve_paths():
    src = _here().parent                            # [SOURCE]  <root>/skills/<name>
    aik = _repo_root(src)                           # 仓库根（AIKnowledge）
    project = aik / ".workbuddy" / "skills" / SKILL_NAME
    glob = Path.home() / ".workbuddy" / "skills" / SKILL_NAME
    return src, project, glob


def snapshot(root: Path):
    """返回 {相对路径: sha256}；目录不存在返回 None。"""
    if not root.is_dir():
        return None
    out = {}
    for p in sorted(root.rglob("*")):
        if p.is_file():
            out[str(p.relative_to(root))] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def diff(a: dict, b: dict):
    """返回 (仅在 a, 仅在 b, 内容不同)"""
    if a is None or b is None:
        return [], [], []
    only_a = sorted(set(a) - set(b))
    only_b = sorted(set(b) - set(a))
    changed = sorted(k for k in set(a) & set(b) if a[k] != b[k])
    return only_a, only_b, changed


def report(label: str, target: Path, src_snap: dict):
    tgt_snap = snapshot(target)
    print(f"\n[{label}] {target}")
    if tgt_snap is None:
        print("   状态：不存在（需创建）")
        return False
    oa, ob, ch = diff(src_snap, tgt_snap)
    if not (oa or ob or ch):
        print(f"   状态：一致（{len(tgt_snap)} 个文件）")
        return True
    print(f"   状态：漂移（{len(tgt_snap)} 个文件）")
    for f in oa:
        print(f"     + 仅 SOURCE 有：{f}")
    for f in ob:
        print(f"     - 仅目标有：{f}")
    for f in ch:
        print(f"     ~ 内容不同：{f}")
    return False


def apply_to(label: str, target: Path):
    src = _here().parent
    if target.is_dir():
        bak = target.parent / f"{target.name}.bak_{time.strftime('%Y%m%d_%H%M%S')}"
        shutil.move(str(target), str(bak))
        print(f"[{label}] 已备份旧副本 -> {bak}")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(str(src), str(target))
    n = len(list(target.rglob("*")))
    print(f"[{label}] 已同步 -> {target}（{n} 个条目）")
    # 保持脚本可执行位
    for f in (target / "scripts").glob("*.py"):
        f.chmod(0o755)


def main():
    ap = argparse.ArgumentParser(description="tech-digest-to-html 三副本一致性同步器")
    ap.add_argument("--apply", action="store_true", help="以 SOURCE 为准执行同步（默认仅检查）")
    ap.add_argument("--check", action="store_true", help="仅检查三处差异（默认行为，显式写出更易读）")
    args = ap.parse_args()

    src, project, glob = resolve_paths()
    print(f"单一真值源 (SOURCE): {src}")
    src_snap = snapshot(src)
    print(f"  {len(src_snap)} 个文件")

    ok_p = report("PROJECT 项目级运行时", project, src_snap)
    ok_g = report("GLOBAL  全局运行时", glob, src_snap)

    if not args.apply:
        print("\n（只读检查模式。如需同步请追加 --apply）")
        sys.exit(0 if (ok_p and ok_g) else 2)

    if not ok_p:
        apply_to("PROJECT", project)
    if not ok_g:
        apply_to("GLOBAL", glob)
    print("\n同步完成。建议再跑一次 --check 复核。")


if __name__ == "__main__":
    main()
