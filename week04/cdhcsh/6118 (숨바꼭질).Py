import sys
from collections import deque


def solve(n: int, data: list[list[int]]) -> list[int]:
    nodes = [[] for _ in range(n + 1)]
    for s, e in data:
        nodes[s].append(e)
        nodes[e].append(s)

    visited = [0] * (n + 1)
    cnt = [0] * (n + 1)
    max_dist = 0
    min_node = n + 1

    def _bfs(start: int):
        nonlocal visited
        queue = deque()
        visited[start] = 1
        queue.append(start)
        while queue:
            node = queue.popleft()
            for t in nodes[node]:
                if visited[t] == 0:
                    visited[t] = visited[node] + 1
                    _check(t)
                    queue.append(t)

    def _check(node: int) -> None:
        nonlocal max_dist, min_node, visited
        dist = visited[node] - 1
        cnt[dist] += 1
        if max_dist < dist:
            max_dist = dist
            min_node = node
        if max_dist == dist and min_node > node:
            min_node = node
    _bfs(1)
    return [min_node, max_dist,cnt[max_dist]]

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    print(*solve(n, arr))
