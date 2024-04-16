import sys
input = sys.stdin.readline

n = int(input())
c = list(map(int, input().split()))
k = int(input())

people = n // k   # 그 만큼 크게 정렬
arr = []
for chicken in range(0, n, people):
    arr = c[chicken:chicken+people]
    arr.sort()
    for element in arr:
        print(element, end=' ')
