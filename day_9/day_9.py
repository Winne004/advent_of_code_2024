from pathlib import Path

file_name = "day_9_input.txt"
script_dir = Path(__file__).parent
file_path = script_dir / file_name


def read_file_content(path: Path) -> str:
    """Read and return the file content as a list of lines."""
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return path.read_text(encoding="utf-8")


def create_disk_map(disk_map: str) -> list:
    line = []
    free_space = False
    i = 0
    for v in str(disk_map):
        if not free_space:
            line += [str(i)] * (int(v))
            i += 1
        else:
            line += [None] * (int(v))
        free_space = not free_space
    return line


def two_pointer(disk_map: list) -> list:
    i, j = 0, len(disk_map) - 1
    while i < j:
        while i < j and disk_map[i]:
            i += 1
        while i < j and not disk_map[j]:
            j -= 1
        if i < j:
            disk_map[i], disk_map[j] = disk_map[j], disk_map[i]
            i += 1
            j -= 1

    return disk_map


def calculate_checksum(line: list) -> int:
    res = 0
    for i, v in enumerate(line):
        if v:
            res += i * int(v)
    return res


def find_contiguous_space(disk_map: list, target: int, finish: int) -> int:
    i = 0

    while i < finish:
        none_count = 0
        while not disk_map[i + none_count]:
            none_count += 1
            if none_count >= target:
                for _ in range(i, i + target):
                    disk_map[i], disk_map[finish] = disk_map[finish], disk_map[i]
                    i += 1
                    finish -= 1
                return disk_map
        i += 1
    return disk_map


def pt_2(disk_map: list) -> int:
    i, j = 0, len(disk_map) - 1
    while j >= 0:
        while i < j and not disk_map[j]:
            j -= 1
        space_needed = disk_map.count(disk_map[j])
        disk_map = find_contiguous_space(disk_map, space_needed, j)
        j -= 1

    return disk_map


def main():
    disk_map = read_file_content(file_path)
    disk_map = create_disk_map(disk_map)
    disk_map_p2 = disk_map.copy()

    print(f"P1: {calculate_checksum(two_pointer(disk_map))}")

    print(f"P2: {calculate_checksum(pt_2(disk_map_p2))}")


if __name__ == "__main__":
    main()
