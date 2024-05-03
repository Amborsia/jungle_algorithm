from collections import deque
import copy
n, m = map(int, input().split())
graph = []
maxs = 0
for i in range(n):
    graph.append(list(map(int,input().split())))


def bfs():
    global maxs
    queue = deque()
    temp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 2:
                queue.append((i,j))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>= n or ny <0 or ny>=m:
                    continue
            if temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] = 2
                queue.append((nx,ny))

    answer = 0
    for i in range(n):
        answer += temp_graph[i].count(0)
    maxs = max(answer,maxs)
    
wall = 0
def soulution(wall):
    if wall == 3:
        bfs()
    else:
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    soulution(wall+1)
                    graph[i][j] = 0
     
soulution(0)
print(maxs)