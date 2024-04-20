import sys

k = int(sys.stdin.readline())
l = [int(sys.stdin.readline().split()[1]) for _ in range(6)]

height = max(max(l[0], l[2]), l[4])
lenght = max(max(l[1], l[3]), l[5])

idx = l.index(height)
small_height = abs(l[idx - 1] - l[(idx + 1) % 6])
idx = l.index(lenght)
small_lenght = abs(l[idx - 1] - l[(idx + 1) % 6])

total = height * lenght - small_height * small_lenght
print(total * k)