import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))

max_cnt = 0

i = 0
while(i != n - 1):
    cnt = 0
    for j in range(i + 1, n):
        if m[i] > m[j]:
            cnt += 1
        if m[i] <= m[j] or j == n - 1:
            i = j
            break
    max_cnt = max(max_cnt, cnt)

print(max_cnt)