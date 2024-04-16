import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]


arr.sort(key=lambda x: (x[1], x[2], x[3]))


index_of_target = [arr[i][0] for i in range(n)].index(k)
tmp = []
for i in range(n):
    tmp.append(arr[i][0])

index_of_target = tmp.index(k)

for i in range(n):
    if (arr[index_of_target][1:] == arr[i][1:]):  # 먼저나오면 =그대로등수고  뒤에 나와도 괜찮네 같이 출력되니까
        print(i+1)
        break
