import sys
from collections import deque


def solve(n: int, m: int, k: int, data: list[list[int]]) -> list[list[int]]:
    result = [[] for _ in range(m)]
    max_level = min(n // 2, m // 2)
    levels = [deque() for _ in range(max_level)]
    lvl = 0
    while lvl < max_level:
        for p in range(lvl, m - lvl - 1):
            levels[lvl].append(data[lvl][p])
        for p in range(lvl, n - lvl - 1):
            levels[lvl].append(data[p][-(lvl + 1)])
        for p in range((m - 1) - lvl, lvl, -1):
            levels[lvl].append(data[-(lvl + 1)][p])
        for p in range((n - 1) - lvl, lvl, -1):
            levels[lvl].append(data[p][lvl])
        lvl += 1

    lvl = 0
    while lvl < max_level:
        levels[lvl].rotate(-k)
        for p in range(lvl, m - lvl - 1):
            data[lvl][p] = levels[lvl].popleft()
        for p in range(lvl, n - lvl - 1):
            data[p][-(lvl + 1)] = levels[lvl].popleft()
        for p in range((m - 1) - lvl, lvl, -1):
            data[-(lvl + 1)][p] = levels[lvl].popleft()
        for p in range((n - 1) - lvl, lvl, -1):
            data[p][lvl] = levels[lvl].popleft()
        lvl += 1
    return data


if __name__ == '__main__':
    n, m, k = map(int, sys.stdin.readline().split())
    data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    arr = solve(n, m, k, data)
    [print(*l) for l in arr]
