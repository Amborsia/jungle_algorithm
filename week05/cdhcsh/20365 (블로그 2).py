import sys


def solve(string: str) -> int:
    p = string[0]
    cnt = {'B': 0, 'R': 0}
    for c in string[1:]:
        if p != c:
            cnt[p] += 1
            p = c
    cnt[p] += 1
    return 1 + min(cnt.values())


if __name__ == '__main__':
    sys.stdin.readline()
    print(solve(sys.stdin.readline().strip()))
