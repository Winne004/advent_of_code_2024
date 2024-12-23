from pathlib import Path

file_name = "day_12_input.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def read_file_content(file_path: Path) -> str:
    return file_path.read_text(encoding="utf-8")


DIRECTIONS = [
    lambda x, y: (x + 1, y),  # right
    lambda x, y: (x - 1, y),  # left
    lambda x, y: (x, y - 1),  # up
    lambda x, y: (x, y + 1),  # down
]


def in_bounds(x, y, grid) -> bool:
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def find_region(grid: list[str], x: int, y: int, seen: set, value: str) -> int:
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

    for direction in DIRECTIONS:
        x_offset, y_offset = direction(x, y)
        res += find_region(grid, x_offset, y_offset, seen, value)
    return res


def find_perimeter(
    grid: list[str],
    x: int,
    y: int,
    seen: set,
    value: str,
) -> int:
    res = 0

    if not in_bounds(x, y, grid) or grid[y][x] != value:
        return 1

    if (x, y) not in seen:
        seen.add((x, y))
    else:
        return 0

    for direction in DIRECTIONS:
        x_offset, y_offset = direction(x, y)
        res += find_perimeter(grid, x_offset, y_offset, seen, value)
    return res


def main() -> None:
    flower_bed = read_file_content(file_path).splitlines()

    visited_area = set()
    result = 0

    for y, row in enumerate(flower_bed):
        for x, cell_value in enumerate(row):
            if (x, y) not in visited_area:
                area = find_region(flower_bed, x, y, visited_area, cell_value)
                perimeter = find_perimeter(flower_bed, x, y, set(), cell_value)
                result += area * perimeter
                print(f"Region: {area} cells" + f" Perimeter: {perimeter}")

    print(result)


if __name__ == "__main__":
    main()
