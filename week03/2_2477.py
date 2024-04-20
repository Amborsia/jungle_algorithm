import sys

input = sys.stdin.readline


n = int(input())
# arr = [list(map(int, input().split())) for _ in range(6)]

r = [[] for _ in range(5)]

# 큰사각형 - 작은사각형

arr = [list(map(int, input().split())) for _ in range(6)]


max_standard = arr[0][1]
index = 0
for i in range(len(arr)):
    if (arr[i][1] > max_standard):
        max_standard = arr[i][1]
        index = i
max_w = 0
max_h = 0
rest_w = 0
rest_h = 0


max_w = max((arr[(index+1) % 6][1]), (arr[(index-1) % 6][1]))
rest_w = abs(arr[(index-1) % 6][1] - arr[(index+1) % 6][1])

print("__________", index)
find_index = ((index-1) % 6) if ((arr[(index-1) % 6][1])
                                 > (arr[(index+1) % 6][1])) else ((index+1) % 6)

index = find_index
print("find_indexfind_index", index)

max_h = max((arr[(index+1) % 6][1]), (arr[(index-1) % 6][1]))
rest_h = abs((arr[(index+1) % 6][1]) - (arr[(index-1) % 6][1]))

# print('rest_w: ', rest_w)
# print('rest_h: ', rest_h)

print(n * ((max_w * max_h) - (rest_w*rest_h)))
