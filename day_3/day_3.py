import re
from pathlib import Path
from typing import List

file_name = "day_3_input.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def read_file_content(file_path: Path) -> str:
    return file_path.read_text(encoding="utf-8")


def extract_mul(line: str) -> int:
    return [
        (match.start(), int(match.group(1)), int(match.group(2)))
        for match in re.finditer(r"mul\((\d+),(\d+)\)", line)
    ]


def extract_do_and_dont(
    line: str,
) -> int:
    return [
        (match.start(), match.group()) for match in re.finditer(r"don't\(\)", line)
    ] + [(match.start(), match.group()) for match in re.finditer(r"do\(\)", line)]


def process_line(line: str) -> int:
    mul_expresions = extract_mul(line)
    return sum([left * right for _, left, right in mul_expresions])


def sum_based_on_instructions(merged: List[tuple]) -> int:
    result = 0
    enabled = True
    for x in merged:
        if len(x) == 3:
            if enabled:
                _, left, right = x
                result += left * right
        else:
            _, instruction = x
            if instruction == "don't()":
                enabled = False
            elif instruction == "do()":
                enabled = True
    return result


def process_line_pt2(line: str) -> int:
    mul_expresions = extract_mul(line)
    do_and_dont = extract_do_and_dont(line)
    merged = sorted(mul_expresions + do_and_dont, key=lambda x: x[0])
    return sum_based_on_instructions(merged)


def main() -> None:
    file_content = read_file_content(file_path)
    result = process_line(file_content)
    print(f"Result: {result}")

    result_pt2 = process_line_pt2(file_content)
    print(result_pt2)


if __name__ == "__main__":
    main()
