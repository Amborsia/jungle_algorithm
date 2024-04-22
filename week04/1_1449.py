import sys
input = sys.stdin.readline

n, tape = map(int, input().split())
arr = sorted(list(map(int, input().split())))
answer = []
cnt = 0

tape -= 1  # NOTE - 0.5 간격을 위해서 -1 빼줌
for i in range(len(arr)):
    if (cnt == 0):
        cnt += 1
        std = arr[i]
    else:
        if ((arr[i] - std) <= tape):

            cnt += 1
        elif ((arr[i] - std) > tape):

            std = arr[i]
            answer.append(cnt)
            cnt = 1

answer.append(cnt)
print(len(answer))
