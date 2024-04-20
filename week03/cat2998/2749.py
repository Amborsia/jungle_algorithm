import sys

n = int(sys.stdin.readline())

mod = 1000000
fibo = [0, 1]
p = 15 * (10**5) # p = 15 * 10^(k - 1), k는 나머지 10^k 의 k

# 피보나치 수를 K로 나눈 나머지는 항상 주기를 갖게 되는데 이를 피사노 주기라고 한다.
# 주기의 길이가 P 이면, n번째 피보나치 수를 M으로 나눈 나머지는 n%P번째 피보나치 수를 M을 나눈 나머지와 같다.
for i in range(2, p):
    fibo.append(fibo[i - 1] + fibo[i - 2])
    fibo[i] %= mod

print(fibo[n % p])