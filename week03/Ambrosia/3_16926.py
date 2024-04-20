import sys
from collections import deque
input = sys.stdin.readline
N, M, R = map(int, input().split())

lit = []
answer = [[0]*M for _ in range(N)]
deq = deque()

for i in range(N):
    lit.append(list(input().split()))

loops = min(N, M) // 2
for i in range(loops):
    deq.clear()
    deq.extend(lit[i][i:M-i])
    deq.extend([row[M-i-1] for row in lit[i+1:N-i-1]])
    deq.extend(lit[N-i-1][i:M-i][::-1])
    deq.extend([row[i] for row in lit[i+1:N-i-1]][::-1])    
    
    deq.rotate(-R)
    for j in range(i,M-i):
        answer[i][j] = deq.popleft()
    for j in range(i+1,N-i-1):
        answer[j][M-i-1] = deq.popleft()
    for j in range(M-i-1,i-1,-1):
        answer[N-i-1][j] = deq.popleft()
    for j in range(N-i-2,i,-1):
        answer[j][i] = deq.popleft()

for i in answer:
    print(" ".join(i))