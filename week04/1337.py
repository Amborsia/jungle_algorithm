import sys

input = sys.stdin.readline


def ans():
    n = int(input())
    data = [int(input()) for _ in range(n)]
    data.sort()

    cnts = []
    for i in range(n):
        cnt = 0
        for j in range(data[i], data[i] + 5):
            if j not in data[i:i+5]:
                cnt += 1
        cnts.append(cnt)

    print(min(cnts))


ans()
