import sys


def solve(n: int, data: list[str]) -> int:
    result = [[0] * n for _ in range(n)]
    for sub in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if data[i][j] == 'Y' or (data[i][sub] == 'Y' and data[sub][j] == 'Y'):
                    result[i][j] = 1
    return sum(max(result, key=sum))


if __name__ == '__main__':
    data = [sys.stdin.readline().strip() for _ in range(int(sys.stdin.readline()))]
    print(solve(len(data), data))
