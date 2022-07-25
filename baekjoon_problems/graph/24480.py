"""
24479번 문제와 똑같지만 내림차순 정렬을 수행한 후 DFS 탐색을 수행하는 문제이다. 따라서 정렬을
수행할 때 내림차순으로 수행하도록 코드를 변경하면 끝이다.

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
    array[i].sort(reverse=True)
    
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