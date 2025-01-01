from pathlib import Path
import re

file_name = "day_13_test_input.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def read_input(file_path: Path):

    data = file_path.read_text(encoding="utf-8")

    pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"

    matches = re.findall(pattern, data)

    extracted_data = [
        {
            "Button A (X)": int(match[0]),
            "Button A (Y)": int(match[1]),
            "Button B (X)": int(match[2]),
            "Button B (Y)": int(match[3]),
            "Prize (X)": int(match[4]),
            "Prize (Y)": int(match[5]),
        }
        for match in matches
    ]
    return extracted_data


class ClawRuleset:
    def __init__(self, ruleset):
        self.button_a = self.extract_moves(ruleset, "Button A")
        self.button_b = self.extract_moves(ruleset, "Button B")
        self.prize = (ruleset["Prize (X)"], ruleset["Prize (Y)"])

    def extract_moves(self, ruleset, button):
        if button == "Button A":
            return lambda x, y, dx=ruleset["Button A (X)"], dy=ruleset[
                "Button A (Y)"
            ]: (
                x + int(dx),
                y + int(dy),
            )
        elif button == "Button B":
            return lambda x, y, dx=ruleset["Button B (X)"], dy=ruleset[
                "Button B (Y)"
            ]: (
                x + int(dx),
                y + int(dy),
            )


def dfs(x, y, visited, ruleset, moves):
    min_moves = float("inf")

    if x == 8400 and y == 5400:
        print("here")

    if (x, y) == ruleset.prize:
        return moves

    if moves == 0:
        return min_moves

    if (x, y, moves) in visited:
        return visited[(x, y, moves)]

    button_a_tmp_x, button_a_tmp_y = ruleset.button_a(x, y)
    button_b_tmp_x, button_b_tmp_y = ruleset.button_b(x, y)

    min_moves = min(
        min_moves,
        dfs(button_a_tmp_x, button_a_tmp_y, visited, ruleset, moves - 1),
        dfs(button_b_tmp_x, button_b_tmp_y, visited, ruleset, moves - 1),
    )

    visited[(x, y, moves)] = min_moves

    return visited[(x, y, moves)]


def main() -> None:
    rulesets = read_input(file_path)
    for ruleset in rulesets:
        claw_ruleset = ClawRuleset(ruleset)
        visited = {}
        res = dfs(0, 0, visited, claw_ruleset, 200)
        print(res)


if __name__ == "__main__":
    main()
