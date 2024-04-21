K = int(input())
lines = []
for _ in range(6):
    d, length = map(int, input().split())
    lines.append([d, length])

max_w, max_h, w_idx, h_idx = 0, 0, 0, 0
for i in range(len(lines)):
    if lines[i][0] == 1 or lines[i][0] == 2:
        if max_w < lines[i][1]:
            max_w = lines[i][1]
            w_idx = i
    elif lines[i][0] == 3 or lines[i][0] == 4:
        if max_h < lines[i][1]:
            max_h = lines[i][1]
            h_idx = i

small_h = abs(lines[(w_idx - 1) % 6][1] - lines[(w_idx + 1) % 6][1])  # 인덱스가 5를 넘어갈 수 있어서 나머지 연산 사용함
small_w = abs(lines[(h_idx - 1) % 6][1] - lines[(h_idx + 1) % 6][1])
total = (max_w * max_h) - (small_w * small_h)
print(total * K)
