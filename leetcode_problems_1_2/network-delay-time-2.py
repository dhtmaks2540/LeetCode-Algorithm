from typing import List

import heapq
import sys
import collections

class Solution:
    # 다익스트라 알고리즘
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 2차원 그래프
        graph = [[] for _ in range(n + 1)]

        # 거리를 나타내는 리스트
        distance = [sys.maxsize] * (n + 1)

        for time in times:
            # 출발 노드, 도착 노드, 시간
            u, v, w = time
            # 우선순위 큐에 활용하기 위해서 시간, 도착 노드 순으로
            graph[u].append((w, v))

            
        # 다익스트라 알고리즘
        q = []
        
        # 시작 노드에서 시작 노드까지의 거리는 0
        distance[k] = 0
        heapq.heappush(q, (distance[k], k))

        while q:
            # 우선순위 큐이기에 거리가 짧은 노드 먼저 pop -> 그리디 알고리즘
            dist, now = heapq.heappop(q)
            
            # 현재의 거리가 기록된 거리보다 작다면 이미 기록된 것이므로 패스
            if dist > distance[now]:
                continue

            for i in graph[now]:
                cost = dist + i[0]
                if distance[i[1]] > cost:
                    # 갱신하기
                    distance[i[1]] = cost
                    heapq.heappush(q, (cost, i[1]))

        max_value = max(distance[1:])
        
        if max_value == sys.maxsize:
            return -1
        else:
            return max_value

    # defaultdict를 사용하는 다익스트라 알고리즘
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            graph[u].append((v, w))

        # 큐 변수: [(소요 시간, 정점)]
        Q = [(0, k)]
        distance = collections.defaultdict(int)

        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in distance:
                distance[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # 모든 노드의 최단 경로 존재 여부 판별
        if len(distance) == n:
            return max(distance.values())
        else:
            return -1


times = [[1,2,1]]
n = 2
k = 2

solution = Solution()
print(solution.networkDelayTime(times, n, k))