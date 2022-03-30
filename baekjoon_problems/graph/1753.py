import sys
import heapq

sys.stdin = open("input.txt", "rt")

"""
주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램
가중치는 10이하의 자연수라고 조건이 주어지기에 모든 간선의 가중치가 음수가 아닌 경우 사용할 수 있는
다익스트라 알고리즘을 통해 문제를 풀이

다익스트라 알고리즘은 최악의 경우에도 시간 복잡도가 O(ElogV) (V는 노드의 개수, E는 간서의 개수)

최단 경로 알고리즘은 말 그대로 가장 짧은 경로를 찾는 알고리즘이다. 최단 경로는 '한 지점에서 다른 특정
지점까지의 최단 경로를 구해야 하는 경우', '모든 지점에서 다른 모든 지점까지의 최단 경로를 구해야 하는 경우'
등의 다양한 예시가 있다.

다익스트라 최단 경로 알고리즘은 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여
다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘이다. 다만, 다익스트라 최단 경로 알고리즘은
'음의 간건'이 없을 때 정상적으로 동작한다.
"""

# 정점의 개수, 간선의 개수
V, E = map(int, input().split())
# 시작 정점
start = int(input())
# 간선의 정보를 받는 2차원 리스트
graph = [[] for _ in range(V + 1)]
# 거리 테이블
distance = [sys.maxsize] * (V + 1)

for _ in range(E):
    # 시작 노드, 도착 노드, 가중치
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    # 시작 노드 거리 초기화
    distance[start] = 0
    # heapq를 사용하기 위한 queue 선언
    # 거리, 노드 순으로
    Q = [(0, start)]

    # 큐에 값이 있는 동안
    while Q:
        # 거리, 노드
        dist, now = heapq.heappop(Q)

        # 이미 처리했다면 continue
        if dist < distance[now]:
            continue

        # 연결된 노드를 확인하며
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 가중치가 기록된 가중치보다 작다면 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(Q, (cost, i[0]))

# 다익스트라 수행
dijkstra(start)

for i in range(1, V + 1):
    if distance[i] == sys.maxsize:
        print("INF")
    else:
        print(distance[i])
