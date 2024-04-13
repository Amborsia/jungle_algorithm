import sys


def solve(data: list) -> float:
    dp = data.copy()
    m = 0.0
    for i in range(1, len(dp)):
        dp[i] = max(dp[i], dp[i] * dp[i - 1])
        m = max(m, dp[i])
    return m


data = [float(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
print('%.3f' % solve(data))
