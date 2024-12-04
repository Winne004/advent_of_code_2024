from collections import Counter
from pathlib import Path
from typing import List, Tuple, Callable

file_name = "day_2_input.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def yield_line(file_path: Path) -> Tuple[List[int], List[int]]:
    with open(file_path, "r") as f:
        for line in f:
            yield [int(x) for x in line.strip().split()]


def factory_based_on_order(line: List[int]) -> Callable[[List[int]], bool]:
    if line[0] < line[-1]:
        return ascending_handler
    else:
        return descending_handler


def ascending_handler(line: List[int]) -> bool:
    for x in range(1, len(line)):
        diff = line[x] - line[x - 1]
        if not (1 <= diff <= 3):
            return False
    return True


def descending_handler(line: List[int]) -> bool:
    for x in range(1, len(line)):
        diff = line[x - 1] - line[x]
        if not (1 <= diff <= 3):
            return False
    return True


def is_safe(line: List[int]) -> bool:
    if line[0] == line[-1]:
        return False
    handler = factory_based_on_order(line)
    return handler(line)


def main() -> None:
    # Part 1 solution
    safe_count = 0
    for line in yield_line(file_path):
        if is_safe(line):
            safe_count += 1

    print(f"Safe count: {safe_count}")


if __name__ == "__main__":
    main()
