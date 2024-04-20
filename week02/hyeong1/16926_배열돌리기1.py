import sys

N, M, R = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = [[0] * M for _ in range(N)]


def _rotate(array):
    rotated_array = array[R % len(array):] + array[:R % len(array)]
    return rotated_array


for i in range(min(N, M) // 2):
    row, col = N - (2 * i), M - (2 * i)
    temp = []

    for c in range(col):  # 위
        temp.append(arr[i][i + c])
    for r in range(1, row + 1):  # 오른쪽
        temp.append(arr[i + r][i + col - 1])
    for c in range(col - 1, -1, -1):  # 아래
        temp.append(arr[i + row - 1][i + c])
    for r in range(row - 2, 0, -1):  # 왼쪽
        temp.append(arr[i + r][i])

    temp = _rotate(temp)
    idx = 0

    for c in range(col):  # 위
        arr[i][i + c] = temp[idx]
        idx += 1
    for r in range(1, row - 1):  # 오른쪽
        arr[i + r][i + col - 1] = temp[idx]
        idx += 1
    for c in range(col - 1, -1, -1):  # 아래
        arr[i + row - 1][i + c] = temp[idx]
        idx += 1
    for r in range(row - 2, 0, -1):  # 왼쪽
        arr[i + r][i] = temp[idx]
        idx += 1

for a in arr:
    print(*a)
