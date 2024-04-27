import sys


def solve(data: list) -> int:
    data.sort()
    n = len(data)
    M = 5
    answer = M
    for i in range(n):
        for j in range(i + 1,n):
            if data[i] + M <= data[j]:
                cnt = j-i
                break
        else:
            cnt = n-i
        answer = min(answer, M - cnt)
    return answer


if __name__ == '__main__':
    arr = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
    print(solve(arr))
