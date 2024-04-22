from sys import stdin

N = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(N)]
arr.sort()

answer = 4
for i in range(N):
    for j in range(N-1, 0, -1):
        if arr[j] - arr[i] <= 4:
            answer = min(answer, 5 - (j - i + 1))

print(answer)
