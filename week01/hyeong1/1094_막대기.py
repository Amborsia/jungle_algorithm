x = int(input())

sticks = [64, 32, 16, 8, 4, 2, 1]
count = 0

# 그리디
# for i in range(len(sticks)):
#     if x >= sticks[i]:
#         x -= sticks[i]
#         count += 1
#     if x == 0:
#         break

# 비트 마스킹
for i in range(7):
    if (x & (1 << i)) > 0:  # i번째 비트가 1인지 확인
        count += 1

print(count)
