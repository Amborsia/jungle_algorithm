def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return
    if graph[x][y] == -1:
        visited[x][y] = True
    if not visited[x][y]:
        visited[x][y] = True
        dfs(x, y + graph[x][y])
        dfs(x + graph[x][y], y)


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dfs(0, 0)
if visited[-1][-1]:
    print("HaruHaru")
else:
    print("Hing")
