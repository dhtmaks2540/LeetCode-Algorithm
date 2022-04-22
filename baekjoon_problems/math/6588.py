"""
골드바흐의 추측이 맞는지 출력하라

에라토스테네스의 체를 사용하는 방법은 알고 접근했지만 in이 시간복잡도가 O(n)인지 파악하지
못해서 문제가 풀리지 않았다... 이보다는 array[값] 을 사용해서 O(1)로 현재 숫자가 모두 
소수인지를 판별하는 방식으로 풀었다...
"""

import sys
import math

def solution():
    # 소수를 저장하는 배열
    prime_nums = []
    # 소수를 판별하는 배열
    array = [True] * (1000001)

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(1000000)) + 1):
        if array[i]:
            prime_nums.append(i)
            j = 2
            while i * j <= 1000000:
                array[i * j] = False
                j += 1
                
    while True:
        num = int(sys.stdin.readline().strip())
        if num == 0:
            break
        
        check = False
        for prime_num in prime_nums:
            if array[num - prime_num]:
                print(f"{num} = {prime_num} + {num - prime_num}")
                check = True
                break
        if not check:
            print("Goldbach's conjecture is wrong.")

solution()