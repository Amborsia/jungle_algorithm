import sys

N = int(sys.stdin.readline())
arrows = list(map(int, sys.stdin.readline().split()))
max_count = 0
high = 0

for i in range(N):
    count = 0
    if arrows[i] >= high:
        high = arrows[i]
        for j in range(i+1, N):
            if arrows[i] > arrows[j]:
                count += 1
            else:
                break
        max_count = max(max_count, count)

print(max_count)
