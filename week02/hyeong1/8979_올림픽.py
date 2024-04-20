import sys

N, K = map(int, sys.stdin.readline().split())

# 45점
# info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# info.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
# for i in range(N):
#     if info[i][0] == K:
#         if info[i][1:] == info[i-1][1:]:
#             print(i)
#             break
#         else:
#             print(i+1)
#             break

gold, silver, bronze = [0] * (N+1), [0] * (N+1), [0] * (N+1)
medals = {}
for i in range(N):
    idx, g, s, b = map(int, sys.stdin.readline().split())
    medals[idx] = (g, s, b)

K_medals = medals[K]

cnt = 1
for n, n_medals in medals.items():
    if n != K:
        if n_medals > K_medals:
            cnt += 1

print(cnt)
