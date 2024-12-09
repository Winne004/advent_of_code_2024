from pathlib import Path
from typing import List


file_name = "day_7_input.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def read_file_content(file_path: Path) -> List[str]:
    """Read and return the file content as a list of lines."""
    return file_path.read_text(encoding="utf-8").splitlines()


def split_lines(lines: List[str]) -> List[str]:
    """Split the lines into a list of strings."""
    return [
        [int(target), list(map(int, operators.strip().split(" ")))]
        for line in lines
        for target, operators in [line.split(":")]
    ]


def recurse(line: List[str], target: int, current_val) -> int:
    """Recursively solve the puzzle."""
    if not line:
        if current_val == target:
            return 1
        return 0
    if current_val > target:
        return 0

    return recurse(line[1:], target, current_val + line[0]) or recurse(
        line[1:], target, current_val * line[0]
    )


def main():
    # Read the file content
    lines = read_file_content(file_path)
    lines = split_lines(lines)
    res = 0
    for target, line in lines:
        target: int
        line: List[str]
        if recurse(line, target, 0):
            res += target

    print(res)


if __name__ == "__main__":
    main()
