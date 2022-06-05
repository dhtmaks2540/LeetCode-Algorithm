"""
3가지의 관계 중 어떠한 관계인지 출력하라

첫 번째 숫자가 두 번째 숫자의 약수인지는 두 번째 숫자를 첫 번째 숫자로 나눈 후 나머지가
0인지로 판단하고, 첫 번째 숫자가 두 번째 숫자의 배수인지는 첫 번째 숫자를 두 번째 숫자로
나눈 후 나머지가 0인지로 판단하고, 그 외의 경우를 세 번째 관계로 분류한다.
"""

import sys

while True:
    a, b = map(int, sys.stdin.readline().strip().split(" "))
    if a == 0 and b == 0:
        break
    
    if b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")