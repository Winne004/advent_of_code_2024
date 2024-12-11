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
    disk_map = list(disk_map)
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


def main():
    disk_map = read_file_content(file_path)
    line = create_disk_map(disk_map)
    line = two_pointer(line)
    print(calculate_checksum(line))


if __name__ == "__main__":
    main()
