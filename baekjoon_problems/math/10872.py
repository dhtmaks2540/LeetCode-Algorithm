"""
팩토리얼을 출력하라

파이썬 함수를 이용하거나 직접 for문을 돌려서 문제를 풀이
"""

import math

# 파이썬 함수
def solution1():
    N = int(input())
    print(math.factorial(N))

# 반복
def solution2():
    N = int(input())
    num = 1
    for i in range(2, N + 1):
        num *= i
        
    print(num)
    
solution2()

# 재귀
def solution3():
    N = int(input())
    
    def recursive(n):
        if n == 1:
            return 1
        
        return n * recursive(n - 1)
    
    print(recursive(N))
    
solution3()