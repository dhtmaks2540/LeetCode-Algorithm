import collections

# 정점의 개수, 간선의 개수, 탐색 시작 정점 번호
N, M, V = map(int, input().split())
# 간선
edges = [[] for _ in range(N + 1)]

for _ in range(M):
    # 양방향 간선
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

# 작은 번호의 정점을 먼저 방문하기 위해 정렬 수행
for edge in edges:
    edge.sort()

# 결과변수를 사용하여 DFS
def dfs(cur_node, paths):
    paths.append(cur_node)
    for node in edges[cur_node]:
        # 방문한 적이 없다면
        if node not in paths:
            # 연결된 노드 재귀 호출
            paths = dfs(node, paths)

    return paths

# 결과변수를 사용하여 BFS
def bfs(start, paths):
    queue = collections.deque([start])
    paths.append(start)

    # 큐에 값이 있는 동안
    while queue:
        cur_node = queue.popleft()

        for node in edges[cur_node]:
            if node not in paths:
                queue.append(node)
                paths.append(node)

    return paths

dfs_result = dfs(V, [])
bfs_result = bfs(V, [])

for node in dfs_result:
    print(node, end = " ")
print()
for node in bfs_result:
    print(node, end=" ")