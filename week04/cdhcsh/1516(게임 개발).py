import sys
from collections import deque


def solve(n: int, data: list[list[int]]) -> list[int]:
    nodes = [set() for _ in range(n + 1)]
    build_time = [0] * (n + 1)
    require_time = [0] * (n + 1)
    in_degree = deque()
    for i, d in enumerate(data):
        i += 1
        build_time[i] = d[0]
        if d[1] < 0:
            in_degree.append(i)
        else:
            for j in range(1, len(d) - 1):
                nodes[i].add(d[j])
    while in_degree:
        require = in_degree.popleft()
        for current in range(1, n + 1):
            if require in nodes[current]:
                require_time[current] = max(require_time[current], build_time[require] + require_time[require])
                nodes[current].remove(require)
                if not nodes[current]:
                    in_degree.append(current)
    return [(build_time[i] + require_time[i]) for i in range(1, n + 1)]


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print(*solve(n, arr), sep='\n')
