"""
총 점수의 최댓값을 구하라

https://mygumi.tistory.com/100
https://kwanghyuk.tistory.com/4

마지막 칸을 무조건 밟아야 한다는 조건이 있기에 마지막 계단을 밟았을 경우

1. 마지막 계단 전의 계단을 밟은 경우 -> 마지막 전전칸의 계단을 밟지 못한다. 조건 중 3개의 계단을
연속으로 밟지 못하기 때문이다.
(?, ?, ?, ?, o, o)라고 할 때 마지막 전의 계단은 밟았으므로 그 전의 계단은 밟지 못하기에 x로 표시하고
그렇다면 전전전칸을 밟는 경우를 추가하여 (?, ?, o, x, o, o)로 표현할 수 있다.

2. 마지막 계단 전의 계단을 밟지 않은 경우 -> 마지막 전전 계단을 밟은 경우이다.
즉 마지막 전전 계단을 밟고 마지막 칸을 밟으면 마지막 전 계단을 
밟지 않은 경우이기에 (?, ?, ?, o, x, o)와 같이 표현할 수 있다.

따라서 이를 점화식으로 나타내면
1. 전전칸을 밟고 현재 칸을 밟은 경우 -> 전전칸까지의 최대값 + 현재칸 -> dp[n] = dp[n-2] + stair[n]
2. 전칸을 밟고 현재 칸은 밟은 경우 -> 전전전칸까지의 최대값 + 전칸 + 현재칸 -> dp[n] = dp[n-3] + stair[n-1] + stair[n] 
"""

def solution():
    import sys
    
    # 계단의 개수
    n = int(input())
    # 계단의 점수
    scores = [0] * 301
    for i in range(n):
        scores[i] = int(sys.stdin.readline())

    dp = [0] * (301)
    # dp[0]은 1칸을 갔을 경우로 1가지만 존재
    dp[0] = scores[0]
    # dp[1]은 2 칸을 갔을 경우로 max값은 1가지
    dp[1] = scores[0] + scores[1]
    # dp[2]는 3 칸을 갔을 경우
    dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])
    
    for i in range(3, n):
        # 점화식
        # 전전전칸의 최댓값 + 전칸 밟고 현재칸 또는
        # 전전칸의 최댓값 + 현재칸 중 최댓값을 가져오는 점화식
        dp[i] = max(dp[i - 3] + scores[i - 1], dp[i - 2]) + scores[i]
        
    print(dp[n - 1])
    
solution()