R, C, K = map(int, input().split())
_map = [list(map(str, input())) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
cnt = 0
print(*_map)

start, end = [R - 1, 0], [0, C - 1]


def recursive(pos, dist):
    global cnt, end
    # 현재 좌표가 end면 종료
    if pos == end:
        if dist == K:
            cnt += 1
        return
    if not visited[pos[0]][pos[1]]:
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            new_pos = [pos[0] + dr, pos[1] + dc]
            if 0 <= new_pos[0] < R and 0 <= new_pos[1] < C and _map[new_pos[0]][new_pos[1]] != 'T':
                visited[pos[0]][pos[1]] = True
                recursive(new_pos, dist + 1)
                visited[pos[0]][pos[1]] = False


recursive(start, 1)
print(cnt)
