"""
a, b, c가 주어졌을 때, w(a,b,c)를 출력하는 프로그램을 작성

3차원 리스트를 통해 중복되는 값을 저장하는 다이나믹 프로그래밍 문제로,
3차원 리스트를 만드는 방법과 중복되는 값을 저장하고 출력하는 조건을 작성할 수 있으면
풀 수 있는 문제이다.
"""

import sys

def recursive(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return recursive(20, 20, 20)
    
    # 값이 기록되어 있다면 바로 return
    if dp[a][b][c] != 0:
        return dp[a][b][c]
    
    # 중복된 하위값 저장
    if a < b and b < c:
        dp[a][b][c] = recursive(a, b, c - 1) + recursive(a, b - 1, c - 1) - recursive(a, b - 1, c)
    else:
        dp[a][b][c] = recursive(a - 1, b, c) + recursive(a - 1, b - 1, c) + recursive(a - 1, b, c - 1) \
            - recursive(a - 1, b - 1, c - 1)
            
    return dp[a][b][c]

# 중복되는 하위값을 저장하기 위한 리스트(3차원 리스트)
dp = [[[0 for x in range(51)] for y in range(51)]for z in range(51)]
print(dp)

while True:
    a, b, c = map(int, sys.stdin.readline().split(" "))
    
    if a == -1 and b == -1 and c == -1:
        break
    
    print(f"w({a}, {b}, {c}) = {recursive(a, b, c)}")