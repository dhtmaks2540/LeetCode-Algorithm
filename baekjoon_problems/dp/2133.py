"""
3 * N 크기의 벽을 2 * 1, 1 * 2 크기의 타일로 채우는 경우의 수를 구하라

타일을 채우는 경우의 수를 구하는 문제인데, 타일을 채우는 경우의 수가 굉장히 많으며
중복되서 사용되기에 다인나믹 프로그래밍으로 문제를 풀이할 수 있다.
"""

def wrong_solution():
    # 타일의 가로 수
    N = int(input())
    # 중복되는 값을 기록하기 위한 dp 테이블
    dp = [[0] * (2) for _ in range(31)]
    # 3 * 2를 만드는 경우의 수는 3가지
    dp[2][0] = 3
    dp[2][1] = 0
    # 3 * 4을 만드는 경우의 수는 11가지
    dp[4][0] = 9
    dp[4][1] = 2 

    for i in range(6, N + 1):
        if i % 4 == 0:
            dp[i][0] = dp[i - 2][0] * 3
            dp[i][1] = dp[i - 2][1] * 3 * 2
        else:
            dp[i][0] = dp[i - 2][0] * 3
            dp[i][1] = dp[i - 2][1] * 3 * 2
        
    print(sum(dp[N]))

"""
https://kosaf04pyh.tistory.com/236
https://t-anb.tistory.com/28

그림에서 주어지는 경우를 파악하며 그림을 그려가며 점화식을 도출하는게 중요하다..!!
즉, 특이 케이스를 잘 생각해서 점화식을 도출하는 과정이 중요
"""


def solution():
    N = int(input())
    dp = [0] * 31
    dp[0] = 1
    dp[2] = 3
    
    for i in range(4, N + 1):
        dp[i] = dp[i - 2] * 3
        for j in range(4, i + 1, 2):
            dp[i] += dp[i - j] * 2
            
    print(dp[N])
solution()