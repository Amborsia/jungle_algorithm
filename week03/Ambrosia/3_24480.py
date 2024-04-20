import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
N,M,R = map(int,input().split())
cnt = 1
visited = [False]*(N+1)
lit = [[] for _ in range(N+1)]
answer = [0]*(N+1)
def dfs(S):
    global cnt
    visited[S] = True
    answer[S] = cnt

    for i in lit[S]:
        if not visited[i] :
            cnt+=1
            dfs(i)
            
        
        
for i in range(M):
    a,b = map(int,input().split())
    lit[a].append(b)
    lit[b].append(a)
for i in range(N+1):
    lit[i].sort(reverse=True)

dfs(R)

for i in answer[1:]:
    print(i)
    
