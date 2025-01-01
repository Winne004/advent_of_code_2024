from pathlib import Path
from typing import Generator, Tuple

file_name = "day_12_input.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def read_file_content(file_path: Path) -> str:
    return file_path.read_text(encoding="utf-8")


DIRECTIONS = [
    lambda x, y: (x, y - 1),  # up
    lambda x, y: (x + 1, y),  # right
    lambda x, y: (x, y + 1),  # down
    lambda x, y: (x - 1, y),  # left
]


def yield_corners(x: int, y: int) -> Generator[Tuple[int, int, int, int], None, None]:
    directions_length = len(DIRECTIONS)
    for direction in range(directions_length):
        corner_1_x, corner_1_y = DIRECTIONS[direction](x, y)
        corner_2_x, corner_2_y = DIRECTIONS[(direction - 1) % directions_length](x, y)
        yield corner_1_x, corner_1_y, corner_2_x, corner_2_y


def count_external_corners(x: int, y: int, grid: list[str], value: str) -> int:
    res = 0

    for corner_1_x, corner_1_y, corner_2_x, corner_2_y in yield_corners(x, y):
        if (
            not in_bounds(corner_1_x, corner_1_y, grid)
            or grid[corner_1_y][corner_1_x] != value
        ) and (
            not in_bounds(corner_2_x, corner_2_y, grid)
            or grid[corner_2_y][corner_2_x] != value
        ):
            res += 1
    return res


def count_internal_corners(x: int, y: int, grid: list[str], value: str) -> int:
    res = 0

    for corner_1_x, corner_1_y, corner_2_x, corner_2_y in yield_corners(x, y):

        diagonal_x, diagonal_y = calc_internal_corner_coords(
            x, y, corner_1_x, corner_1_y, corner_2_x, corner_2_y
        )

        if (
            (
                in_bounds(corner_1_x, corner_1_y, grid)
                and grid[corner_1_y][corner_1_x] == value
            )
            and (
                in_bounds(corner_2_x, corner_2_y, grid)
                and grid[corner_2_y][corner_2_x] == value
            )
            and (grid[diagonal_y][diagonal_x] != value)
        ):
            res += 1
    return res


def calc_internal_corner_coords(
    x: int, y: int, corner_1_x: int, corner_1_y: int, corner_2_x: int, corner_2_y: int
) -> Tuple[int, int]:
    diagonal_x = corner_1_x if corner_1_x != x else corner_2_x
    diagonal_y = corner_1_y if corner_1_y != y else corner_2_y
    return diagonal_x, diagonal_y


def in_bounds(x: int, y: int, grid: list[str]) -> bool:
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


def find_sides(
    grid: list[str],
    x: int,
    y: int,
    seen: set,
    value: str,
) -> int:
    res = 0

    if not in_bounds(x, y, grid) or grid[y][x] != value:
        return 0

    if (x, y) not in seen:
        seen.add((x, y))
    else:
        return 0

    res = count_external_corners(x, y, grid, value)
    res += count_internal_corners(x, y, grid, value)

    for direction in DIRECTIONS:
        x_offset, y_offset = direction(x, y)
        res += find_sides(grid, x_offset, y_offset, seen, value)
    return res


def main() -> None:
    flower_bed = read_file_content(file_path).splitlines()

    visited_area = set()

    price = 0
    discounted_price = 0

    for y, row in enumerate(flower_bed):
        for x, cell_value in enumerate(row):
            if (x, y) not in visited_area:
                area = find_region(flower_bed, x, y, visited_area, cell_value)
                perimeter = find_perimeter(flower_bed, x, y, set(), cell_value)
                sides = find_sides(flower_bed, x, y, set(), cell_value)
                price += area * perimeter
                discounted_price += area * sides
                print(
                    f"Cell value: {cell_value}\n"
                    + f"Region: {area} cells\n"
                    + f" Perimeter: {perimeter}\n"
                    + f" Sides: {sides}\n\n"
                )

    print(f"Price: {price}")
    print(f"Discounted Price: {discounted_price}")


if __name__ == "__main__":
    main()
