import sys

def solve(n: int, data: list[list[int]]) -> str:
    d = [[0, 1], [1, 0]]
    visited = set()
    def _dfs(pos: tuple[int, int])->bool:
        nonlocal  data, n
        x, y = pos
        if data[x][y] < 0:
            return True
        answer = False
        for _d in d:
            _pos = _x, _y = x + _d[0] * data[x][y], y + _d[1]*data[x][y]
            if 0 <= _x < n and 0 <= _y < n and data[_x][_y] != 'T' and _pos not in visited:
                visited.add(_pos)
                answer |= _dfs(_pos)
                visited.remove(_pos)
        return answer
    start = (0,0)
    visited.add(start)
    if _dfs(start):
        return 'HaruHaru'
    else:
        return 'Hing'


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    data = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    print(solve(n,data))
