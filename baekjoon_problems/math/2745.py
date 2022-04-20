"""
B 진법의 수 N을 10진법으로 출력하라

B 진법의 수 N을 10진법으로 바꾸려면 파이썬의 int 함수를 사용하거나 직접 함수를 구현하여
사용할 수 있다.
"""

# 파이썬의 함수 사용
def solution1():
    N, B = input().split(" ")
    print(int(N, int(B)))
    
# solution1()

# 직접 함수를 구현
def solution2():
    N, B = input().split(" ")
    M = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = 0
    # 숫자 거꾸로 iteration
    for idx, number in enumerate(N[::-1]):
        # 현재 숫자값의 index * 진법^idx 를 계속해서 더한다
        answer += M.find(number) * (int(B)**idx)
        
    print(answer)
    
solution2()