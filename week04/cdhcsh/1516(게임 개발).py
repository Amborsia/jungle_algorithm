import sys
from collections import deque


def solve(n:int,data:list[list[int]])->list[int]:
    nodes = [set() for _ in range(n+1)]
    base_time = [0] * (n+1)
    add_time = [0] * (n+1)
    in_degree = deque()
    for i,d in enumerate(data):
        i += 1
        base_time[i] = d[0]
        if d[1] < 0 : in_degree.append(i)
        else:
            for j in range(1,len(d)-1):
                nodes[i].add(d[j])
    while in_degree:
        node = in_degree.popleft()
        for i in range(1,n+1):
            if node in nodes[i]:
                add_time[i] = max(add_time[i],base_time[node]+add_time[node])
                nodes[i].remove(node)
                if not nodes[i]:
                    in_degree.append(i)
    return[(base_time[i] + add_time[i]) for i in range(1,n+1)]





if __name__ == '__main__':
    n = int(sys.stdin.readline())
    data = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    print(*solve(n,data),sep='\n')