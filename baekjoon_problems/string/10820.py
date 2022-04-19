"""
문자열이 주어질 때, 각 문자열에 대해서 소문자, 대문자, 숫자, 공백의 개수를 구분해 출력하라

각 문자를 소문자, 대문자, 숫자, 공백으로 구분하는 문제로
파이썬은 문자열 라이브러리의 지원이 풍부하기에 is~ 와 같은 함수를 사용해서 쉽게 구분할 수 있다.
"""

import sys

while True:
    try:
        value = list(sys.stdin.readline())
        if not value:
            break
        
        # 각 문자를 구분하기 위한 리스트
        # 소문자, 대문자, 숫자, 공백
        array = [0] * 4
        
        for x in value:
            if x.isdigit():
                array[2] += 1
            elif x.islower():
                array[0] += 1
            elif x.isupper():
                array[1] += 1
            elif x == " ":
                array[3] += 1
                
        for x in array:
            print(x, end=" ")
        print()
    except EOFError:
        break