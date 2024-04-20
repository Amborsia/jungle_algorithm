import sys

def f(x):
    return int(str(x)[0]) * int(len(str(x)))

x = int(sys.stdin.readline())

flag = 0
while x :
    if (x == f(x)):
        flag = 1
        break
    x = f(x)
