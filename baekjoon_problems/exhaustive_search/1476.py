"""
E S M을 우리가 알고 있는 연도로 몇 년인지 구하라

1 1 1부터 시작해 문제로 주어진 E S M이 될 때까지 더하는 방식으로 풀이 생각
즉, 완전 탐색으로 세 값이 문제로 주어진 E S M이 될때까지 계속해서 더해나가는 방식으로 풀이했다.
"""

import sys

E, S, M = map(int, sys.stdin.readline().strip().split(" "))

e_value = s_value = m_value = 1
answer = 1

# 세 숫자중 하나라도 같이 틀리다면 -> 모두 같을 때까지 반복
while e_value != E or s_value != S or m_value != M:
    e_value += 1
    s_value += 1
    m_value += 1
    
    # 값의 범위를 벗어나면 1로 변경
    if e_value >= 16:
        e_value = 1
    if s_value >= 29:
        s_value = 1
    if m_value >= 20:
        m_value = 1
        
    answer += 1
    
print(answer)