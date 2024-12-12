from pathlib import Path
from collections import Counter
from typing import Callable

file_name = "day_10_input.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def read_file_content(file_path: Path) -> str:
    return file_path.read_text(encoding="utf-8")


directions = [
    lambda x, y: (x, y + 1),  # Down
    lambda x, y: (x, y - 1),  # Up
    lambda x, y: (x - 1, y),  # Left
    lambda x, y: (x + 1, y),  # Right
]


def in_bounds(x, y, grid) -> bool:
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def find_trail_head(
    grid: list[str],
    x: int,
    y: int,
    search_string: str,
    move_directions: list[Callable],
    seen: set,
):
    res = 0

    if not in_bounds(x, y, grid):
        return 0

    if grid[y][x] == "9" and search_string == "9" and (x, y) not in seen:
        seen.add((x, y))
        return 1

    if not search_string or grid[y][x] != search_string[0]:
        return 0
    for direction in directions:

        x_offset, y_offset = direction(x, y)
        res += find_trail_head(
            grid, x_offset, y_offset, search_string[1:], move_directions, seen
        )
    return res


def record_step(path: str, x: int, y: int) -> str:
    return path + str(x) + str(y)


def find_distinct_trail_head(
    grid: list[str],
    x: int,
    y: int,
    search_string: str,
    path: str,
    move_directions: list[Callable],
    seen: set,
):
    res = 0

    path = record_step(path, x, y)

    if not in_bounds(x, y, grid):
        return 0

    if grid[y][x] == "9" and search_string == "9" and path not in seen:
        seen.add(path)
        return 1

    if not search_string or grid[y][x] != search_string[0]:
        return 0

    path = record_step(path, x, y)

    for direction in directions:

        x_offset, y_offset = direction(x, y)
        res += find_distinct_trail_head(
            grid, x_offset, y_offset, search_string[1:], path, move_directions, seen
        )
    return res


def main() -> None:
    trail_map = read_file_content(file_path).splitlines()
    res_pt_1 = 0
    res_pt_2 = 0
    for y, row in enumerate(trail_map):
        for x, cell in enumerate(row):
            if cell == "0":
                res_pt_1 += find_trail_head(
                    trail_map, x, y, "0123456789", directions, set()
                )
                res_pt_2 += find_distinct_trail_head(
                    trail_map, x, y, "0123456789", "", directions, set()
                )

    print(f"Part 1: {res_pt_1}\nPart 2: {res_pt_2}")


if __name__ == "__main__":
    main()
