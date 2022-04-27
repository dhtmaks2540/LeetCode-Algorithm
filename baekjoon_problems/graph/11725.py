"""
트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하라

처음 문제를 이해 못하고 그림을 그려서 대충 감은 얻었지만 확실히 풀이하지 못했다.
힌트를 확인하던 중 입력 값과 결과 값을 그려보라는 힌트를 받아서 그려보니
부모 - 자식 노드의 방향이 그려졌다. 즉, 입력 값과 결과 값에서 힌트를 받았다..
이를 통해서 graph를 그리고 DFS 탐색을 사용하여 문제를 풀이하였다.

문제가 잘 이해되지 않을 때는 그림을 그려보고 결과 값과 비교해보며 내가 정답을 도출하기 위해
사용할 수 있는 힌트들을 얻는 것이 중요하다.
"""

import sys
sys.setrecursionlimit(10**6)

# 노드의 개수
N = int(sys.stdin.readline().strip())
# 간선
edges = [[] for _ in range(N + 1)]

# 간선 연결
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().strip().split(" "))
    edges[a].append(b)
    edges[b].append(a)

# 방문 확인 리스트와 부모 노드
visited = [False] * (N + 1)
parents = [0] * (N + 1)

def dfs(node):  
    for next_node in edges[node]:
        # 아직 방문 하지 않았다면
        if not visited[next_node]:
            # 방문 처리
            visited[next_node] = True
            # 연결된 노드의 부모 노드를 현재 노드로
            parents[next_node] = node
            dfs(next_node)

# 첫 번째 노드 방문 처리 및 dfs 호출
visited[1] = True
dfs(1)       

for i in range(2, N + 1):
    print(parents[i])