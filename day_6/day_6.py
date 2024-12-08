from pathlib import Path
from typing import Generator, List, Optional, Set, Tuple

# Define the input file
file_name = "day_6_input.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def read_file_content(file_path: Path) -> List[str]:
    """Read and return the file content as a list of lines."""
    return file_path.read_text(encoding="utf-8").splitlines()


class Guard:
    def __init__(self, grid: List[List[str]]):
        self.current_direction: int = 0
        self.directions: List = [self.go_up, self.go_right, self.go_down, self.go_left]
        self.positions: Set[Tuple[int, int]] = set()
        self.positions_with_directions: Set[Tuple[int, int, int]] = set()
        self.grid: List[List[str]] = grid
        self.x: int
        self.y: int
        self.x, self.y = self.find_starting_point()
        self.previous_step: Optional[Tuple[int, int]] = None
        self.add_to_trace()

    def go_up(self) -> None:
        self.y -= 1

    def go_down(self) -> None:
        self.y += 1

    def go_left(self) -> None:
        self.x -= 1

    def go_right(self) -> None:
        self.x += 1

    def turn_right(self) -> None:
        """Turn right by updating the direction index."""
        self.current_direction = (self.current_direction + 1) % len(self.directions)

    def generate_coords(self) -> Tuple[int, int]:
        """Move to the next coordinates based on the current direction."""
        self.directions[self.current_direction]()
        return self.x, self.y

    def add_to_trace(self) -> None:
        """Record the current position in the trace."""
        self.positions.add((self.x, self.y))

    def add_to_trace_with_direction(self) -> None:
        """Record the position and direction in the trace."""
        self.positions_with_directions.add((self.x, self.y, self.current_direction))

    def find_starting_point(self) -> Tuple[int, int]:
        """Find and return the starting position marked by '^'."""
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == "^":
                    return x, y
        raise ValueError("No starting point '^' found in the grid.")

    def in_bounds(self) -> bool:
        """Check if the current position is within grid bounds."""
        return 0 <= self.x < len(self.grid[0]) and 0 <= self.y < len(self.grid)

    def is_obstructed(self) -> bool:
        """Check if the current position is obstructed by a wall."""
        return self.grid[self.y][self.x] == "#"

    def is_loop(self) -> bool:
        """Check if the current state (position + direction) is a loop."""
        return (
            self.x,
            self.y,
            self.current_direction,
        ) in self.positions_with_directions

    def navigate(self) -> None:
        """Navigate through the grid, recording visited positions."""
        while self.in_bounds():
            if self.is_obstructed():
                self.x, self.y = self.previous_step
                self.turn_right()
            else:
                self.previous_step = (self.x, self.y)
                self.add_to_trace()
            self.generate_coords()

    def navigate_with_loops(self) -> bool:
        """Navigate the grid and detect loops."""
        while self.in_bounds():
            if self.is_obstructed():
                if self.is_loop():
                    return True
                self.add_to_trace_with_direction()
                self.x, self.y = self.previous_step
                self.turn_right()
            else:
                self.previous_step = (self.x, self.y)
                self.add_to_trace()
            self.generate_coords()
        return False


def mutate_grid(
    grid: List[List[str]],
) -> Generator[Tuple[List[List[str]], int, int], None, None]:
    """Yield mutated versions of the grid with one position replaced by a wall."""
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if value == "^":
                continue
            original_value: str = grid[y][x]
            grid[y][x] = "#"
            yield grid, y, x
            grid[y][x] = original_value


def main() -> None:
    grid: List[str] = read_file_content(file_path)

    # Part 1: Navigate and count visited positions
    directions = Guard(grid=[list(row) for row in grid])  # Convert strings to lists
    directions.navigate()
    print(f"Part 1: {len(directions.positions)} positions visited")

    # Part 2: Detect obstacles causing loops
    grid: List[List[str]] = [list(row) for row in grid]
    obstacles_positions: Set[Tuple[int, int]] = set()
    for mutated_grid, y, x in mutate_grid(grid):
        directions = Guard(grid=mutated_grid)
        if directions.navigate_with_loops():
            obstacles_positions.add((x, y))
    print(f"Part 2: {len(obstacles_positions)} obstacle positions")


if __name__ == "__main__":
    main()
