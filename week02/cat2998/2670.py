import sys

n = int(sys.stdin.readline())
arr = [0.0 for _ in range(n)]
dp = [0 for _ in range(n)]

for i in range(n):
    arr[i] = float(sys.stdin.readline())

dp[0] = arr[0]
for i in range(1, n):
    dp[i] = max(dp[i - 1] * arr[i], arr[i])

print('%.3f' % max(dp))