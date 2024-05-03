import sys
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())

p = [int(input()) for _ in range(m)]

std = deepcopy(p)
std.sort(reverse=True)

cnt = 0
answer = []
while (std):
    price = std.pop()
    tmp = 0
    cnt = n
    for element in p:
        if (element >= price and cnt > 0):
            tmp += price
            cnt -= 1

    answer.append((price, tmp))


answer.sort(key=lambda x: x[1])

print(answer[-1][0], answer[-1][1])
