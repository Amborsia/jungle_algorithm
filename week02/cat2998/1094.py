import sys

x = int(sys.stdin.readline())

cnt = 0
while x > 0:
    cnt += (x & 1)
    x >>= 1

print(cnt)