"""
정수가 주어지면 소인수분해해서 출력하라.

처음에 에라토스테네스 체를 사용하여 문제를 풀이하려고 접근했다. 다만 이 방법은 코드를 잘못 작성했는지
시간초과가 나와서 그냥 주어진 값이 1이 아니라면 2 ~ N까지 나누어보면서 작은 값부터 나누기에 해당 값으로
나누어지면 소수라 판별하고, 그 값을 누적해서 결과로 도출했다.

https://www.acmicpc.net/source/42356547

조건을 잘 활용하면 시간복잡도를 줄일 수 있는 문제이다.
"""

import math

def solution():
    N = int(input())
        
    answer = []
                
    while N != 1:
        for num in range(2, N + 1):
            if N % num == 0:
                answer.append(num)
                N //= num
                break
            
    for x in answer:
        print(x)
        
def solution2():
    n_max = 10000000
    sqrt_n_max = int(math.sqrt(n_max))
    check = [False, False] + [True] * sqrt_n_max
    
    for i in range(2, int(math.sqrt(sqrt_n_max)) + 1):
        if check[i]:
            j = 2
            while i * j <= sqrt_n_max:
                check[i * j] = False
                j += 1
                
    # 소수
    prime = [x for x in range(len(check)) if check[x] == True]
    
    n = int(input())
    
    # 소수 iteration
    for i in prime:
        # 현재 소수가 주어진 값보다 크다면
        if i > n:
            # 1보다 클 때 print
            if n > 1:
                print(n)
            break
        # 나머지가 0인동안
        while n % i == 0:
            n //= i
            print(i)
    
    # 더이상 나누어지지않는 소수이며 저장된 소수의 최대값보다 크다면
    if n > prime[-1]:
        print(n)

solution2()