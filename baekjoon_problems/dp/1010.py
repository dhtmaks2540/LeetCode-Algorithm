"""
다리를 지을 수 있는 경우의 수를 구하라

해당 문제는 겹치지 않고 서쪽과 동쪽의 다리를 연결하는 문제로
순서를 상관하지 않고 다리를 놓는 경우의 수인 조합에 해당한다.
따라서 nCm(n = 서쪽, m = 동쪽)의 값을 구하는 문제로 풀이할 수 있고,
nCm = n-1Cm-1 + n-1Cm과 같은 공식이 나오기에 이를 테이블에 저장하는 방식으로 풀이한다.
즉, 하위의 중복되는 값을 저장하는 다이나믹 프로그래밍으로 해당 문제를 풀이할 수 있다.
"""

# 조합 공식 사용해서 풀이
def solution():
    import sys

    # 테스트 케이스
    T = int(input())
    # 서쪽과 동쪽에 있는 사이트의 개수
    array = []

    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split(" "))
        array.append((N, M))
        
    def factorial(n):
        if n == 0:
            return 1
        
        return n * factorial(n - 1)

    def combination(n, m):
        return factorial(n) / (factorial(n - m) * factorial(m))

    for nums in array:
        print(int(combination(nums[1], nums[0])))
        
# 조합 공식 + 다이나믹 프로그래밍 사용
def solution2():
    import sys
    
    # 테스트 케이스
    T = int(input())
    # 서쪽과 동쪽에 있는 사이트 개수
    array = []
    
    for _ in range(T):
        n, m = map(int, sys.stdin.readline().split(" "))
        array.append((n, m))
    
    # 서로 다른 M개 중에서 N개 뽑기
    def combination(n, m):
        # 이미 풀었던 문제라면 바로 return
        if dp[n][m] > 0:
            return dp[n][m]
        
        if n == m or n == 0:
            dp[n][m] = 1
            return dp[n][m]
        
        dp[n][m] = combination(n - 1, m - 1) + combination(n, m - 1)
        
        return dp[n][m]
        
    for n, m in array:
        # 중복되는 값을 저장하기 위한 테이블
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        result = combination(n, m)
        print(result)
        
solution2()