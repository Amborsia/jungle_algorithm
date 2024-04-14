import sys
import math

input = sys.stdin.readline


def ans():
    k = int(input())
    cnt = 0
    temp = 1
    temp_k = k

    if 2 ** (int(math.log2(k))) == k:
        print(k, 0)
        return

    while k > 0:
        cnt += 1
        k >>= 1
        temp <<= 1

    if temp_k % 2 == 0:
        print(temp, cnt - 1)
    else:
        print(temp, cnt)


ans()
