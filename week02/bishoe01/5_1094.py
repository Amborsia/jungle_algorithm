
import sys
input = sys.stdin.readline

target = int(input())

print((bin(target)[2:]).count('1'))
