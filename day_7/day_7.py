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


def recurse_pt_1(line: List[str], target: int, current_val) -> int:
    """Recursively solve the puzzle."""
    if not line:
        if current_val == target:
            return 1
        return 0
    if current_val > target:
        return 0

    return recurse_pt_1(line[1:], target, current_val + line[0]) or recurse_pt_1(
        line[1:], target, current_val * line[0]
    )


def recurse_pt_2(line: List[int], target: int, current_val: int) -> List[int]:
    """
    Recursively solve the puzzle and return a flattened list of results, including concatenations.

    :param line: List of integers to process.
    :param target: Target value to match.
    :param current_val: Current value in the recursion.
    :return: Flattened list of solutions.
    """
    if not line:

        return 1 if current_val == target else 0

    if current_val != 0:
        concatenated_value = int(str(current_val) + str(line[0]))
        return (
            recurse_pt_2(line[1:], target, current_val + line[0])
            or recurse_pt_2(line[1:], target, current_val * line[0])
            or recurse_pt_2(line[1:], target, concatenated_value)
        )

    else:
        return recurse_pt_2(line[1:], target, current_val + line[0]) or recurse_pt_2(
            line[1:], target, current_val * line[0]
        )


def main():
    # Read the file content
    lines = read_file_content(file_path)
    lines = split_lines(lines)
    res_pt_1 = 0
    res_pt_2 = 0
    for target, line in lines:

        if recurse_pt_2(line, target, 0):
            res_pt_2 += target
    print(res_pt_1)
    print(res_pt_2)


if __name__ == "__main__":
    main()
