"""
접근방법

네트워크를 연결하려 하는데 컴퓨터와 컴퓨터를 직접 연결하려고 한다. 다만 모든 컴퓨터를 연결하며 
비용을 최소로 구하라가 문제의 핵심이다.

따라서 컴퓨터와 컴퓨터를 연결하며 모든 컴퓨터를 연결해야 하기에 Spanning Tree = 신장 트리에 해당하고
그 비용을 최소로 하는 것은 최소 신장 트리(Minimum Spanning Tree)에 해당한다.

최소 신장 트리를 풀이하는 방법은 크루스칼 알고리즘, 프림 알고리즘이 있는데 두 알고리즘 모두
시간 복잡도가 O(ElogV)이다.
"""

import sys

# sys.stdin = open("input.txt", "rt")

input = sys.stdin.readline

# 재귀적으로 부모 노드 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

# 노드 Union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 더 작은 노드를 부모 노드로
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

# 컴퓨터의 수(접점의 수)
V = int(input())
# 연결할 수 있는 선의 수(간선의 수)
E = int(input())
# 부모 노드 
parent = [0] * (V + 1)
# 간선의 정보
edges = []

# 간선의 정보 입력
for _ in range(E):
    # a 노드에서 b 노드로 가는 가중치가 c
    a, b, c = map(int, input().split())
    # 정렬을 위해 가중치 먼저
    edges.append((c, a, b))

# 부모 노드 자기 자신으로
for i in range(1, V + 1):
    parent[i] = i

# 정렬 수행
edges.sort()

# 결과 변수
result = 0

# 가중치가 작은 값부터 먼저 탐색
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 union 수행
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)