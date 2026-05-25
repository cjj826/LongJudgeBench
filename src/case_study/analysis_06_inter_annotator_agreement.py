"""
Inter-Annotator Agreement (MA dataset, insights dimension).

计算: 固定同一个 query-answer pair, 8 人 label 两两配对,
排除含 tie 的 pair, 算 acc (同一label分子+1/分母+1, 不同label分子+0/分母+1),
最后所有 pair 全局平均.

Rating: A2(0) < A1(1) < tie(2) < B1(3) < B2(4)
"""
import sys
from pathlib import Path
from itertools import combinations

import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR))

import json

ANNOTATION_FILE = BASE_DIR / "data" / "MA" / "human_annotation_data.json"
RATING_MAP = {"A2": 0, "A1": 1, "tie": 2, "B1": 3, "B2": 4}


def load_tasks(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    tasks = []
    for task in data["per_task_annotations"].values():
        if task.get("dimension_id") != "insights":
            continue
        anns = task.get("human_annotations", {})
        ratings = np.array([a["rating_num"] for a in anns.values()])
        if len(ratings) == 8:
            tasks.append(ratings)
    return tasks


def compute_acc(tasks, mode="5class"):
    """
    遍历所有 task, 每个 task 内 8 人两两配对.
    排除含 tie 的 pair, 统计:
      - numerator:  两人 label 完全一致的 pair 数
      - denominator: 有效 pair 数 (不含 tie)
    最后全局 numerator / denominator 即为 acc.

    mode:
      "5class" — 原始 5 级 label: A2/A1/tie/B1/B2
      "3class" — 映射为 3 级: A2/A1→A, tie→T, B1/B2→B
    """
    total_num = 0
    total_den = 0

    for t in tasks:
        for i, j in combinations(range(8), 2):
            ri, rj = t[i], t[j]

            if mode == "5class":
                # 排除含 tie 的 pair
                if ri == 2 or rj == 2:
                    continue
                total_den += 1
                if ri == rj:
                    total_num += 1

            elif mode == "3class":
                # 映射: A2/A1→0, tie→1, B1/B2→2
                ti = 0 if ri <= 1 else (1 if ri == 2 else 2)
                tj = 0 if rj <= 1 else (1 if rj == 2 else 2)
                # 排除含 tie 的 pair
                if ti == 1 or tj == 1:
                    continue
                total_den += 1
                if ti == tj:
                    total_num += 1

    return total_num / total_den if total_den > 0 else 0, total_num, total_den


def main():
    tasks = load_tasks(ANNOTATION_FILE)
    print(f"Insights tasks: {len(tasks)}")
    print(f"总 pair 数 (含tie): {len(tasks) * 28}\n")

    for label, mode in [("五类 Label (A2/A1/tie/B1/B2)", "5class"),
                        ("三类 Label (A/T/B, 映射后)", "3class")]:
        acc, num, den = compute_acc(tasks, mode=mode)
        print(f"=== {label} ===")
        print(f"  一致 pair: {num}")
        print(f"  有效 pair (不含tie): {den}")
        print(f"  ACC (全局): {acc*100:.2f}%")
        print()


if __name__ == "__main__":
    main()
