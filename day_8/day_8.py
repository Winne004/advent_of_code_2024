from collections import defaultdict
from pathlib import Path
from typing import List, Dict, Tuple

# Constants
file_name = "day_8_test_input.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def read_file_content(file_path: Path) -> List[str]:
    """Read and return the file content as a list of lines."""
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    return file_path.read_text(encoding="utf-8").splitlines()


def get_antennas_locations(grid: List[str]) -> Dict[str, List[Tuple[int, int]]]:
    """Extract locations of antennas from the grid."""
    antenna_locations = defaultdict(list)
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != ".":  # Antennas are any non-dot character
                antenna_locations[cell].append((y, x))
    return antenna_locations


def in_bounds(x: int, y: int, grid: List[str]) -> bool:
    """Check if the coordinates are within the grid bounds."""
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def main():
    """Main function to execute the program."""
    try:
        grid = read_file_content(file_path)
        if not grid:
            print("Grid is empty. Exiting.")
            return

        antenna_locations = get_antennas_locations(grid)

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
