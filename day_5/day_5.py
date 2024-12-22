from collections import defaultdict
from itertools import permutations
from pathlib import Path
from typing import Dict, List, Set, Tuple

file_name = "day_5_input.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def read_file_to_lists(file_path: Path) -> Tuple[Dict[str, Set[str]], List[List[str]]]:
    ordering_rules = defaultdict(set)
    reverse_ordering_rules = defaultdict(set)
    updates = []
    with open(file_path, "r") as f:
        for line in f:
            if "|" in line:
                parent, child = line.strip().split("|")
                ordering_rules[parent.strip()].add(child.strip())
                reverse_ordering_rules[child.strip()].add(parent.strip())
            elif "," in line:
                updates.append([x.strip() for x in line.strip().split(",")])
    return ordering_rules, updates, reverse_ordering_rules


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


def main():
    read_file_to_lists(file_path)
    pt_1_res = 0
    pt_2_res = 0
    ordering_rules, updates, reversed_ordering_rules = read_file_to_lists(file_path)
    for i, update in enumerate(updates):
        if is_right_order(ordering_rules, update):
            pt_1_res += find_middle(update)

    print(pt_1_res)
    print(pt_2_res)


if __name__ == "__main__":
    main()
