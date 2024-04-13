import sys


def solve(order: list) -> list:
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    for i in range(6, len(dp)):
        dp[i] = dp[i-1] + dp[i-5]

    result = []
    for o in order:
        result.append(dp[o])

    return result


if __name__ == '__main__':
    order = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
    print(*solve(order),sep='\n')
