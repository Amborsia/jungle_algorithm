import sys


class fireball:
    x = 0
    y = 0
    m = 0
    d = 0
    s = 0

    def __init__(self, data: list[int]):
        self.x, self.y, self.m, self.s, self.d = data

    def __str__(self):
        return str([self.x, self.y, self.m, self.d, self.s])


def solve(n: int, fire_ball_cnt: int, k: int, data: list[list[int]]) -> int:
    d = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

    d_1 = [0, 2, 4, 6]
    d_2 = [1, 3, 5, 7]
    fireballs = []

    def _move(f: fireball, world_d: list[list[list[fireball]]]):
        f.x, f.y = f.x + f.s * d[f.d][0], f.y + f.s * d[f.d][1]
        while f.x > n:
            f.x = f.x - n
        while f.x <= 0:
            f.x = f.x + n
        while f.y > n:
            f.y = f.y - n
        while f.y <= 0:
            f.y = f.y + n
        world_d[f.x][f.y].append(f)

    def _sum(fires: list[fireball]):
        x = fires[0].x
        y = fires[0].y
        m = sum(map(lambda f: f.m, fires)) // 5
        s = sum(map(lambda f: f.s, fires)) // len(fires)
        if sum(map(lambda f: f.d % 2, fires)) % len(fires) == 0:
            d = d_1
        else:
            d = d_2
        if m <= 0: return
        nonlocal fireballs
        for _d in d:
            fireballs.append(fireball([x, y, m, s, _d]))

    for f in data:
        tmp = fireball(f)
        fireballs.append(tmp)

    for __ in range(k):
        world = [[[] for __ in range(n + 1)] for _ in range(n + 1)]
        for fire in fireballs:
            _move(fire, world)
        fireballs.clear()
        for w in world[1:]:
            for l in w[1:]:
                if len(l) >= 2:
                    _sum(l)
                elif len(l) == 1:
                    fireballs.append(l[0])

    return sum(map(lambda f: f.m, fireballs))


if __name__ == '__main__':
    n, m, k = map(int, sys.stdin.readline().split())
    data = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    print(solve(n, m, k, data))
