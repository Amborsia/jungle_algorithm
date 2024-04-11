import sys
input = sys.stdin.readline
N = input()

before = 0
# while len(N)>0:
#     N = len(N)*int(N[0])
#     if before != int(N):
#         before = int(N)
#     else:
#         print("FA")
#         break

def func(value):
    temp = (len(N)-1)*int(N[0])
    
    if temp == value:
        print("FA")
        return
    else:
        func(temp)
func(N)