"""
두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하라

"""

import sys

# 투 포인터 이용
def solution1():
    # 배열 A의 크기, 배열 B의 크기
    N, M = map(int, sys.stdin.readline().split(" "))
    # 배열 A
    a_array = list(map(int, sys.stdin.readline().split(" ")))
    # 배열 B
    b_array = list(map(int, sys.stdin.readline().split(" ")))
    
    # a 포인트, b 포인트
    a_index = b_index = 0
    
    answer = []
    
    while a_index < N or b_index < M:
        # b를 모두 확인했거나, a를 모두 확인하지 않았고, 현재 a의 값이 더 작거나 같다면
        if b_index == M or (a_index != N and a_array[a_index] <= b_array[b_index]):
            answer.append(a_array[a_index])
            a_index += 1
        # a를 모두 확인했거나, b를 모두 확인하지 않았고, 현재 ㅁ의 값이 더 크다면
        elif a_index == N or (b_index != M and a_array[a_index] > b_array[b_index]):
            answer.append(b_array[b_index])
            b_index += 1
            
    for x in answer:
        print(x, end=" ")
    
solution1()
    
# 파이썬 함수 사용
def solution2():
    import sys
    
    # 배열 A의 크기, 배열 B의 크기
    N, M = map(int, sys.stdin.readline().split(" "))
    # 배열 A
    a_array = list(map(int, sys.stdin.readline().split(" ")))
    # 배열 B
    b_array = list(map(int, sys.stdin.readline().split(" ")))
    
    answer = a_array + b_array
    answer.sort()
    
    for x in answer:
        print(x, end=" ")
    
solution2()

