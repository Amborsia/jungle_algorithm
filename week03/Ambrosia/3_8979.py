import sys
input = sys.stdin.readline

N,M = map(int,input().split())
lit = [[]for i in range(N)]
for i in range(N):
    flag,gold,silver,bronze = map(int,input().split())
    lit[i] = [flag,gold,silver,bronze]
    
lit.sort(key = lambda x: (x[1],x[2],x[3]),reverse=True)
temp = [lit[0][1],lit[0][2],lit[0][3]]
cnt = 1
temp_cnt = 0
if lit[0][0] == M:
    print(1)
else:
    for i in range(1,len(lit)):
        temp2 = [lit[i][1],lit[i][2],lit[i][3]]
        if temp != temp2:
            temp = temp2
            cnt+=1+temp_cnt
            temp_cnt = 0
        else:
            temp_cnt += 1
        if lit[i][0] == M:
            print(cnt)
            break

