import sys

input = sys.stdin.readline


n = int(input())

arr = list(map(int, input().split()))


answer = []
target = arr[0]
tmp = 0
for i in range(1, len(arr)):
    if (arr[i] < target):
        tmp += 1
        if (i == len(arr)-1):
            answer.append(tmp)
    else:
        answer.append(tmp)
        target = arr[i]
        tmp = 0


print(max(answer))
