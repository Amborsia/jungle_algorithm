import sys
input = sys.stdin.readline

N = int(input().strip())
lit = [64,32,16,8,4,2,1]
count = 0
for i in lit:
    if N-i >= 0:
        N-=i
        count += 1

print(count)

