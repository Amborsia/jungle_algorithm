import sys

intput = sys.stdin.readline


def ans():
    n = int(input())
    cnt = 0
    while n > 0:
        cnt += (n & 1)
        n >>= 1
    print(cnt)


ans()
