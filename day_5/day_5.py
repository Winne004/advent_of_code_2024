from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple

file_name = "day_5_input.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def read_file_to_lists(file_path: Path) -> Tuple[Dict[str, Set[str]], List[List[str]]]:
    ordering_rules = defaultdict(set)
    updates = []
    with open(file_path, "r") as f:
        for line in f:
            if "|" in line:
                parent, child = line.strip().split("|")
                ordering_rules[parent.strip()].add(child.strip())
            elif "," in line:
                updates.append([x.strip() for x in line.strip().split(",")])
    return ordering_rules, updates


def is_right_order(ordering_rules: dict, update: List[str]) -> bool:
    seen = set()
    for page in update:
        page_to_be_printed_before = ordering_rules[page]
        if any(page in seen for page in page_to_be_printed_before):
            return False
        seen.add(page)
    return True


def find_middle(update: List[str]) -> int:
    return int(update[len(update) // 2])


def bubble(arr: List[str], item):
    for i in range(len(arr) + 1):
        yield arr[:i] + [item] + arr[i:]


def pt_2(arr: List[str], ordering_rules: dict) -> bool:
    res = []
    for x in arr:
        for match in bubble(res, x):
            if is_right_order(ordering_rules, match):
                res = match
                break
    return res


def main():
    for x in bubble(["a", "b", "c"], "d"):
        print(x)

    read_file_to_lists(file_path)
    pt_1_res = 0
    pt_2_res = 0
    ordering_rules, updates = read_file_to_lists(file_path)
    for i, update in enumerate(updates):
        if is_right_order(ordering_rules, update):
            pt_1_res += find_middle(update)
        else:
            if rearranged := pt_2(update, ordering_rules):
                pt_2_res += find_middle(rearranged)
        print(f"Progress: {i}/{len(updates)}")

    print(pt_1_res)
    print(pt_2_res)


if __name__ == "__main__":
    main()
