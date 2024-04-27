import sys

n = int(sys.stdin.readline())

l = []
cnt = [1 for _ in range(n)]
max_cnt = 1

for _ in range(n):
    l.append(int(sys.stdin.readline()))

l.sort()

for i in range(n):
    n_list = [j for j in range(l[i], l[i] + 5)]
    for j in range(1, 5):
        if i + j < n and l[i + j] in n_list:
            cnt[i] += 1
    max_cnt = max(max_cnt, cnt[i])

print(5 - max_cnt)