"""
1번 컴퓨터가 바이러스에 걸릴 때, 1번 컴퓨터를 통해 바이러스에 걸리게 되는
컴퓨터의 수를 출력하라.

간선을 통해서 연결된 그래프상에서 탐색을 해야 하는 문제
BFS를 활용하여 인접한 노드를 방문하는 방식으로 문제 풀이

그래프를 탐색하는 문제로 시작 노드와 연결된 노드의 개수를 체크하면 된다.
노드와 간선의 정보가 주어졌으므로, 시작 노드를 큐에 넣고 큐에서 값을 pop하면서
현재 노드와 연결된 노드들을 간선의 리스트를 통해 확인하며 방문처리 및 새로 큐에 삽입하는 방식으로 풀이
"""
import collections

# 컴퓨터의 수(노드)
N = int(input())
# 간선의 개수
M = int(input())
# 간선
edges = [[] for _ in range(N + 1)]

# 무방향 그래프
for i in range(M):
    # a와 b 컴퓨터가 연결
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

# 방문확인을 위한 리스트
visited = [False] * (N + 1)
    
# BFS 탐색을 위한 큐 선언 및 시작노드 추가
queue = collections.deque([1])
# 시작노드 방문처리
visited[1] = True
# 결과변수
answer = 0

# 큐에 값이 있는 동안
while queue:
    # 현재 노드 방문 처리
    cur_node = queue.popleft()
    # 결과 더하기
    answer += 1
    
    for node in edges[cur_node]:
        # 방문하지 않았다면
        if not visited[node]:
            # 큐에 추가 및 방문 처리
            visited[node] = True
            queue.append(node)

# 시작 노드 1은 제외한 정답 출력    
print(answer - 1)