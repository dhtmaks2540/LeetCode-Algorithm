"""
입력으로 주어진 A진법으로 나타낸 수를 B진법으로 변환하여 출력하라

N 진법의 수를 10진법으로 바꾼 후 다시 M 진법으로 바꾸어서 문제를 풀었다.
문제를 정확히 이해하고 푸는게 중요한 문제이다.
"""

import sys

def solution():
    # 미래 진법, 정이 진법
    A, B = map(int, sys.stdin.readline().split(" "))
    m = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split(" ")))

    # 미래 진법을 10진법으로 변경(O(M))
    num = 0
    square_root = 0
    for x in array[::-1]:
        num += (A**square_root) * x
        square_root += 1

    answer = []
    
    # 예외처리
    if num == 0:
        print(0)
    else:
        # 10진법을 정이 진법으로(O(M))
        while num:
            remainder = num % B
            if remainder > B:
                answer.append(str(remainder - 10 + ord('a')))
            else:
                answer.append(str(remainder))
                
            num //= B
            
        print(" ".join(answer[::-1]))

solution()