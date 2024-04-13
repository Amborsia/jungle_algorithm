import sys
from math import log2


def solve(n: int) -> list:
    l = int(log2(n))
    if 2**l == n:
        return [2**l, 0]
    else:
        l += 1
    cnt = l
    while not n & 1:
        cnt -= 1
        n >>= 1
    return [2**l,cnt]


if __name__ == '__main__':
    print(*solve(int(sys.stdin.readline())))
