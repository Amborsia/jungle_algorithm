import sys

input = sys.stdin.readline

n = int(input())

answer_arr = []
arr = [int(input()) for _ in range(n)]

arr.sort()
print('arr: ', arr)
std = arr[0]
cnt = 1

for i in range(1, n):
    if (abs(std-arr[i]) <= 4):
        # std = arr[i]  # 갱신해주기
        cnt += 1
    else:  # 5이상 차이날 때  리셋해주기
        answer_arr.append(cnt)
        if ((cnt >= 2) and abs(std-arr[i-1]) <= 4):
            # print('arr[i-1]: ', arr[i-1])
            # print('std: ', std)
            tmp = 1
            for k in range(1, cnt):  # 0 ,1, 2.. cnt
                if (abs(arr[i] - arr[i-k]) <= 4):
                    tmp += 1
            cnt = tmp
            std = arr[i-tmp+1]
        else:
            cnt = 1
            std = arr[i]

answer_arr.append(cnt)
# print('answer_arr: ', answer_arr)


print(5-max(answer_arr))
