test_case = int(input())

for _ in range(test_case):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif ((r1 + r2) ** 2 < dist) or ((abs(r1 - r2) ** 2) > dist):
        print(0)
    elif ((r1 + r2) ** 2 == dist) or ((abs(r1 - r2) ** 2) == dist):
        print(1)
    elif (abs(r1 - r2) ** 2) < dist < (abs(r1 + r2) ** 2):
        print(2)
