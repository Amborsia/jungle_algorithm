import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())


arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


# BFS
visited = [False] * (n + 1)
visited[1] = True
queue = deque([1])
distance = [0] * (n+1)
while (queue):
    tmp = queue.popleft()
    for element in arr[tmp]:
        if (not visited[element]):
            visited[element] = True
            distance[element] = distance[tmp]+1
            queue.append(element)
print(distance)
answer1 = 0
max_distance = max(distance)

cnt = 0
for i in range(n+1):
    if (distance[i] == max_distance):
        if (answer1 == 0):
            answer1 = i
        cnt += 1

print(answer1, max_distance, cnt)
