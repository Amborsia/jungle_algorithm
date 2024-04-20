import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n+1)
cnt = 1
ordered = [0] * (n+1)

# 내림차순 방문


def dfs(start):
    global cnt
    visited[start] = True
    ordered[start] = cnt
    graph[start].sort(reverse=True)
    for element in (graph[start]):
        if not visited[element]:
            cnt += 1
            dfs(element)


for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(r)

for element in ordered[1:]:
    print(element)
