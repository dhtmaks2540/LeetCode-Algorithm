"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하라

파이썬의 일반적인 정렬 알고리즘을 사용하면 O(nlogn)의 시간복잡도가 걸리는데
만약 10,000,000가 입력값으로 들어온다면 총 시간복잡도가 O(10,000,000log10,000,000)으로 이는
2억 3천에 해당한다. 따라서 일반적으로 파이썬은 1초에 20,000,000개의 연산을 수행하고 5초면
1억개이기에 일반적인 정렬 알고리즘을 사용할 수 없다. 따라서 계수 정렬을 통해서
O(n)의 시간 복잡도로 접근하도록 풀이하였다.
"""

import sys

# 계수 정렬을 사용하여 접근
def solution():
    array = [0] * (10001)
    # 수의 개수
    N = int(sys.stdin.readline())
    # 수
    for _ in range(N):
        num = int(sys.stdin.readline())
        array[num] += 1
        
    for i in range(1, 10001):
        if array[i] != 0:
            for _ in range(array[i]):
                print(i) 
            
solution()