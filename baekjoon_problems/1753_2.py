import heapq
import sys
import collections

"""
문제풀이

"""

sys.stdin = open("input.txt", "rt")

# 정점의 개수, 간선의 개수
V, E = map(int, input().split())
# 시작 정점
start = int(input())
# 간선의 정보를 받는 2차원 리스트
graph = [[] for _ in range(V + 1)]
# 거리 테이블
distance = collections.defaultdict(int)

for _ in range(E):
    # 시작 노드, 도착 노드, 가중치
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    # heapq를 사용하기 위한 큐 초기화
    Q = [(0, start)]

    while Q:
        dist, now = heapq.heappop(Q)

        if now not in distance:
            distance[now] = dist

            # 연결된 노드 확인
            for i in graph[now]:
                cost = dist + i[1]
                heapq.heappush(Q, (cost, i[0]))

dijkstra(start)

for i in range(1, V + 1):
    if i not in distance:
        print("INF")
    else:
        print(distance[i])