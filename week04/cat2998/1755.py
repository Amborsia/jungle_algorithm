import sys

m, n = map(int, sys.stdin.readline().split())
number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
l = []

for i in range(m, n + 1):
    s = str(i)
    s_str = ""
    for j in range(len(s)):
        s_str += number[int(s[j])]
    l.append((s_str, i))

l.sort()
for i in range(len(l)):
    if i != 0 and i % 10 == 0:
        print()
    print(l[i][1], end=" ")