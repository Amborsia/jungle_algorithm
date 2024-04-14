import sys

input = sys.stdin.readline


def ans():
    n, k = map(int, input().split())

    a = [0] * 9  # 9번째 자리수 까지 있음
    a[0] = 1
    a[1] = 10
    for i in range(2, 9):
        a[i] = a[i - 1] + 9 * i * 10 ** (i - 1)
    start = 0
    length = 0
    for j in range(9):
        if k >= a[j]:
            start = a[j]
            length = j + 1
    num = ((k - start) // length) + 10**(length-1) # 칸 + 자릿수 시작값
    if num > n:
        print(-1)
        return
    print(list(str(num))[(k - start) % length])


ans()
