import sys


def solve(n: int, data: list, k: int) -> list:
    d = n // k
    for i in range(0, n, d):
        data[i:i + d] = sorted(data[i:i + d])
    return data


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    k = int(sys.stdin.readline())
    print(*solve(n, data, k))
