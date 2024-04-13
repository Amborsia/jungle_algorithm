import sys
input = sys.stdin.readline


n = int(input())

arr = [float(input()) for _ in range(n)]

# NOTE 연속된 곱이 최대가 되는 부분 찾기

# 지금까지의 곱
# 지금자체가 더 크면 리셋
# 맥스로 비교

current_value = 1.0   # 누적 값
answer = 0.0
for i in range(n):
    temp = current_value * arr[i]   # 비교할 값 -> 누적값 * 현재값
    print('temp < arr[i]: ', temp, arr[i])
    if (temp < arr[i]):  # 비교할 값  < 현재값  -> 초기화
        current_value = arr[i]
        answer = max(answer, arr[i])
    else:  # 비교할값 > 현재값 -> 누적시키기
        print('arr[i]: ', arr[i])
        answer = max(answer, temp)
        current_value = temp
print("%.3f" % answer)
