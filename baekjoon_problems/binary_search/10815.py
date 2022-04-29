"""
숫자 카드를 상근이가 가지고 있으면 1, 아니면 0을 출력하라

두 개의 리스트가 주어진 후 하나의 리스트의 값들이 다른 하나의 리스트에 포함되어있는지 확인하는 
문제이다. 일일히 확인은 해야하므로 완전 탐색 등을 사용할 수 있는데, 데이터의 개수가 500,000개이고
2초(50,000,000)안에 풀어야하므로 O(nlogn)에 풀이할 수 있으면 된다.

따라서 계수 정렬 또는 이분 탐색을 사용해서 문제를 풀이하였다.
"""

import sys

# 계수 정렬을 사용하여 문제 풀이
# 시간 복잡도는 O(n + m)
def solution():
    # 숫자 카드의 개수
    N = int(sys.stdin.readline().strip())
    # 숫자 카드 정수
    numbers = list(map(int, sys.stdin.readline().strip().split(" ")))
    
    # 확인할 숫자의 개수
    M = int(sys.stdin.readline().strip())
    # 확인할 숫자
    check_numbers = list(map(int, sys.stdin.readline().strip().split(" ")))
    
    counts = [0] * (20000001)
    
    for num in numbers:
        counts[num] += 1
        
    for check_num in check_numbers:
        if counts[check_num]:
            print("1", end=" ")
        else:
            print("0", end=" ")
    
solution()

# 이분 탐색 사용
# 시간 복잡도는 O(nlogn + mlogn)
def solution2():
    # 숫자 카드의 개수
    N = int(sys.stdin.readline().strip())
    # 숫자 카드 정수
    numbers = list(map(int, sys.stdin.readline().strip().split(" ")))
    
    # 확인할 숫자의 개수
    M = int(sys.stdin.readline().strip())
    # 확인할 숫자
    check_numbers = list(map(int, sys.stdin.readline().strip().split(" ")))
    
    # 이분 탐색을 위해 정렬 수행
    numbers.sort()
    
    # 이분 탐색
    def binary_search(start, end, target):
        while start <= end:
            mid = start + (end - start) // 2
            
            if numbers[mid] > target:
                end = mid - 1
            elif numbers[mid] < target:
                start = mid + 1
            else:
                return 1
        
        return 0
    
    start = 0
    end = N - 1
    for check_num in check_numbers:
        if binary_search(start, end, check_num):
            print("1", end=" ")
        else:
            print("0", end=" ")
            
solution2()