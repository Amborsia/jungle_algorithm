import sys

n, m, r = map(int, sys.stdin.readline().split())

l = [[] for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    l[a].append(b)
    l[b].append(a)

for i in range(1, n + 1):
    l[i].sort(reverse=True)

cnt = 1

def dfs(k):
    global cnt
    visit[k] = cnt
    cnt += 1
    for i in l[k]:
        if visit[i] == 0:
            dfs(i)

dfs(r)

print(*visit[1:], sep="\n")