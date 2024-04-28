import sys
from collections import deque
from copy import deepcopy


def solve(n: int, m: int, data: list[list[int]]) -> int:
    directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

    def _find(walls: set[tuple[int, int]]) -> int:
        visited = set()

        def _bfs(start: tuple[int, int]) -> int:
            nonlocal visited, walls
            queue = deque()
            queue.append(start)
            visited.add(start)
            cnt = 0
            flag = False
            while queue:
                x, y = queue.popleft()
                cnt += 1
                for d in directions:
                    nx, ny = x + d[0], y + d[1]
                    if not (0 <= nx < n and 0 <= ny < m): continue
                    pos = (nx, ny)
                    if data[nx][ny] == 2:
                        flag = True
                    if data[nx][ny] == 1 or pos in walls:
                        continue
                    if data[nx][ny] == 0 and pos not in visited:
                        visited.add(pos)
                        queue.append(pos)
            if flag : return 0
            else : return cnt

        answer = 0
        visited = set()
        for i in range(n):
            for j in range(m):
                pos = (i, j)
                if pos not in walls and pos not in visited and data[i][j] == 0:
                    answer += _bfs(pos)
        return answer

    target = set()
    checked = deepcopy(data)

    def _dfs(start: int) -> int:
        nonlocal target, checked
        if len(target) == 3:
            tmp = _find(target)
            # if tmp == 9:
            #     print(sorted(target),tmp);
            return tmp
        result = 0
        for num in range(start + 1, n * m):
            nx, ny = num // m, num % m
            if checked[nx][ny] == 0:
                checked[nx][ny] = 1
                target.add((nx, ny))
                result = max(result, _dfs(num))
                target.remove((nx, ny))
                checked[nx][ny] = 0
        return result

    return _dfs(-1)


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print(solve(n, m, arr))
