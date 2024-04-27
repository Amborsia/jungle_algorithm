import sys

input = sys.stdin.readline

def ans():
    n, l = map(int, input().split())
    loc = list(map(int, input().split()))
    cnt = 0
    loc.sort()

    i = 0
    while i < n:
        temp_i = i
        for j in range(loc[temp_i], loc[temp_i] + l):
            if j in loc:
                i += 1
        cnt += 1

    print(cnt)


ans()
