m, n = map(int, input().split())

dic = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
       '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'}

arr = [i for i in range(m, n+1)]  # m 부터 n까지 담아주기
answer = []
for element in arr:
    tmp = ''.join(dic[k] for k in str(element))
    answer.append((element, tmp))
answer.sort(key=lambda x: x[1])

for i in range(len(answer)):
    if (i % 10 == 0 and i != 0):
        print()
    print(answer[i][0], end=' ')
