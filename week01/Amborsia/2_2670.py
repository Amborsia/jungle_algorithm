import sys
input = sys.stdin.readline

n=int(input())
lit=[]
dp=[]
for i in range(n):
    lit.append(float(input()))
    if i==0:
        dp.append(lit[0])
    else:
        dp.append(max(dp[i-1]*lit[i], lit[i]))

print('%.3f' % max(dp))