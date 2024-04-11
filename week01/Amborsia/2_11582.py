import sys
input = sys.stdin.readline

N = int(input().strip())
lit = list(map(int,input().split()))
k = int(input().strip())

index = N//k
temp = []

for i in range(0,N,index):
    arr = lit[i:i+index]
    arr.sort()
    temp.append(arr)

for i in range(len(temp)):
    print(*temp[i], end = ' ')