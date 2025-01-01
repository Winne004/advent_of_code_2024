from pathlib import Path
import re

file_name = "day_13_input.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def read_input(file_path: Path):
    data = file_path.read_text(encoding="utf-8")
    pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
    matches = re.findall(pattern, data)
    return [
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


class ClawRuleset:
    def __init__(self, ruleset):
        self.button_a = self._create_move_function(ruleset, "Button A")
        self.button_b = self._create_move_function(ruleset, "Button B")
        self.prize = (ruleset["Prize (X)"], ruleset["Prize (Y)"])

    def _create_move_function(self, ruleset, button):
        dx, dy = ruleset[f"{button} (X)"], ruleset[f"{button} (Y)"]
        return lambda x, y: (x + dx, y + dy)


def dfs(x, y, visited, ruleset, moves, cost):
    if (x, y) == ruleset.prize:
        return cost

    if moves == 0:
        return float("inf")

    if (x, y, moves) in visited:
        return visited[(x, y, moves)]

    button_a_tmp_x, button_a_tmp_y = ruleset.button_a(x, y)
    button_b_tmp_x, button_b_tmp_y = ruleset.button_b(x, y)

    cost_a = dfs(button_a_tmp_x, button_a_tmp_y, visited, ruleset, moves - 1, cost + 3)
    cost_b = dfs(button_b_tmp_x, button_b_tmp_y, visited, ruleset, moves - 1, cost + 1)

    min_cost = min(cost_a, cost_b)
    visited[(x, y, moves)] = min_cost

    return min_cost


def main() -> None:
    rulesets = read_input(file_path)
    total_cost = 0
    for ruleset in rulesets:
        claw_ruleset = ClawRuleset(ruleset)
        visited = {}
        result = dfs(0, 0, visited, claw_ruleset, 200, 0)
        if result < float("inf"):
            total_cost += result
    print(f"Total cost to reach all prizes: {total_cost}")


if __name__ == "__main__":
    main()
