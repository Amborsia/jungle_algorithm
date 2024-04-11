import sys

input = sys.stdin.readline


def solve(n:int,k:int)->int:
    return n*n*k



if __name__ == '__main__':
    n,k = map(int,sys.stdin.readline().split())
    print(solve(n,k))
