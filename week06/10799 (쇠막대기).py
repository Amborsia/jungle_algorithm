import sys

def solve(data:str)->int:
    stack = 0
    answer = 0
    prev = ' '
    for c in data:
        if c == '(':
            stack += 1
        else :
            stack -= 1
            if prev == '(':
                answer += stack
            else:
                answer += 1
        prev = c
    return answer

if __name__ == '__main__':
    string = sys.stdin.readline().strip()
    print(solve(string))