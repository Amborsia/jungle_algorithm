import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [int(input()) for i in range(N)]
graph.sort()
dic = {}
cnt = 0

for i in range(N):
    quiz = int(graph[i])
    if quiz in dic:
        continue
    dic[quiz] = i
for i in range(M):
    q=int(input())
    if q in dic : 
        print(dic[q])
    else: print(-1)




