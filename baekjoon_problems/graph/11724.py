"""
방향 그래프가 주어졌을 때, 연결 요소의 개수를 구하라

union-find를 사용해서 서로소 집합을 구한 후 부모를 파악하여 서로소 개수를 파악하였다.
서로소 집합 알고리즘을 사용하여 문제를 풀이하려고 했는데, 답이 도출되지 않았다. 서로소
알고리즘에 대한 개념을 정확히 파악하지 않은 것 같다..

해당 문제는 정점을 완전 탐색하면서 해당 정점을 방문하지 않았다면 DFS 또는 BFS를 통해
탐색을 수행하며 count를 증가시켜서 풀이할 수 있다. 풀이는 BFS를 사용해서 풀이하였다.
"""

import sys
import collections

# 정점의 개수, 간선의 개수
N, M = map(int, sys.stdin.readline().strip().split(" "))

edges = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split(" "))
    edges[a].append(b)
    edges[b].append(a)
    
visited = [False] * (N + 1)
answer = 0

for i in range(1, N + 1):
    if not visited[i]:
        answer += 1
        
        queue = collections.deque([i])
        visited[i] = True
        
        while queue:
            node = queue.popleft()
            
            for next_node in edges[node]:
                if not visited[next_node]:
                    queue.append(next_node)
                    visited[next_node] = True
print(answer)