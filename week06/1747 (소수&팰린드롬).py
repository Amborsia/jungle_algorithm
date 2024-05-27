import sys


def solve(n:int)->int:
    def is_prime(n: int):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    while n == 1 or not (str(n) == str(n)[::-1] and is_prime(n)):
        n += 1
    return n

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(solve(n))