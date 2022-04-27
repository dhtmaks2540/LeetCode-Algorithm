"""
이진 트리를 입력받아 전위 순회, 중위 순회, 후위 순회한 결과를 출력하라

DFS를 사용하여 문제를 풀이
전위, 중위, 후위의 순서에 따라서 먼저 올 노드의 위치에서 노드를 출력해주면 된다.
즉, 전위는 N(가운데) 노드가 먼저이므로 가장 먼저 출력하고
중위는 L(왼쪽) 노드가 먼저이므로 왼쪽을 먼저 방문한 후 출력하고
후위는 L(왼쪽), R(오른쪽) 노드가 먼저이므로 그 둘을 방문한 후 출력하면 된다.
"""

import sys

# 노드의 개수
N = int(sys.stdin.readline().strip())

# NLR
pre_order_path = []
# LNR
in_order_path = []
# LRN
post_order_path = []

# 그래프
graph = [[] for _ in range(1, N + 1)]
for _ in range(N):
    x, y, z = sys.stdin.readline().strip().split(" ")
    index = ord(x) - ord('A')
    if y == '.':
        graph[index].append(None)
    else:
        graph[index].append(ord(y) - ord('A'))
    
    if z == '.':
        graph[index].append(None)
    else:
        graph[index].append(ord(z) - ord('A'))

# 전위
def pre_order(node):
    val = chr(ord('A') + node)
    pre_order_path.append(val)
    
    # 왼쪽 자식 노드 방문
    if graph[node][0]:
        pre_order(graph[node][0])
    
    # 오른쪽 자식 노드 방문
    if graph[node][1]:
        pre_order(graph[node][1])

# 중위
def in_order(node):
    val = chr(ord('A') + node)
    
    # 왼쪽 자식 노드 방문
    if graph[node][0]:
        in_order(graph[node][0])
    
    in_order_path.append(val)
    
    # 오른쪽 자식 노드 방문
    if graph[node][1]:
        in_order(graph[node][1])

# 후위   
def post_order(node):
    val = chr(ord('A') + node)
    
    # 왼쪽 자식 노드 방문
    if graph[node][0]:
        post_order(graph[node][0])
    
    # 오른쪽 자식 노드 방문
    if graph[node][1]:
        post_order(graph[node][1])
        
    post_order_path.append(val)
        
pre_order(0)
in_order(0)
post_order(0)

print("".join(pre_order_path))
print("".join(in_order_path))
print("".join(post_order_path))