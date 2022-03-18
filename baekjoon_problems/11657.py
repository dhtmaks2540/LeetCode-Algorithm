"""
1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간을 구하는 프로그램

문제풀이

문제에서 가중치에 음수가 포함되어 있기에 벨만 포드를 사용하여 문제를 풀이해야 한다.
벨만 포드 알고리즘은 음수 가중치를 포함한 상황에서 최단 거리를 구할 수 있고
또한 음수 순환이 발생하는지의 여부까지 파악이 가능하다.

다익스트라 알고리즘과의 차이점은 다익스트라는 현재 방문하지 않는 노드 중 최단거리를 찾기에
음수 가중치를 가진 문제에서 최단 거리를 파악하지 못하지만 벨만 포드 알고리즘은 노드를 한 번씩 방문하며
모든 간선을 방문하기에 음수 가중치를 가진 그래프에서도 최단 거리를 파악할 수 있다.
"""

import sys

sys.stdin = open("input.txt", "rt")

# input = sys.stdin.readline
INF = sys.maxsize

# 노드의 개수, 간선의 개수
V, E = map(int, input().split())
# 간선의 정보
edges = []

for _ in range(E):
    # 시작 노드, 도착 노드, 비용
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

# 최단 거리 테이블
distance = [INF] * (V + 1)

def bf(start):
    # 시작 노드에 대해서 0으로 초기화
    distance[start] = 0

    # 전체 V - 1번의 라운드(round)를 반복
    for i in range(V):
        # 매 반복마다 "모든 간선"을 확인하며
        for j in range(E):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[cur] != INF and distance[next_node] > distance[cur] + cost:
                distance[next_node] = distance[cur] + cost

        print(f"{i} : {distance}")

    # 음수 간선 순환 체크(한 번 더 확인해서 값이 갱신된다면 음수 순환이 존재하는 것)
    for j in range(E):
        cur = edges[j][0]
        next_node = edges[j][1]
        cost = edges[j][2]

        if distance[cur] != INF and distance[next_node] > distance[cur] + cost:
            return True

    return False

# 벨만 포드 알고리즘을 수행
negative_cycle = bf(1)

if negative_cycle:
    print("-1")
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, V + 1):
        # 도달할 수 없는 경우, -1
        if distance[i] == INF:
            print("-1")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(distance[i])