# 소트마스터 배지훈의 후계자
# https://www.acmicpc.net/problem/20551

import sys

input = sys.stdin.readline


def ans():
    n, m = map(int, input().strip().split())

    data = [int(input().strip()) for _ in range(n)]
    data.sort()

    idx_lst = {}
    for idx, d in enumerate(data):
        if d in idx_lst:
            continue
        idx_lst[d] = idx

    for a in range(m):
        q = int(input())
        if q in idx_lst:
            print(idx_lst[q])
        else:
            print(-1)


ans()
