import re
from pathlib import Path
from typing import List

file_name = "day_3_input.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def read_file_content(file_path: Path) -> str:
    return file_path.read_text(encoding="utf-8")


def parse_mul_expressions(line: str) -> List[str]:
    return re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)


def extract_and_multiply(expressions: List[str]) -> int:
    return sum(
        int(left) * int(right)
        for expr in expressions
        if (match := re.search(r"(\d+),(\d+)", expr))
        for left, right in [match.groups()]
    )


def process_line(line: str) -> int:
    expressions = parse_mul_expressions(line)
    return extract_and_multiply(expressions)


def main() -> None:
    file_content = read_file_content(file_path)
    result = process_line(file_content)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
