"""
입력으로 주어진 두 문자열의 LCS의 길이를 출력하라

LCS 알고리즘은 Longest Common Subsequence와 Longest Common Substring 알고리즘으로 나뉘는데,
두 알고리즘의 풀이법은 약간만 다르다. 해당 문제는 Longest Common Subsequence 알고리즘으로 코드는
아래와 같다.
"""

import sys

# LCS 알고리즘의 편의성을 위해 앞에 '0'을 붙임
a = '0' + sys.stdin.readline().strip()
b = '0' + sys.stdin.readline().strip()

len_a = len(a)
len_b = len(b)

dp = [[0] * (1001) for _ in range(1001)]

for i in range(len_a):
    for j in range(len_b):
        # 첫 번째 행 또는 열에 해당한다면 0으로 초기화
        if i == 0 or j == 0:
            dp[i][j] = 0
        # 현재 비교하는 값이 서로 같다면 왼쪽 대각선의 값에 1 더하기
        elif a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        # 값이 서로 다르다면 왼쪽 혹은 위쪽의 값 중 최댓값 가져오기
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
print(dp[len_a - 1][len_b - 1])