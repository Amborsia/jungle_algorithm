import sys

k = int(sys.stdin.readline())

first_bit = last_bit = -1
bit = 0

while k > 0:
    if (k & 1) and first_bit == -1:
        first_bit = bit
    if (k & 1):
        last_bit = bit
    bit += 1
    k >>= 1

if first_bit == last_bit:
    print(pow(2, last_bit), end=" ")
    print(0)
else:
    print(pow(2, (last_bit + 1)), end=" ")
    print(last_bit - first_bit + 1)