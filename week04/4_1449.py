import sys
input = sys.stdin.readline

n,l = map(int,input().split())
lit = list(map(int,input().split()))
lit.sort()

start = -1
cnt = 1
for i in range(n):
    if start == -1:
        start = i
    else:
        if abs(lit[start]-lit[i]) >= l:
            start = i
            cnt += 1

print(cnt)
