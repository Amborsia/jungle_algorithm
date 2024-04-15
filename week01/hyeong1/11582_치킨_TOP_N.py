import sys

N = int(sys.stdin.readline())
yum = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())

sorted_yum = []
for i in range(0, N, N//K):
    arr = sorted(yum[i:i+N//K])
    sorted_yum += arr
for s in sorted_yum:
    print(s, end=" ")
