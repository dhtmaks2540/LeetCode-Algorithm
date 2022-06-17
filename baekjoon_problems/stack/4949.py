"""
균형잡힌 괄호인지 판단하라

균형잡힌 괄호, 괄호 등의 문제가 나오면 일단 스택을 생각하면 된다. 그 이유는 대부분의 괄호 문제들은
균형잡힌(정상적인) 괄호인지 많이 물어보는 문제들이 많은데, 정상적인 괄호인지를 판단하기 위해서 닫힌
괄호가 나왔을 경우 가장 최근에 들어간 괄호가 자신과 짝이 맞는 열린 괄호인지 판단하면 되기 때문이다.
따라서 스택을 사용해 후입선출의 특징을 살려서 문제를 풀이하면 쉽게 풀 수 있다.

해당 문제는 스택의 개념과 괄호를 판단하는 예제와 같은 경우 스택을 사용하는 방법을 알 수 있는 
문제인듯하다.
"""

import sys

dic = {
    ")" : "(",
    "]" : "["
}

while True:
    line = sys.stdin.readline().rstrip()
    
    if line == ".":
        break
    
    # 괄호를  처리하기 위한 스택
    stack = []
    # 균형을 이루고 있는지 확인하는 변수
    balance_check = True
    
    for chr in line:
        # 현재 글자가 열린 괄호라면 스택에 삽입
        if chr in "([":
            stack.append(chr)
        # 현재 글자가 닫힌 괄호인 경우
        elif chr in ")]":
            # 스택에 값이 있고 자신과 짝이 맞는 열린 괄호라면
            if stack and stack[-1] == dic[chr]:
                # 열린 괄호 제거
                stack.pop()
                continue
            # 스택에 값이 없거나 짝이 맞지 않다면 올바르지 않은 괄호이므로 break
            else:
                balance_check = False
                break
            
    # 스택에 값이 있거나 올바르지 않은 괄호라면 no 출력      
    if not balance_check or stack:
        print("no")
    else:
        print("yes")