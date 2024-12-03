from collections import Counter
from pathlib import Path
from typing import List, Tuple

file_name = "day_2_input.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def yeild_line(file_path: Path) -> Tuple[List[int], List[int]]:
    with open(file_path, "r") as f:
        for line in f:
            yield [int(x) for x in line.strip().split()]


def is_safe(line: List) -> bool:
    if line[0] == line[-1]:
        return False
    if line[0] < line[-1]:
        for x in range(1, len(line)):
            if line[x] <= line[x - 1] or line[x] - line[x - 1] > 3:
                return False

    else:
        for x in range(1, len(line)):
            if line[x - 1] <= line[x] or line[-1] - line[x] > 3:
                return False
    return True


def main() -> None:
    # Part 1 solution
    safe_count = 0
    for line in yeild_line(file_path):
        if is_safe(line):
            safe_count += 1

    print(f"Safe count: {safe_count}")


if __name__ == "__main__":
    main()
