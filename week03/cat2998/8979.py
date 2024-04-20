import sys

n, k = map(int, sys.stdin.readline().split())
l = [[-sys.maxsize, -sys.maxsize, -sys.maxsize, -sys.maxsize] for _ in range(n + 1)]

for i in range(n):
    i, a, b, c = map(int, sys.stdin.readline().split())
    l.append([i, a, b, c])

l.sort(key=lambda c: (-c[1], -c[2], -c[3]))

rank = 0
for i in range(n):
    rank += 1
    if l[i][0] == k:
        for j in range(i - 1, -1, -1):
            if l[i][1] == l[j][1] and l[i][2] == l[j][2] and l[i][3] == l[j][3]:
                rank -= 1
            else:
                break
        break

print(rank)