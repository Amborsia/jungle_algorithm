import sys


def solve(n: int, m: int, data: list[int]) -> list[int]:
    data.sort(reverse=True)
    res = [0, 0]
    for i in range(m):
        income = data[i] * min(n, i + 1)
        if income >= res[1]:
            res = data[i], income
    return res


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    customs = [int(sys.stdin.readline()) for _ in range(m)]
    print(*solve(n, m, customs))
