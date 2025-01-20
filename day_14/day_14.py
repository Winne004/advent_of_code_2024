import math
from pathlib import Path
import re
from typing import Counter

# file_name = "day_14_test_input.txt"
file_name = "day_14_input.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def parse_input(file_path: Path = file_path):
    data = file_path.read_text(encoding="utf-8")
    pattern = r"^p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)"

    matches = re.findall(pattern, data, flags=re.MULTILINE)

    return [
        {
            "x": int(match[0]),
            "y": int(match[1]),
            "x_velocity": int(match[2]),
            "y_velocity": int(match[3]),
        }
        for match in matches
    ]


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Robot:
    def __init__(self, x: int, y: int, x_velocity, y_velocity, grid) -> None:
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.grid = grid

    def move(self) -> None:
        self.x = (self.x + self.x_velocity) % self.grid.width
        self.y = (self.y + self.y_velocity) % self.grid.height


class RobotSimulator:
    def __init__(self, grid) -> None:
        self.grid = grid
        self.robots = []
        self.vertical_midpoint = self.grid.height // 2
        self.horizontal_midpoint = self.grid.width // 2

    def __iter__(self):
        return iter(self.robots)

    def __getitem__(self, index):
        return self.robots[index]

    def __len__(self):
        return len(self.robots)

    def add_robot(self, robot: Robot) -> None:
        self.robots.append(robot)

    def step(self) -> None:
        for robot in self.robots:
            robot.move()

    def get_robot_positions(self):
        return [(robot.x, robot.y) for robot in self.robots]

    def identify_quadrant(self, x, y):
        if x < self.horizontal_midpoint and y < self.vertical_midpoint:
            return "top_left"
        elif x > self.horizontal_midpoint and y < self.vertical_midpoint:
            return "top_right"
        elif x < self.horizontal_midpoint and y > self.vertical_midpoint:
            return "bottom_left"
        elif x > self.horizontal_midpoint and y > self.vertical_midpoint:
            return "bottom_right"
        return None

    def calculate_robots_per_quad(self):
        number_of_robots_per_quad = Counter(
            {"top_left": 0, "top_right": 0, "bottom_left": 0, "bottom_right": 0}
        )

        for robot in self.robots:
            identified_quad = self.identify_quadrant(robot.x, robot.y)
            if identified_quad:
                number_of_robots_per_quad[identified_quad] += 1

        return number_of_robots_per_quad


def main() -> None:
    data = parse_input(file_path=file_path)
    robot_simulator = RobotSimulator(Grid(width=101, height=103))
    # robot_simulator = RobotSimulator(Grid(width=11, height=7))
    for robot_data in data:
        robot = Robot(**robot_data, grid=robot_simulator.grid)
        robot_simulator.add_robot(robot)

    for sec in range(100):
        robot_simulator.step()
        robots_per_quad = robot_simulator.calculate_robots_per_quad()

    print(robots_per_quad)
    print(math.prod(robots_per_quad.values()))


if __name__ == "__main__":
    main()
