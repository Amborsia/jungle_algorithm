import sys


def solve(n: int, m: int, k: int, data: list[str]) -> int:
    d = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    result = [[0] * m for _ in range(n)]
    visited = set()
    def _dfs(len: int, pos: tuple[int, int]):
        nonlocal result,data, n, m, k
        x, y = pos
        if len == k:
            result[x][y] += 1
            return
        for _d in d:
            _pos = _x, _y = x + _d[0], y + _d[1]
            if 0 <= _x < n and 0 <= _y < m and data[_x][_y] != 'T' and _pos not in visited:
                visited.add(_pos)
                _dfs(len + 1, _pos)
                visited.remove(_pos)

    visited.add((n-1,0))
    _dfs(1, (n - 1, 0))
    return result[0][m - 1]


if __name__ == '__main__':
    n, m, k = map(int, sys.stdin.readline().split())
    data = [sys.stdin.readline() for _ in range(n)]
    print(solve(n, m, k, data))
