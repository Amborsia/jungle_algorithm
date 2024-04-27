import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

v = [[] for _ in range(n + 1)]
visit = [-1 for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    v[a].append(b)
    v[b].append(a)

que = deque()

visit[1] = 0
for i in v[1]:
    que.append(i)
    visit[i] = visit[1] + 1

while que:
    top = que.popleft()
    for i in v[top]:
        if (visit[i] == -1):
            visit[i] = visit[top] + 1
            que.append(i)

farm = -sys.maxsize
farm_i = 0
farm_cnt = 1
for i in range(1, n + 1):
    if farm < visit[i]:
        farm = visit[i]
        farm_i = i
        farm_cnt = 1
    elif farm == visit[i]:
        farm_cnt += 1
    
print(farm_i, farm, farm_cnt)