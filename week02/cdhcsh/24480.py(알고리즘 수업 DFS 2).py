import sys

sys.setrecursionlimit(10**8)


def solve(n: int, m: int, start: int, data: list[list[int]]) -> list:
    def _dfs(node: int, num: int):
        nonlocal nodes, visited
        visited[node] = num
        for child in nodes[node]:
            if visited[child] == 0:
               num = _dfs(child, num+1)
        return num
    visited = [0] * n
    nodes = [[] for _ in range(n)]
    for s, e in data:
        nodes[s - 1].append(e - 1)
        nodes[e - 1].append(s - 1)
    [node.sort(key=lambda i: -i) for node in nodes]

    _dfs(start - 1, 1)
    return visited


if __name__ == '__main__':
    n, m, s = map(int, sys.stdin.readline().split())
    data = [list(map(int, sys.stdin.readline().split())) for i in range(m)]
    print(*solve(n, m, s, data), sep='\n')
