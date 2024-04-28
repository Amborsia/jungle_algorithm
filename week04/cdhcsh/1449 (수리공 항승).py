import sys


def solve(holes: list[int], length: int) -> int:
    holes.sort()
    last = holes[0]
    answer = 1;
    for i in range(1, len(holes)):
        if (last + length - 1) < holes[i]:
            answer += 1
            last = holes[i]
    return answer


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    print(solve(arr, m))
