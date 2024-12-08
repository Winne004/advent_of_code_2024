from itertools import cycle
from pathlib import Path
from collections import Counter

file_name = "day_6_test_input.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def read_file_content(file_path: Path) -> str:
    return file_path.read_text(encoding="utf-8")


class Directions:
    def __init__(self):
        self.current_direction = 0
        self.directions = [
            self.go_up,
            self.go_right,
            self.go_down,
            self.go_left,
        ]
        self.trace = set()

    def go_down(self, x, y):
        return (x, y + 1)

    def go_up(self, x, y):
        return (x, y - 1)

    def go_left(self, x, y):
        return (x - 1, y)

    def go_right(self, x, y):
        return (x + 1, y)

    def turn_right(self):
        self.current_direction = (self.current_direction + 1) % len(self.directions)

    def generate_coords(self, x, y):
        return self.directions[self.current_direction](x, y)

    def yield_directions(self, x, y):
        for _ in range(4):
            yield self.generate_coords(x, y)


def in_bounds(x, y, grid):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def navigate(x, y, grid, directions):
    if not in_bounds(x, y, grid):
        return 1

    if grid[y][x] == "#":
        directions.turn_right()
        return 0

    for tmp_x, tmp_y in directions.yield_directions(x, y):

        tmp_x, tmp_y = directions.generate_coords(x, y)
        res = navigate(tmp_x, tmp_y, grid, directions)
        if res:
            print(f"({tmp_x}, {tmp_y})")
            return res + 1


def find_starting_point(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "^":
                return x, y
    return None


def main() -> None:
    map = read_file_content(file_path).splitlines()

    x, y = find_starting_point(map)
    directions = Directions()
    result = navigate(x, y, map, directions)
    print(result)


if __name__ == "__main__":
    main()
