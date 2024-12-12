from pathlib import Path
from collections import Counter

file_name = "day_10_input.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def read_file_content(file_path: Path) -> str:
    return file_path.read_text(encoding="utf-8")


def go_down(x, y):
    return (x, y + 1)


def go_up(x, y):
    return (x, y - 1)


def go_left(x, y):
    return (x - 1, y)


def go_right(x, y):
    return (x + 1, y)


directions = [
    go_down,
    go_up,
    go_left,
    go_right,
]


def in_bounds(x, y, grid):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def find_trail_head(grid, x, y, search_string, move_directions, seen):
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


def main():
    res = 0
    trail_map = read_file_content(file_path).splitlines()
    for y, row in enumerate(trail_map):
        for x, cell in enumerate(row):
            if cell == "0":
                res += find_trail_head(trail_map, x, y, "0123456789", directions, set())

    print(res)


if __name__ == "__main__":
    main()
