"""
주어진 조건을 만족하면서 풀 문제의 순서를 결정해라

해당 문제는 방향 그래프상에서 정점 간에 순서가 존재하는 문제이다.
따라서 위상 정렬을 통해 모든 정점을 나열하면 되는데 다만 문제의 조건 중 정점의 번호가 더 작은 값
부터 풀라는 조건이 있기에 일반적인 큐를 사용하여 위상 정렬을 풀이하는 것이 아닌 우선순위큐를 사용하여
풀어야 한다.

진입차수를 입력하고 진입 차수가 0인 정점을 우선순위큐에 넣는다.
그렇게 되면 정점의 값이 작으면 파이썬의 우선순위큐인 heapq는 최소인 값을 뽑을 수 있기에 조건에 충족시킬 수
있다. 그리고 우선순위 큐에서 정점을 뽑아내고 해당 정점과 연결된 정점을 확인하며
새롭게 진입차수가 0이 된다면 우선순위 큐에 넣어주는 방식으로 풀면 된다.
"""

import sys
import heapq

input = sys.stdin.readline

# 문제의 수, 정보의 개수
n, m = map(int, input().split())
# 진입차수
indegree = [0] * (n + 1)
# 순서쌍(순서)
graph = [[] for _ in range(n + 1)]
# 결과 변수
result = []

# A번 문제는 B번 문제보다 먼저 푸는 것이 좋다
# 즉 B번 문제로 진입하기 위해 A번 문제가 존재
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

queue = []

for i in range(1, len(indegree)):
    # 현재 진입 차수가 0이라면 큐에 추가
    if indegree[i] == 0:
        heapq.heappush(queue, i)

while queue:
    cur_node = heapq.heappop(queue)

    result.append(cur_node)

    # 현재 정점과 연결된 정점을 순회하며
    # 진입 차수를 1씩 감소
    for next_node in graph[cur_node]:
        indegree[next_node] -= 1
        # 이때 새롭게 진입차수가 0이 된다면
        # 큐에 삽입
        if indegree[next_node] == 0:
            heapq.heappush(queue, next_node)

for i in range(len(result)):
    print(result[i], end = " ")