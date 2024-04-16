import sys
from decimal import Decimal

N = int(sys.stdin.readline())
floats = [Decimal(sys.stdin.readline()) for _ in range(N)]

for i in range(1, N):
    floats[i] = max(floats[i], floats[i] * floats[i-1])

print("%0.3f" % max(floats))

# 완탐 -실패
# _max = floats[0]
# for i in range(N):
#     tmp = floats[i]
#     for j in range(i+1, N):
#         tmp *= floats[j]
#         _max = max(_max, tmp)
#     _max = max(_max, tmp)
#
