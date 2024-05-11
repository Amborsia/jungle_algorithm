import sys

N = int(sys.stdin.readline())
colors = list(map(str, sys.stdin.readline()))
colors = colors[:len(colors)-1]

b_cnt, r_cnt = 0, 0
for c in colors:
    if c == 'B':
        b_cnt += 1
    elif c == 'R':
        r_cnt += 1

small_c = ''
if b_cnt > r_cnt:
    small_c = 'R'
else:
    small_c = 'B'

small_cnt = 0
for i in range(len(colors)):
    if i < len(colors) and colors[i] == small_c:
        if colors[i-1] == small_c:
            continue
        small_cnt += 1

print(small_cnt + 1)
