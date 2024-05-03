import sys
input = sys.stdin.readline

N = int(input().strip())
lit = []
for i in range(N):
    lit.append(int(input().strip()))
lit.sort()
start = -1
maxs = 10
for i in range(N):
    if start == -1:
        start = i
    
    temp = 0
    for j in range(start,N):
        if abs(lit[start]- lit[j])>=5:
            start = -1
            break
        else:
            temp += 1
    maxs = min(maxs,5-temp)
# 1 (2) 3 (4 5 6) 7 8 (9 10 11) 12
print(maxs)
                


# lit.sort()
# temp = lit[0]
# maxs = 0
# temp_cnt = 0
# for i in range(1,len(lit)):
#     if lit[i] -1 ==temp:
#         temp_cnt += 1
#         temp = lit[i]
#     else:
#         maxs = max(maxs,temp_cnt)
#         temp_cnt = 0
# print(max(maxs,temp_cnt))
