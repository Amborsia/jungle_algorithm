import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())

map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = [[0] * m for _ in range(n)]
deq = deque()

loops = min(n, m) // 2
for i in range(loops):
    deq.clear()
    deq.extend(map[i][i:m-i])
    deq.extend([row[m-i-1] for row in map[i+1:n-i-1]])
    deq.extend(map[n-i-1][i:m-i][::-1])
    deq.extend([row[i] for row in map[i+1:n-i-1]][::-1])
    
    deq.rotate(-r)
    
    for j in range(i, m-i):
        answer[i][j] = deq.popleft()
    for j in range(i+1, n-i-1):
        answer[j][m-i-1] = deq.popleft()
    for j in range(m-i-1, i-1, -1):
        answer[n-i-1][j] = deq.popleft()  
    for j in range(n-i-2, i, -1):
        answer[j][i] = deq.popleft()    

for i in range(n):
    print(*answer[i])