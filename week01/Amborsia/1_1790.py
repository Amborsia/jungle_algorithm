import sys
input = sys.stdin.readline
lit = [0]*10
N,M = map(int,input().split())
ans = 0
number = 1
nine = 9
# 실행하면서 9 180 2700 이런식으로 계속해서 빼줌
while M > number*nine:
    M = M-(number*nine)
    ans = ans + nine
    number+=1
    nine = nine*10

# 20 23이라면 ans에는 9, M에는 23에서 9를 뺀 숫자가 들어갈거임
#그러면 ans는 스트링의 총 길이값이 되어버림 
ans = (ans+1)+(M-1) // number
if ans>N:
    print(-1)
else:
    # ans는 몇번인지가 나옴
    # (순서-1) //자릿수 이렇게 하면 이 숫자의 몇번째 값인지가 나옴
    print(str(ans)[(M-1)%number])
