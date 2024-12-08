from itertools import cycle
from pathlib import Path
from collections import Counter

file_name = "day_6_input.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def read_file_content(file_path: Path) -> str:
    return file_path.read_text(encoding="utf-8")


class Guard:
    def __init__(self, grid):
        self.current_direction = 0
        self.directions = [
            self.go_up,
            self.go_right,
            self.go_down,
            self.go_left,
        ]
        self.trace = set()
        self.grid = grid
        self.x, self.y = self.find_starting_point(grid)
        self.previous_step = None

    def go_down(self):
        self.y += 1

    def go_up(
        self,
    ):
        self.y -= 1

    def go_left(
        self,
    ):
        self.x -= 1

    def go_right(
        self,
    ):
        self.x += 1

    def turn_right(self):
        self.current_direction = (self.current_direction + 1) % len(self.directions)

    def generate_coords(self):
        self.directions[self.current_direction]()
        return self.x, self.y

    def find_starting_point(self, grid):
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == "^":
                    self.trace.add((x, y))
                    return x, y
        return None

    def in_bounds(self):
        return 0 <= self.x < len(self.grid[0]) and 0 <= self.y < len(self.grid)

    def is_obstructed(self):
        return self.grid[self.y][self.x] == "#"

    def navigate(self):
        while self.in_bounds():
            if self.is_obstructed():
                self.x, self.y = self.previous_step
                self.turn_right()
            else:
                self.previous_step = (self.x, self.y)
                self.trace.add((self.x, self.y))
                print(self.x, self.y)
            self.generate_coords()


def main() -> None:

    grid = read_file_content(file_path).splitlines()
    directions = Guard(grid=grid)
    directions.navigate()
    print(len(directions.trace) + 1)


if __name__ == "__main__":
    main()
