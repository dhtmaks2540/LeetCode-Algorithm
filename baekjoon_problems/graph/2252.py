"""
일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성

문제접근

정점들의 순서를 주고 줄을 세우는 프로그램이기에 위상 정렬로 문제를 풀이하였다.
해당 문제는 정점(노드)과 방향이 존재하는 정점들의 순서가 주어지기에 이를 이용해서 모든 정점을 
나열하면 되는 것이다. 문제의 풀이는 진입차수를 리스트로 선언하고 간선을 확인하며 정점을 더한다.

1. 그 후 큐를 선언한 후 우선적으로 진입차수가 0인 정점들을 추가하고
2. 큐에 값이 있는 동안 정점들을 순회하며 해당 정점과 연결된 진입 차수를 제거하며
새롭게 진입차수가 0이 되는 값을 다시 큐에 넣는다.
3. 이와 같은 방식으로 전부 순회하고 아직도 진입차수에 0이 아닌 값이 있다면 해당 문제는
순서를 찾을 수 없는 문제이고, 진입차수가 모두 0이면 해당 문제는 순서를 찾을 수 있는 문제이다.
"""

import sys
import collections

input = sys.stdin.readline

# 학생들의 번호, 키를 비교한 횟수
n, m = map(int, input().split())
# 진입차수
indegree = [0] * (n + 1)
# 키 비교(A가 B 앞에 서야한다)
graph = [[] for _ in range(n + 1)]
# 결과변수
result = []

queue = collections.deque()

for _ in range(m):
    # A가 B 앞에 서야하므로
    # B로 진입하기 위해 A가 필요
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 진입차수가 0인 큐에 넣기
for i in range(1, len(indegree)):
    if indegree[i] == 0:
        queue.append(i)

# 큐에 값이 있는 동안에
while queue:
    cur_node = queue.popleft()

    # 현재 노드 결과에 추가
    result.append(cur_node)

    # 현재 노드와 연결된 노드를 확인하며 진입차수 제거
    for next_node in graph[cur_node]:
        # 진입차수 1 빼기
        indegree[next_node] -= 1
        # 진입차수가 0이 된다면 queue에 추가
        if indegree[next_node] == 0:
            queue.append(next_node)

for i in range(len(result)):
    print(result[i], end = " ")