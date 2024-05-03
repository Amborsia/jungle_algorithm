import sys
from collections import deque
input = sys.stdin.readline
# 점프왕 쩰리 (Small)

dx, dy = [1, 0], [0, 1]

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]


def is_range(x, y):
    return 0 <= x < n and 0 <= y < n


stack = deque([])
stack.append([0, 0, grid[0][0]])
answer = False
while (stack):
    current_x, current_y, jump_range = stack.pop()
    if (grid[current_x][current_y] == -1):
        answer = True
        break
    visited[current_x][current_y] = True
    nx = current_x + jump_range
    ny = current_y + jump_range
    if (is_range(nx, current_y) and not visited[nx][current_y]):
        stack.append([nx, current_y, grid[nx][current_y]])
    if (is_range(current_x, ny) and not visited[current_x][ny]):
        stack.append([current_x, ny, grid[current_x][ny]])

print('HaruHaru') if answer else print("Hing")
