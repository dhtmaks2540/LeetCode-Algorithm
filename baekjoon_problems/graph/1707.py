"""
그래프가 이분 그래프인지 아닌지 판별하라

https://gmlwjd9405.github.io/2018/08/23/algorithm-bipartite-graph.html

이분 그래프 개념 정리 및 풀이 방법 다시한번 확인하기!
"""

import sys
import collections

# 테스트 케이스
K = int(sys.stdin.readline().strip())

RED = 1
BLUE = -1

def dfs(start, color):
    global check
    # 시작 정점의 색을 설정
    colors[start] = color
    
    for next_node in edges[start]:
        # 시작 정점의 색과 인접한 정점의 색이 같으면 이분 그래프 X
        if colors[next_node] == color:
            check = False
            return
        
        # 시작 정점과 인접한 정점이 방문하지 않은 정점이면 dfs 실행
        if colors[next_node] == 0:
            # 인접한 정점 다른 색 지정
            dfs(next_node, -color)

def bfs(start, color):
    global check
    # root 정점 큐에 삽입 및 방문 표시와 색 표시
    queue = collections.deque([start])
    colors[start] = color
    
    # 큐가 비어있지 않고 이분 그래프가 true라면
    while queue and check:
        node = queue.popleft()
        
        # 해당 정점과 연결된 모든 인접 정점을 방문
        for next_node in edges[node]:
            # 방문하지 않은 정점이면
            if colors[next_node] == 0:
                queue.append(next_node) # 인접 정점 큐에 삽입
                colors[next_node] = colors[node] * -1 # 인접한 정점 다른색으로 칠하기
            # 서로 인접한 정점의 색이 같은 색이면 이분 그래프 아니다
            elif colors[next_node] + colors[node] != 0:
                check = False
                return

for _ in range(K):
    # 정점의 개수, 간선의 개수
    V, E = map(int, sys.stdin.readline().strip().split(" "))
    # 간선
    edges = [[] for _ in range(V + 1)]
    # 양방향 그래프 연결
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().strip().split(" "))
        edges[a].append(b)
        edges[b].append(a)
        
    # 각 정점의 색을 구분
    colors = [0] * (V + 1)
    # 이분 그래프라고 가정
    check = True
    
    # 연결 그래프와 비연결 그래프(모든 정점을 돌면서 확인) 모두 고려
    for i in range(1, V + 1):
        # 이분 그래프가 아니라면 반복문 탈출
        if not check:
            break
        # 방문하지 않은 정점에 대해서 탐색 수행
        if colors[i] == 0:
            dfs(i, RED)
    
    if not check:
        print("NO")
    else:
        print("YES")