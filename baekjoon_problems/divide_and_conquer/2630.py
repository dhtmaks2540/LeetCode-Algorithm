"""
파란색과 흰색 종이의 개수를 파악해라. 1780번 문제와 비슷한데 이 문제는
9등분으로 종이를 나누는 것이 아닌 4등분으로 종이를 나누어서 개수를 파악한다.

분할 정복을 사용하여 모두 같은 색이 아니라면 4등분으로 분할하고(분할),
모두 같은 색이라면 해당 색의 개수를 확인하는 과정(정복)을 통해 문제를 풀이한다.
다만 해당 문제는 병합정렬과 같이 조합의 과정은 수행하지 않는다.
"""

import sys

N = int(sys.stdin.readline().strip())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split(" "))))

blue_colors = 0
white_colors = 0

def check_color(x, y, size):
    now_color = graph[x][y]
    
    for i in range(size):
        for j in range(size):
            if now_color != graph[i + x][j + y]:
                return False
            
    return True

def divide_and_conquer(x, y, size):
    global blue_colors
    global white_colors
    
    # 모두 같은 색인지 체크(정복)
    if check_color(x, y, size):
        if graph[x][y] == 1:
            blue_colors += 1
        else:
            white_colors += 1
        return
    
    new_size = size // 2
    
    # 4등분으로 분할(분할)
    divide_and_conquer(x, y, new_size) # 왼쪽 위
    divide_and_conquer(x, y + new_size, new_size) # 오른쪽 위
    
    divide_and_conquer(x + new_size, y, new_size) # 왼쪽 아래
    divide_and_conquer(x + new_size, y + new_size, new_size) # 오른쪽 아래
    
divide_and_conquer(0, 0, N)
print(white_colors)
print(blue_colors)