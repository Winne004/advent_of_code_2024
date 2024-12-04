from collections import Counter
from pathlib import Path
from typing import Generator, List, Tuple, Callable

file_name = "day_2_input.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def yield_line(file_path: Path) -> Generator[List[int], None, None]:
    with open(file_path, "r") as f:
        for line in f:
            yield [int(x) for x in line.strip().split()]


def factory_based_on_order(line: List[int]) -> Callable[[List[int]], bool]:
    return ascending_handler if line[0] < line[-1] else descending_handler


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


def is_safe_pt2(line: List[int]) -> bool:
    for x in range(0, len(line)):
        tmp_line = line[:x] + line[x + 1 :]
        handler = factory_based_on_order(line)
        if handler(tmp_line):
            return True
    return False


def main() -> None:
    # Part 1 solution
    safe_count = 0
    for line in yield_line(file_path):
        if is_safe(line):
            safe_count += 1

    print(f"Safe count: {safe_count}")

    # Part 2 solution
    safe_count = 0
    for line in yield_line(file_path):
        if is_safe_pt2(line):
            safe_count += 1
    print(f"Safe count Pt. 2: {safe_count}")


if __name__ == "__main__":
    main()
