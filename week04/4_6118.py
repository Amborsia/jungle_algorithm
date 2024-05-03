import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
lit = [[]for i in range(n+1)]
answer = []
cnt = 0
for i in range(m):
    x,y = map(int,input().split())
    lit[x].append(y)
    lit[y].append(x)
visited = [0] * (n+1)

def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node] = 1
    while queue:
        
        node = queue.popleft()
        #print(node, end = ' ')
        for i in lit[node]:
            if visited[i] == 0:
                visited[i] = visited[node]+1
                queue.append(i)
                
bfs(1)

maxs = max(visited)
print(visited.index(maxs), maxs-1, visited.count(maxs))