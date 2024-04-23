import sys

input = sys.stdin.readline


def ans():  # 스택 사용
    n = int(input())
    bongs = list(map(int, input().split()))
    stack = []
    res = 0
    max_ = bongs[0]
    for i in range(1, n):
        if bongs[i] < max_:
            stack.append(bongs[i])
        else:
            max_ = bongs[i]
            res = max(res, len(stack))
            stack.clear()

    res = max(res, len(stack))
    print(res)


def ans2():    # 그냥 cnt 사용
    n = int(input())
    bongs = list(map(int, input().split()))
    res = 0
    cnt = 0
    cur_max = bongs[0]
    for i in range(1, n):
        if bongs[i] < cur_max:
            cnt += 1
        else:
            cur_max = bongs[i]
            res = max(cnt, res)
            cnt = 0
    res = max(cnt, res)
    print(res)


ans2()
# ans()
