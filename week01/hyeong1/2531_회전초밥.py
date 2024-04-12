import sys
from collections import deque

N, d, k, c = map(int, sys.stdin.readline().split())
table = [int(sys.stdin.readline()) for _ in range(N)]

# 시간 초과 -> depth < N이 N, table[0:k]할 때 최악 N(k <= N) ==> 최악 O(N^2)
# event = []
# depth = 1
# lower_dup = 0  # 가장 중복이 적은 부분 집합 만들기
# while depth < N:
#     depth += 1
#     table = deque(table)
#     table.rotate(-1)
#     table = list(table)
#     new = table[0:k] + [c]
#     if lower_dup < len(set(new)):
#         lower_dup = len(set(new))
#         event.append(new)
#
# print(event)
# print(len(set(event[-1])))

# 투포인터, 슬라이딩 윈도우 띵킹..
count = 0

print(count)
