"""
https://www.acmicpc.net/source/24498930

접근방법

괄호 및 현재 괄호의 점수를 기록하기 위해서 스택을 사용했고, 문제의 조건을 만족하기 위해서 구현으로 풀이했다.
스택을 사용한 이유는 스택은 FILO 자료구조로 나중에 들어간 것이 먼저 나오는 구조이다.
이를 이용하면 가장 최근에 괄호의 열림과 닫힘을 쉽게 파악할 수 있기에 스택을 이용하면 좋다.

그리고, 괄호의 점수를 기록하기 위해서 구현을 사용하였는데, 여러가지 조건('('이냐, '['이냐 등)
이 있기에 이를 머리속으로 생각해내고 조건에 충족하게 코드로 구현해내면 된다.

"""

import sys

string = sys.stdin.readline().strip()

stack = []
multi = 1
answer = 0
pre = ''
pair = {')' : '(', ']' : '['}
score = {'(' : 2, '[' : 3}

for s in string:
    if s in '([':
        stack.append(s)
        # 여는 괄호가 중첩될 때마다 해당 괄호가 닫힐 때 더해질 값을 미리 곱함
        multi *= score[s]
    elif stack:
        if stack[-1] == pair[s]:
            stack.pop()

            # 이전의 문자열이 현재 닫는 괄호와 쌍을 이루는 여는 괄호인 경우에만 값을 추가
            # 그 외에는 닫는 괄호는 이미 그 전에 저장된 값의 곲으로 반영되어 있음
            if pre == pair[s]:
                answer += multi
            # 괄호가 닫혔으니 해당 괄호 만큼 곱했던 값을 나누어 줌
            multi //= score[pair[s]]
        # 괄호끼리 쌍이 맞지 않으면 틀린 괄호
        else:
            answer = 0
            break
    # 여는 괄호가 없는데 닫히면 틀린 괄호
    else:
        answer = 0
        break
    # 괄호가 닫힐 때 현재 값을 저장할 지 판단하기 위해 직전 문자를 저장
    pre = s

# 스택에 값이 남으면 틀린 괄호
if stack:
    answer = 0

print(answer)