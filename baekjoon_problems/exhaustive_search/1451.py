"""
https://nim-code.tistory.com/89

직접 직사각형을 잘라서 완전탐색으로 모두 탐색해본 후 최댓값을 출력하는 문제라는것은 파악했다.
다만 코드로 구현을 하지 못했다.. 위의 정답을 보면 직사각형을 나누는 경우는 6가지 경우가 있는데
해당 경우를 크기를 줄여가며 모두 확인해보면서 최댓값을 갱신하는 방식으로 풀이했다.

"""

import sys

# 세로, 가로
N, M = map(int, sys.stdin.readline().strip().split(" "))
array = [[0] * (M + 1) for _ in range(N + 1)]
max_value = 0

def get_sum(startx, starty, endx, endy):
    sum_num = 0
    for i in range(startx, endx + 1):
        for j in range(starty, endy + 1):
            sum_num += array[i][j]
            
    return sum_num

for i in range(N):
    nums = list(map(int, sys.stdin.readline().strip()))
    for j in range(len(nums)):
        array[i][j] = nums[j]
        
# 1번 모양
print("Case1")
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        square1 = get_sum(0, 0, i, M - 1)
        square2 = get_sum(i + 1, 0, j, M - 1)
        square3 = get_sum(j + 1, 0, N - 1, M - 1)
        print(f"[{i} {j}]", end="")
        print(f"{square1} {square2} {square3}")
        max_value = max(max_value, square1 * square2 * square3)

# 2번 모양    
print("Case2")    
for i in range(M - 2):
    for j in range(i + 1, M - 1):
        square1 = get_sum(0, 0, N - 1, i)
        square2 = get_sum(0, i + 1, N - 1, j)
        square3 = get_sum(0, j + 1, N - 1, M - 1)
        print(f"[{i} {j}]", end="")
        print(f"{square1} {square2} {square3}")
        max_value = max(max_value, square1 * square2 * square3)

# 3번 모양
print("Case3")
for i in range(M - 1, 0, -1):
    for j in range(N - 1):
        square1 = get_sum(0, i, N - 1, M - 1)
        square2 = get_sum(0, 0, j, i - 1)
        square3 = get_sum(j + 1, 0, N - 1, i - 1)
        print(f"[{i} {j}]", end="")
        print(f"{square1} {square2} {square3}")
        max_value = max(max_value, square1 * square2 * square3)

# 4번 모양
print("Case4")
for i in range(M - 1):
    for j in range(N - 1):
        square1 = get_sum(0, 0, N - 1, i)
        square2 = get_sum(0, i + 1, j, M - 1)
        square3 = get_sum(j + 1, i + 1, N - 1, M - 1)
        print(f"[{i} {j}]", end="")
        print(f"{square1} {square2} {square3}")
        max_value = max(max_value, square1 * square2 * square3)

# 5번 모양
print("Case5")
for i in range(N - 1):
    for j in range(M - 1):
        square1 = get_sum(0, 0, i, M - 1)
        square2 = get_sum(i + 1, 0, N - 1, j)
        square3 = get_sum(i + 1, j + 1, N - 1, M - 1)
        print(f"[{i} {j}]", end="")
        print(f"{square1} {square2} {square3}")
        max_value = max(max_value, square1 * square2 * square3)

# 6번 모양
print("Case6")
for i in range(N - 1, 0, -1):
    for j in range(M - 1):
        square1 = get_sum(i, 0, N - 1, M - 1)
        square2 = get_sum(0, 0, i - 1, j)
        square3 = get_sum(0, j + 1, i - 1, M - 1)
        print(f"[{i} {j}]", end="")
        print(f"{square1} {square2} {square3}")
        max_value = max(max_value, square1 * square2 * square3)
        
print(max_value)