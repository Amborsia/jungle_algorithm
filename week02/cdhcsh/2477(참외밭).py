import sys


def solve(k, data: list[list]) -> int:
    n = len(data)
    data = data + data
    maxi = 0

    for i in range(n):
        maxi = max(maxi, i, key=lambda j: data[j][1])
    subi = max(maxi - 1, maxi + 1, key=lambda j: data[j][1])
    if subi > maxi:
        sub = data[subi + 2][1] * data[subi + 3][1]
    else:
        sub = data[subi - 2][1] * data[subi - 3][1]
    return (data[maxi][1] * data[subi][1] - sub) * k


if __name__ == '__main__':
    k = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(6)]
    print(solve(k, arr))
