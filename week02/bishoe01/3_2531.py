import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())

arr = [int(input()) for _ in range(n)]
# [7, 9, 7, 30, 2, 7, 9, 25]
cnt = 0
stomach = [0] * (d + 1)

for i in range(k):
    if (stomach[arr[i]] == 0):
        cnt += 1
    stomach[arr[i]] += 1

max_cnt = cnt

if (stomach[c] == 0):
    max_cnt += 1

for position in range(k, n+k):
    if (stomach[arr[position-k]] == 1):
        cnt -= 1
    stomach[arr[position-k]] -= 1

    if (stomach[arr[position % n]] == 0):
        cnt += 1
    stomach[arr[position % n]] += 1

    if (stomach[c] == 0):
        max_cnt = max(max_cnt, cnt+1)
    else:
        max_cnt = max(max_cnt, cnt)

print(max_cnt)
