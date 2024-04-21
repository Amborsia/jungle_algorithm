import sys
sys.setrecursionlimit(10**9)


def dfs(visited, graph, r):
    global count
    count += 1
    visited[r] = count
    for adj in graph[r]:
        if not visited[adj]:
            dfs(visited, graph, adj)


N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
count = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort(reverse=True)

dfs(visited, graph, R)

for i in range(1, N+1):
    if visited[i]:
        print(visited[i])
    else:
        print(0)

