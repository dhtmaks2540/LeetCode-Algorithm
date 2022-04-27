"""
트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 구하라

DFS를 사용하여 먼저 풀이하려고 했는데 풀리지 않아서 BFS로 도전, 힌트를 얻은 후 문제 풀이.
우선 아무 노드를 BFS 탐색에 투입해서 가장 먼 노드를 구한 후, 다시 해당 노드부터
가장 먼 노드를 구하는 방식으로 풀이하였다. 이렇게 되면 트리의 지름이 된다.

https://dbstndi6316.tistory.com/153 -> DFS 답

https://blog.myungwoo.kr/112 -> 위의 논리 증명

"""
import sys
import collections

# 정점의 개수
V = int(sys.stdin.readline().strip())
# 간선
edges = [[] for _ in range(V + 1)]

for _ in range(V):
    values = list(map(int, sys.stdin.readline().strip().split(" ")))
    for j in range(1, len(values) - 1, 2):
        edges[values[0]].append((values[j], values[j + 1]))
        
# 방문 확인 리스트
visited = [False] * (V + 1)
# 거리
answer = 0
# 가장 먼 인덱스
long_index = 0

# BFS 탐색
def bfs(start, visited):
    global answer
    global long_index
    queue = collections.deque([(start, 0)])
    visited[start] = True
    
    while queue:
        node, diameter = queue.popleft()
        
        for next_node, price in edges[node]:
            # 방문하지 않았다면
            if not visited[next_node]:
                # 방문처리 후 큐에 삽입
                visited[next_node] = True
                queue.append((next_node, diameter + price))
                # 현재 저장된 거리보다 더 크다면 갱싱
                if answer < diameter + price:
                    answer = diameter + price
                    long_index = next_node

# DFS 탐색
def dfs(node, visited, dist):
    global answer
    global long_index
    
    # 이미 방문했다면 return
    if visited[node]:
        return
    
    if answer < dist: # 갱신
        answer = dist
        long_index = node
    
    # 방문 처리 및 연결된 노드 확인
    visited[node] = True
    for next_node, price in edges[node]:
        dfs(next_node, visited, dist + price)

# 임의의 노드 지정 후 가장 먼 노드 구하기            
bfs(1, visited[:])
# 가장 먼 노드를 다시 한번 돌리면 가장 먼 노드까지의 거리가 도출되며 트리의 지름이 됨
bfs(long_index, visited[:])
# dfs(1, visited[:], 0)
# dfs(long_index, visited[:], 0)
print(answer)