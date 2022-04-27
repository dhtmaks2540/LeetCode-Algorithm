"""
트리의 지름(트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이)를 구하라.
1167번과 굉장히 비슷한 문제로 똑같은 방식으로 풀이할 수 있다.
"""

import sys
sys.setrecursionlimit(10**5)

# 노드의 개수
n = int(sys.stdin.readline().strip())
# 간선
edges = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    # 부모 노드, 자식 노드, 간선의 길이
    a, b, c = map(int, sys.stdin.readline().strip().split(" "))
    edges[a].append((b, c))
    edges[b].append((a, c))
    
# 방문을 확인하기 위한 리스트
visited = [False] * (n + 1)
# 지름의 길이
max_dist = 0
# 가장 먼 인덱스
max_index = 0

def dfs(node, visited, dist):
    global max_dist
    global max_index
    
    # 이미 방문했다면 return
    if visited[node]:
        return
    
    # 방문 처리
    visited[node] = True
    # 갱신
    if max_dist < dist:
        max_dist = dist
        max_index = node
    
    # 연결된 노드 확인
    for next_node, price in edges[node]:
        dfs(next_node, visited, dist + price)
        
# 임의의 노드에서 가장 먼 노드 탐색
dfs(1, visited[:], 0)
# 해당 노드에서 다시 한번 가장 먼 노드를 탐색하면 트리의 길이에 해당
dfs(max_index, visited[:], 0)
print(max_dist)