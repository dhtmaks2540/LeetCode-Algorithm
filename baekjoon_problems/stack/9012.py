"""
괄호가 주어질 경우 괄호 문자열이 올바른 괄호 문자열인지 판단하라.

스택을 사용해서 풀 수 있는 대표적인 문제로, FILO 특성을 사용해서 올바른 괄호인지 확인하는 코드를
작성하면 된다. 열린 괄호인 경우에는 스택에 삽입하고, 닫힌 괄호인 경우에는 스택에 값이 있다면 열린
괄호가 있는 것이므로 열린 괄호를 pop하여 정상괄호로 처리한다. 하지만 스택에 값이 없다면
정상괄호가 아니므로 비정상으로 처리한다. 스택의 특성이 First-in Last-out 이므로 이와 같은 방식으로
문제를 풀이할 수 있다.
"""

import sys

# 테스트 케이스
T = int(sys.stdin.readline())

for _ in range(T):
    # 괄호
    array = list(sys.stdin.readline().strip())
    stack = []
    for parenthesis in array:
        # 열린 괄호인 경우 stack에 삽입
        if parenthesis == '(':
            stack.append(parenthesis)
        # 닫힌 괄호인 경우
        else:
            # 스택에 열린 괄호가 있다면 정상괄호로
            if stack:
                stack.pop()
            # 스택에 괄호가 없다면 정상괄호가 아닌 경우
            else:
                stack.append(')')
                break
                    
    # 스택에 값이 없다면, 모두 정상괄호로 처리된 경우
    if not stack:
        print("YES")
    else:
        print("NO")