import sys
input = sys.stdin.readline

lit = ['zero','one','two','three','four','five','six','seven','eight','nine']

start,end = map(int,input().split())
answer_lit=[]
for i in range(start,end+1):
    if i>=10:
        answer_lit.append([str(lit[i//10]+lit[i%10]),i])
    else:
        answer_lit.append([str(lit[i]),i])

answer_lit = sorted(answer_lit)
#answer_lit.sort(key=lambda x: x[0], reverse=False)
for i in range(len(answer_lit)):
    if i>0 and i%10 == 0:
        print()
    print(answer_lit[i][1],end =' ')
   


