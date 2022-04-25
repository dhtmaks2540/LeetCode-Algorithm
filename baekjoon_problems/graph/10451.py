"""
N개의 정수로 이루어진 순열이 주어졌을 때, 순열 사이클의 개수를 구하라

11724번과 비슷한 문제로 완전 탐색을 수행하면서 현재 노드를 방문하지 않았다면 DFS 또는 BFS 탐색을 통해
인접한 노드들을 방문하고 결과를 하나씩 추가하는 방식으로 풀이할 수 있다. 즉, Connected Component(연결 요소)
를 찾는 문제이고, 시간 복잡도는 정점 N개를 모두 DFS 또는 BFS 탐색을 수행하므로 
O(N(N + E)) = O(N^2 + NE)라고 생각한다.
"""

import sys
import collections

# 테스트 케이스
T = int(sys.stdin.readline().strip())

for _ in range(T):
    # 정점
    N = int(sys.stdin.readline().strip())
    # 방문 확인 리스트
    visited = [False] * (N + 1)
    # 간선
    edges = [[] for _ in range(N + 1)]
    # 순열
    array = list(map(int, sys.stdin.readline().strip().split(" ")))
    for i in range(len(array)):
        edges[i + 1].append(array[i])
        
    answer = 0
    
    # 모든 정점을 iteration
    for i in range(1, N + 1):
        # 현재 노드를 방문하지 않았다면(새로운 사이클이라면)
        if not visited[i]:
            # 큐 선언 및 방문 처리
            queue = collections.deque([i])
            visited[i] = True
            # 새로운 사이클 추가
            answer += 1
            
            # 큐에 값이 있는 동안
            while queue:
                node = queue.popleft()
                
                # 현재 노드와 연결된 노드 iteration
                for next_node in edges[node]:
                    # 연결된 노드를 방문하지 않았다면
                    if not visited[next_node]:
                        # 큐에 추가 및 방문 처리
                        queue.append(next_node)
                        visited[next_node] = True
                        
    print(answer)