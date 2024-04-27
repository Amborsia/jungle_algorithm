import sys

strs = ['zero','one','two','three','four','five','six','seven','eight','nine']

def solve(n:int,m:int)->list:
    def _convert(num:int)->str:
        answer = ''
        while num > 0:
            answer = strs[num%10] + answer
            num //= 10
        return answer

    arr = list(range(n,m+1))
    arr.sort(key=_convert)
    return arr

if __name__ == '__main__':
    n,m = map(int,sys.stdin.readline().split())
    answer = solve(n,m)
    for i in range(len(answer)):
        print(answer[i],end=' ')
        if i > 1 and (i+1)%10 == 0:
            print()