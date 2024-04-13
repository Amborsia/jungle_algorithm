import sys
input = sys.stdin.readline

count = int(input().strip())
dp = [0]*100
dp[0] = 1
dp[1] = 1
dp[2] = 1

for i in range(count):
    N = int(input())
    for j in range(3,N):
        
        dp[j] = dp[j-3]+dp[j-2]
    print(dp[N-1])


