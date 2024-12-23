from functools import lru_cache


def to_list(input):
    input = input.strip()
    return input.split(" ")


def apply_rule(stone):
    left = None
    right = None

    if stone == "0":
        left = "1"
    elif len(stone) % 2 == 0:
        mid = len(stone) // 2
        left = str(int(stone[:mid]))
        right = str(int(stone[mid:]))
    else:
        left = str(int(stone) * 2024)

    return left, right


@lru_cache(maxsize=None)
def recurse(stones, depth):

    if depth == 0:
        return 1

    res = 0

    left, right = apply_rule(stones)
    res += recurse(left, depth - 1)
    res += recurse(right, depth - 1) if right else 0
    return res


def main():
    input = "17639 47 3858 0 470624 9467423 5 188"
    input = to_list(input)
    res = 0
    for stone in input:
        res += recurse(stone, 75)
    print(res)


if __name__ == "__main__":
    main()
