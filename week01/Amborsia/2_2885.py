import sys
input = sys.stdin.readline

K = int(input().strip())
lit = [2**i for i in range(21)]
chocolate = 0
cnt = 0
for i in lit:
    if K <= i:
        chocolate = i
        break
temp = chocolate
if K != chocolate:
    while K:
        temp //=2
        if K >= temp:
            K = K-temp
            cnt += 1
        else:
            cnt += 1
print(chocolate, cnt)

