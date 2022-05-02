"""
-1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 출력하라

문제를 읽고 그래프를 탐색하는 문제인듯하여 DFS 또는 BFS를 사용하여 문제를 풀이하려고 했는데
조건중에 모두 같은 수가 아닌 경우 종이를 같은 크기 9개로 자르고, 각 자른 종이에 대해서
다시 같은 수 인지 확인하는 과정을 가진다고 하기에 분할정복을 사용하여 재귀 형식으로
풀이했다.

https://st-lab.tistory.com/235

for 문을 사용하여 문제를 풀이하려고 했는데 for문에서 불필요한 범위가 들어가서 시간초과가
출력됐다. 따라서 왼쪽 위부터 오른쪽 아래까지 직접 9 가지 구역으로 나누어서 재귀호출하도록 풀이하였다.
"""

import sys

N = int(sys.stdin.readline().strip())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split(" "))))
answer = [0] * 3

def divide_and_conquer(i, j, len_graph):
    # 모두 같은 수라면(정복)
    if check_num(i, j, len_graph): 
        if graph[i][j] == -1:
            answer[0] += 1
        elif graph[i][j] == 0:
            answer[1] += 1
        elif graph[i][j] == 1:
            answer[2] += 1
        return
    # 모두 같은 수가 아니라면 분할
    len_graph //= 3
    
    divide_and_conquer(i, j, len_graph) # 왼쪽 위
    divide_and_conquer(i, j + len_graph, len_graph) # 중앙 위
    divide_and_conquer(i, j + 2 * len_graph, len_graph) # 오른쪽 위
    
    divide_and_conquer(i + len_graph, j, len_graph) # 왼쪽 중간
    divide_and_conquer(i + len_graph, j + len_graph, len_graph) # 중앙 중간
    divide_and_conquer(i + len_graph, j + 2 * len_graph, len_graph) # 오른쪽 중간
    
    divide_and_conquer(i + 2 * len_graph, j, len_graph) # 왼쪽 아래
    divide_and_conquer(i + 2 * len_graph, j + len_graph, len_graph) # 중앙 아래
    divide_and_conquer(i + 2 * len_graph, j + 2 * len_graph, len_graph) # 오른쪽 아래

# 모두 같은 수인지 확인        
def check_num(i, j, len_graph):
    first_num = graph[i][j] 
    
    for x in range(len_graph):
        for y in range(len_graph):
            if graph[i + x][j + y] != first_num:
                return False
    
    return True

divide_and_conquer(0, 0, N)

for x in answer:
    print(x)