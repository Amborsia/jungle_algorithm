import sys

def solve(n:int,data:list[int])->int:
    answer = 0
    p = 0
    for i in range(1,n):
        if data[p] < data[i]:
            answer = max(answer,i-p-1)
            p = i
    answer = max(answer,n-p-1)
    return answer

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    data = list(map(int,sys.stdin.readline().split()))
    print(solve(n,data))