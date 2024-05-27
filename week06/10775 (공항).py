import sys


def solve(g: int, p: int, data: list[int]) -> int:
    gates = [-1] * (g + 1)
    answer = 0

    def _find(n: int):
        if gates[n] < 0:
            return n
        gates[n] = _find(gates[n])
        return gates[n]

    def _union(n, v):
        n, v = _find(n), _find(v)

        if n == v:
            return
        gates[v] = n

    for n in data:
        gate = _find(n)
        if gate == 0:
            return answer
        _union(gate - 1, gate)
        answer += 1
    return answer


if __name__ == '__main__':
    g = int(sys.stdin.readline())
    p = int(sys.stdin.readline())
    data = [int(sys.stdin.readline()) for _ in range(p)]
    print(solve(g, p, data))