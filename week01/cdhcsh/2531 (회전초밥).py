import sys
from collections import defaultdict


def solve(n: int, k: int, c: int, data: list) -> int:
    sushi = defaultdict()
    sushi[c] += n
    for n in data[:k]:
        sushi[n] += 1
    result = len(sushi)
    for i in range(1, n):
        sushi[data[(i + k - 1) % n]] += 1
        sushi[data[i - 1]] -= 1
        if sushi[data[i - 1]]: sushi.pop(data[i - 1])
        result = max(result, len(sushi))
    return result


if __name__ == '__main__':
    n, d, k, c = map(int, sys.stdin.readline().split())
    data = [int(sys.stdin.readline()) for _ in range(n)]
    print(solve(n, k, c, data))
