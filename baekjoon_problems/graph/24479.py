"""
간선의 가중치와 오름차순으로 정렬해야 한다고 나오기에 다익스트라 알고리즘을 통해 풀이하는 문제로
이해했다. 하지만 문제를 읽어 보니 간선의 가중치는 사용되지도 않고 단지 깊이 우선 탐색을 통해
노드를 방문할 경우 노드의 방문 순서를 출력하라고 나와있다. 따라서 우선 2차원 리스트로 간선의 정보를
모두 입력받은 후 정렬을 통해서 오름차순으로 만들어준다. 이에 따른 시간복잡도는 O(NlogN)이므로
시간 내에 정렬을 수행할 수 있다. 그 후 DFS를 통해서 탐색을 수행하면 문제를 풀이할 수 있다.

DFS 코드를 작성할 수 있는지, 시간복잡도를 계산할 수 있는지 묻는 문제인듯하다. 
"""

import sys
sys.setrecursionlimit(10**6)

# 정점의 수, 간선의 수, 시작 정점
N, M, R = map(int, sys.stdin.readline().strip().split(" "))
# 정점
array = [[] for _ in range(N + 1)]
# 간선 정보(무방향 그래프)
for _ in range(M):
    start, end = map(int, sys.stdin.readline().strip().split(" "))
    array[start].append(end)
    array[end].append(start)
# 오름차순으로 방문해야 하기에 정렬 수행
for i in range(1, N + 1):
    array[i].sort()
    
answer = [-1] * (N + 1) 
visited = [False] * (N + 1)
cnt = 0
    
def dfs(node):
    global cnt
    
    # 현재 노드 방문 처리
    answer[node] = cnt
    visited[node] = True
    cnt += 1
    
    # 간선을 통해 연결된 노드 확인
    for next_node in array[node]:
        # 방문하지 않았다면 dfs 호출
        if not visited[next_node]:
            dfs(next_node)
            
dfs(R)

for num in range(1, N + 1):
    # 방문을 못한다면 0 출력
    if answer[num] == -1:
        print(0)
    else: # 방문할 수 있다면 방문 순서 출력
        print(answer[num] + 1)