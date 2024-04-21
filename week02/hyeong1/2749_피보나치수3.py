import sys

N = int(sys.stdin.readline())
MAX = 15 * (10 ** 5)  # 피사노 주기
dp = [0] * MAX
dp[0] = 0
dp[1] = 1

for i in range(2, MAX):
    dp[i] = (dp[i-1] + dp[i-2]) % 1000000

print(dp[N % MAX])
