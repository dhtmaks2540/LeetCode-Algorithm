"""
가능한 모든 쌍의 GCD의 합을 구하라

우선 가능한 쌍을 구하기 위해서 itertools의 combinations 라이브러리를 사용하여 조합을 구했다.
그 후 유클리드 호제법을 사용해 해당 조합의 최대 공약수를 구해주면서 더해주는 방식으로 풀이했다.
"""

import sys
import itertools

# 유클리드 호제법을 이용한 최대 공약수 구하기
def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a % b)
    
T = int(sys.stdin.readline())

for _ in range(T):
    # 수
    array = list(map(int, sys.stdin.readline().split(" ")))[1:]
    result = 0
    for nums in list(itertools.combinations(array, 2)):
        result += gcd(nums[0], nums[1])
        
    if result == 0:
        print(1)
    else:      
        print(result)