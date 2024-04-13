import sys
input = sys.stdin.readline

N,d,k,c = map(int,input().split())
sushi = []
for i in range(N):
    sushi.append(int(input().strip()))


lit = [[]for i in range(N)]
maxs = 0
for i in range(N):
    temp = set()
    temp.add(c)
    for j in range(k):
        temp.add(sushi[i-N+j])
    maxs = max(maxs,len(temp))

print(maxs)
