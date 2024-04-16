import sys

input = sys.stdin.readline


n, k = map(int, input().split())

print(int(k*n**2))
