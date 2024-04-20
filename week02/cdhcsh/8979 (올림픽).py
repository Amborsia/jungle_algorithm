import sys


def solve(n: int, k: int, data: list[list[int]]) -> int:
    answer = 1
    for d in data:
        if d[0] == k:
            for i in range(n):
                answer += int(compare(d, data[i]))
            return answer


def compare(l1: list[int], l2: list[int]) -> bool:
    if l1[0] == l2[0]: return False
    if l1[1] == l2[1]:
        if l1[2] == l2[2]:
            return l1[3] < l2[3]
        return l1[2] < l2[2]
    return l1[1] < l2[1]


if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    data = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
    print(solve(n, k, data))
