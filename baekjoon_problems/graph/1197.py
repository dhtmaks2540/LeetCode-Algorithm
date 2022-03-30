"""
그래프가 주어졌을 때 최소 스패닝 트리를 구하라.

우선 스패닝 트리란 그래프의 최소 연결 부분 그래프이다. 최소 연결은 간선의 수가 가장 적다는 의미이며,
n개의 정점을 가지는 그래프의 최소 간선의 수가 n-1개이고, n-1개의 간선으로 연결되어 있으면 필연적으로
트리 형태가 되고 이것이 바로 Spanning Tree이다.

최소 스패닝 트리란, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프(Spanning Tree) 중에서 
그 가중치의 합이 최소인 트리를 말한다.

해당 문제는 스패닝 트리이면서 가중치의 합이 최소인 트리의 가중치를 구하는 문제로 MST를 구하는 문제이다.
MST는 크루스칼 알고리즘 또는 프림 알고리즘을 사용하면 되는데 아래는 크루스칼 알고리즘을 사용해서 풀이했다.
"""

import sys

input = sys.stdin.readline

# Find the root node of x recursively
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

# Union the two sets
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 더 작은 값을 부모로
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

# 정점의 개수, 간선의 개수
V, E = map(int, input().split())
# 간선의 정보
edges = []
# 부모 노드
parent = [0] * (V + 1)
# 결과 변수
result = 0

# 부모 노드 자기 자신으로 초기화
for i in range(1, V + 1):
    parent[i] = i

for _ in range(E):
    # a에서 b 정점으로 가는 가중치
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

# 정렬
edges.sort()

# 낮은 금액부터 edge 확인
for edge in edges:
    cost, a, b = edge
    # cycle이 존재하지 않는다면
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)