import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())

idx = 0
div = n // k
for _ in range(k):
    l = arr[idx:idx + div]
    idx = idx + div
    l.sort()
    print(*l, end=" ")