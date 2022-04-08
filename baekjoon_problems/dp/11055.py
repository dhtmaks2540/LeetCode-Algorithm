"""
수열 A가 주어졌을 때, 그 수열의 중가 부분 수열 중에서 합이 가장 큰 것을 구하라

해당 문제는 LIS의 응용 문제로, 가장 큰 합을 가진 LIS를 출력하는 문제이다.
우선 최장 증가 부분 수열의 길이를 구하는 문제는 dp 테이블에 현재 원소까지의
최장 수열의 길이를 저장한다면, 해당 문제는 최장 수열의 합을 저장하는 방식으로 풀 수 있다.

즉, 점화식은 현재 index의 값 이전에 값들 중 현재 값보다 작은 값들의 최댓값을 
dp[index]에 저장하도록 풀면 되므로 dp[index] = max(dp[:index] + dp[index], dp[index])가 된다.
"""

import sys

# 수열의 크기
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split(" ")))
# 중복되는 하위 문제들을 저장하기 위한 리스트
dp = [0] * (n + 1)

def lis_dp():
    for i in range(n):
        # 자기 자신
        dp[i] = array[i]
        # 증가되는 수열의 합 중 최댓값을 저장하는 변수
        max_value = 0
        for j in range(i):
            # i번째 이전의 모든 원소에 대해, 그 원소에서 끝나는 LIS 최댓값 확인
            if array[i] > array[j]:
                # 단, 이는 현재 수가 그 원소보다 클 때만 확인한다.
                max_value = max(max_value, dp[j])
            
        dp[i] = max(dp[i], dp[i] + max_value)
        
    print(max(dp))
                
lis_dp()