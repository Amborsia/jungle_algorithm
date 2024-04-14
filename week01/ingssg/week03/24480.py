import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline
cnt = 1     # 몇 번째 방문인지


def dfs(graph, start, visited, order):
    global cnt
    visited[start] = True
    order[start] = cnt
    for next in graph[start]:
        if not visited[next]:
            cnt += 1
            dfs(graph, next, visited, order)


def ans():
    global cnt
    n, m, r = map(int, input().split())     # 정점수, 간선 수, 시작 정점
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    order = [0] * (n + 1)       # order[index] = k ,  index 정점의 방문 순서 k
    for _ in range(m):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
    for i in graph:         # 내림차순 방문이기 때문에 들를 수 있는 정점들 내림차순 정렬
        i.sort(reverse=True)
    visited[r] = True
    order[r] = cnt
    dfs(graph, r, visited, order)

    for i in order[1:]:
        print(i)


ans()
