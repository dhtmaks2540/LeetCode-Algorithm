"""
두 수 A,B 가 주어졌을 때 최소 공배수를 구하라

https://coding-factory.tistory.com/599

최대 공약수는 유클리드 호제법을 사용해서 구할 수 있다. 유클리드 알고리즘은
2개의 자연수의 최대공약수를 구하는 알고리즘이다. 비교대상의 두 개의 자연수 a와 b에서(단 a > b)
a를 b로 나눈 나머지를 r이라고 했을 때 GCD(a, b) = GCD(b, r)과 같고 "r이 0이면 그때 b가 최대 공약수
이다" 라는 원리를 활용한 알고리즘이다.
ex) GCD(24, 16) -> GCD(16, 8) -> GCD(8, 0) : 최대공약수 = 8
"""

import sys
        
# 유클리드 호제법을 이용
def solution():
    # 시간복잡도 O(logN)
    # 최대 공약수
    def gcd(a, b):
        if b == 0: return a
        else: return gcd(b, a % b)
    
    # 최소 공배수
    def lcm(a, b):
        return a * b // gcd(a, b)
        
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        a, b = map(int, sys.stdin.readline().split(" "))
        # 최소 공배수
        result = lcm(a, b)
        print(result)
        
solution()