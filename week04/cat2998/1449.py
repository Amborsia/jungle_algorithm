import sys

n, l = map(int, sys.stdin.readline().split())
tape_list = list(map(int, sys.stdin.readline().split()))

tape_list.sort()

tape_count = 0
tape_lenght = 0

for tape in tape_list:
    if (tape_lenght < tape):
        tape_lenght = tape - 0.5 + l
        tape_count += 1

print(tape_count)