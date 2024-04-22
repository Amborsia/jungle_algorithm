M, N = map(int, input().split())
# dict_num = [8, 5, 4, 9, 1, 7, 6, 3, 2, 0]
# answer = [0] * 100

string_nums = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
               5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
nums = {}
for i in range(M, N+1):
    num_str = ""
    for j in str(i):
        num_str += string_nums[int(j)]
        num_str += " "
    nums[i] = num_str
nums_sorted = sorted(nums.items(), key=lambda x: x[1])

cnt = 0
for n in nums_sorted:
    if cnt != 0 and cnt % 10 == 0:
        print()
    print(n[0], end=" ")
    cnt += 1

