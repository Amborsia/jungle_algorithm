import sys

N, M = map(int, sys.stdin.readline().split())
P = [int(sys.stdin.readline()) for _ in range(M)]
P.sort()

max_profit = float('-inf')
max_price = 0
for i in range(M):
    sale = min(N, len(P[i:]))
    if max_profit < sale * P[i]:
        max_profit = sale * P[i]
        max_price = P[i]

print(max_price, max_profit)
