from pathlib import Path
from typing import Callable

file_name = "day_12_test.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def read_file_content(file_path: Path) -> str:
    return file_path.read_text(encoding="utf-8")


directions = [
    lambda row, col: (row, col + 1),  # right
    lambda row, col: (row, col - 1),  # left
    lambda row, col: (row - 1, col),  # up
    lambda row, col: (row + 1, col),  # down
    lambda row, col: (row - 1, col + 1),  # up-right
    lambda row, col: (row - 1, col - 1),  # up-left
    lambda row, col: (row + 1, col + 1),  # down-right
    lambda row, col: (row + 1, col - 1),  # down-left
]


def in_bounds(x, y, grid) -> bool:
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def find_area(grid: list[str], x: int, y: int, seen: set, value: str) -> int:
    res = 0

    if not in_bounds(x, y, grid):
        return 0

    if grid[y][x] != value:
        return 0

    if (x, y) not in seen:
        seen.add((x, y))
        res += 1
    else:
        return 0

    for direction in directions:
        x_offset, y_offset = direction(x, y)
        res += find_area(grid, x_offset, y_offset, seen, value)
    return res


def main() -> None:
    flower_bed = read_file_content(file_path).splitlines()
    seen = set()
    res = 0
    for y, row in enumerate(flower_bed):
        for x, v in enumerate(row):
            if (x, y) not in seen:
                print(f"{v}: {find_area(flower_bed, x, y, seen, v)}")
    print(res)


if __name__ == "__main__":
    main()
