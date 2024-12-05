from pathlib import Path
from collections import Counter

file_name = "day_4_input.txt"
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


def go_up_right(x, y):
    _, y = go_up(x, y)
    x, _ = go_right(x, y)
    return (x, y)


def go_up_left(x, y):
    _, y = go_up(x, y)
    x, _ = go_left(x, y)
    return (x, y)


def go_down_left(x, y):
    _, y = go_down(x, y)
    x, _ = go_left(x, y)
    return (x, y)


def go_down_right(x, y):
    _, y = go_down(x, y)
    x, _ = go_right(x, y)
    return (x, y)


directions = [
    go_down,
    go_up,
    go_left,
    go_right,
    go_up_right,
    go_up_left,
    go_down_left,
    go_down_right,
]


def in_bounds(x, y, grid):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def count_xmas_matches(grid, x, y, search_string, direction):
    res = 0
    if not in_bounds(x, y, grid):
        return 0
    if grid[y][x] != search_string[0]:
        return 0
    if grid[y][x] == "S" and search_string == "S":
        return 1

    x_offset, y_offset = direction(x, y)
    res += count_xmas_matches(grid, x_offset, y_offset, search_string[1:], direction)
    return res


def count_x_mas_matches(
    grid,
    x,
    y,
):
    coords = []
    for direction in [go_up_right, go_down_left, go_up_left, go_down_right]:
        tmp_x, tmp_y = direction(x, y)
        if not in_bounds(tmp_x, tmp_y, grid):
            return 0
        coords.append(grid[tmp_y][tmp_x])
    c = Counter(coords)
    if c["S"] != 2 or c["M"] != 2 or coords[0] == coords[1]:
        return 0
    return 1


def main() -> None:
    word_search = read_file_content(file_path).splitlines()
    xmas_res = 0
    x_mas_res = 0
    for y, row in enumerate(word_search):
        for x, char in enumerate(row):
            if char == "X":
                for direction in directions:
                    xmas_res += count_xmas_matches(word_search, x, y, "XMAS", direction)
            if char == "A":
                x_mas_res += count_x_mas_matches(word_search, x, y)
    print(f"pt 1: {xmas_res}")
    print(f"pt 2: {x_mas_res}")


if __name__ == "__main__":
    main()
