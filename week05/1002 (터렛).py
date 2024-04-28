import sys


def solve(data: list[int]) -> int:
    def _get_distance(x1, y1, x2, y2) -> float:
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    x1, y1, r1, x2, y2, r2 = data
    d = _get_distance(x1, y1, x2, y2)
    if d == 0:
        if r1 == r2:
            return -1
        else:
            return 0
    if d == abs(r2 - r1): # 내접
        return 1
    if d > abs(r2 - r1):
        if d == r1 + r2: # 외접
            return 1
        if d < r1 + r2:
            return 2
    return 0


if __name__ == '__main__':
    data = [list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline().strip()))]
    [print(solve(case)) for case in data]
