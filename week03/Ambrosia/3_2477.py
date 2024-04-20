import sys
input = sys.stdin.readline
N = int(input().strip())
lit = []
maxwidth = 0
width = 0
maxheight = 0
height = 0

for i in range(6):
    go, length = map(int, input().split())
    lit.append([go, length])
    if (length > maxheight) and (go == 4 or go == 3):
        maxheight = length
        height = i
    elif (length > maxwidth) and (go == 2 or go == 1):
        maxwidth = length
        width = i

temp_width = abs(lit[height - 1][1] - lit[(height + 1) % 6][1])
temp_height = abs(lit[width - 1][1] - lit[(width + 1) % 6][1])

print((maxheight * maxwidth - temp_width * temp_height) * N)
