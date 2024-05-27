import sys


def solve(a: int, k: int):
    dp = [k] * (k + 1)
    dp[k] = 0
    for i in range(k, a, -1):
        if i % 2 == 0:
            dp[i // 2] = min(dp[i // 2], dp[i] + 1)
        dp[i - 1] = min(dp[i - 1], dp[i] + 1)

    return dp[a]


if __name__ == '__main__':
    a, k = map(int, sys.stdin.readline().split())
    print(solve(a, k))
