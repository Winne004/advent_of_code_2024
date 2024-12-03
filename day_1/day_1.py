from collections import Counter
from pathlib import Path
from typing import List, Tuple

file_name = "day_1_input.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def read_file_to_lists(file_path: Path) -> Tuple[List[int], List[int]]:
    left_list: List[int] = []
    right_list: List[int] = []
    with open(file_path, "r") as f:
        for line in f:
            item_1, item_2 = map(int, line.strip().split())
            left_list.append(item_1)
            right_list.append(item_2)
    return left_list, right_list


def calculate_differences(left_list: List[int], right_list: List[int]) -> List[int]:
    return [abs(l - r) for l, r in zip(left_list, right_list)]


def calculate_similarity_scores(
    left_list: List[int], right_list: List[int]
) -> List[int]:
    count_of_numbers = Counter(right_list)
    return [number * count_of_numbers[number] for number in left_list]


def main() -> None:
    # Part 1 solution
    left_list, right_list = read_file_to_lists(file_path)
    left_list.sort()
    right_list.sort()
    differences = calculate_differences(left_list, right_list)
    sum_of_differences = sum(differences)
    print(f"Sum of differences: {sum_of_differences}")

    # Part 2 solution
    res = calculate_similarity_scores(left_list, right_list)
    print(f"Sum of similarity scores: {sum(res)}")


if __name__ == "__main__":
    main()
