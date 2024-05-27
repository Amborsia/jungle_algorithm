import sys


def solve(data: list[list[int]]) -> list:
    result = []
    for l in data:
        l.remove(max(l))
        l.remove(min(l))
        if max(l) - min(l) >= 4:
            result.append('KIN')
        else:
            result.append(sum(l))
    return result


if __name__ == '__main__':
    data = [list(map(int, sys.stdin.readline().split())) for i in range(int(sys.stdin.readline()))]
    print(*solve(data), sep='\n')
