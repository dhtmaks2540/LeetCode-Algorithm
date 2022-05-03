"""
쿼드 트리 구조를 이용하여 압축 결과를 출력하라

2630번과 굉장히 비슷한 문제인데 영역을 압축한 결과를 차례대로 괄호 안에 묶어서 표현해야 하는
문제이다. 똑같이 분할정복을 사용하여 풀이한다. 
"""

import sys

# 영상의 크기(2의 제곱수)
N = int(sys.stdin.readline().strip())
# 영상 배열
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))
    
answer = []

# 모두 같은 색의 점인지 확인
def check_color(x, y, size):
    now_color = graph[x][y]
    
    for i in range(size):
        for j in range(size):
            if graph[i + x][j + y] != now_color:
                return False
            
    return True

def divide_and_conquer(x, y, size):
    # 정복
    if check_color(x, y, size):
        if graph[x][y] == 0:
            answer.append('0')
        else:
            answer.append('1')
        return
    
    new_size = size // 2
    
    # 분할 시작
    answer.append('(')
    
    # 4등분(분할)
    divide_and_conquer(x, y, new_size) # 왼쪽 위
    divide_and_conquer(x, y + new_size, new_size) # 오른쪽 위
    
    divide_and_conquer(x + new_size, y, new_size) # 왼쪽 아래
    divide_and_conquer(x + new_size, y + new_size, new_size) # 오른쪽 아래
    
    # 분할 끝
    answer.append(')')
    
divide_and_conquer(0, 0, N)
for x in answer:
    print(x, end="")