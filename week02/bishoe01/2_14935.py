import sys
input = sys.stdin.readline

n = input().strip()


def solve(n):
    x = len(n)
    temp = int(n[0]) * x
    if (temp == int(n)):  # int처리해줘야 비교가 가능
        print('FA')
        sys.exit()
    elif (len(n) == 1 and temp == n):
        print("NFA")
        sys.exit()
    else:
        solve(str(temp))


solve(n)
