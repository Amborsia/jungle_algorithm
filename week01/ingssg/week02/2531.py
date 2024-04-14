import sys

input = sys.stdin.readline


def ans():
    # 접시 수, 초밥 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
    n, d, k, c = map(int, input().split())
    chobabs = [int(input()) for _ in range(n)]
    select = {}

    # print(n, d, k, c)
    # print(chobabs)
    # 쿠폰 선택하지 않는 경우 + 쿠폰
    max_set = 0


    for i in range(n):
        select_set = set()
        has_c = False

        for j in range(i, i + k):
            select_set.add(chobabs[j % n])
            if chobabs[j % n] == c:
                has_c = True
        if has_c:
            select_set.add(-1)
        max_set = max(max_set, len(select_set))
    print(max_set)


ans()
