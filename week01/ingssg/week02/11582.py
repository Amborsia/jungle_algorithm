import sys

input = sys.stdin.readline


def ans():
    n = int(input())
    chickens = list(map(int, input().split()))
    k = int(input())
    result = []
    i = 0
    while i < n:
        temp = chickens[i:i + n//k]
        temp.sort()
        result.append(temp)
        i += n//k
    for i in range(k):
        for j in range(n//k):
            print(result[i][j], end=" ")


ans()
