# import sys
# import heapq

"""
출발 도시에서 도착 도시로 가는 최소 비용을 출력하라

문제풀이

A 도시에서 B 도시로 가는 최소 비용을 출력하면 되기에 다익스트라 알고리즘을 사용해서 문제를 풀이했다.
시작도시를 A로 두고 모든 도시로 가는 최소비용을 계산한 후 도착 도시를 B로 주면 된다.
또한 가중치(버스의 비용)이 양수로 이루어져 있기에 벨만포드가 아닌 다익스트라 알고리즘으로 풀이가 가능하며
다익스트라 알고리즘의 시간 복잡도는 O(ElogV) (V는 노드, E는 간선의 개수)이다.

"""

from heapq import heappush, heappop
import sys

input = sys.stdin.readline
INF = sys.maxsize

def solution():
    # 도시의 개수(노드의 개수)
    v = int(input())
    # 버스의 개수(간선의 개수)
    e = int(input())
    # 버스의 정보
    edge = [[] for _ in range(v+1)]
    
    for _ in range(e):
        # 시작 도시, 도착 도시, 금액
        a, b, c = map(int, input().split())
        edge[a].append((b, c))

    # 출발 도시, 도착 도시
    start, end = map(int, input().split())
    
    # 거리 테이블
    dp = [INF] * (v+1)
    # 시작노드 초기화
    dp[start] = 0
    q = [(0, start)]

    # q에 값이 있는 동안
    while q:
        cur_dist, cur_node = heappop(q)
        # 이미 처리헀다면 continue
        if dp[cur_node] < cur_dist:
            continue
        
        for to_node, to_dist in edge[cur_node]:
            dist = cur_dist + to_dist
            # 기록된 거리보다 값이 작다면 갱신
            if dp[to_node] > dist:
                dp[to_node] = dist
                heappush(q, (dist, to_node))
    
    print(dp[end])
    
solution()