

import sys
input = sys.stdin.readline

N = int(input())
lit = list(map(int,input().rstrip().split()))
answer = [[] for _ in range(N)]
cnt = 0

maxs = 0
temp = 0
for i in range(len(lit)):
    if temp < lit[i]:
        temp = lit[i]
        maxs = max(maxs,cnt)
        cnt = 0
    else:
        cnt += 1
print(max(maxs,cnt))