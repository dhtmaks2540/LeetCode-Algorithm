from typing import List


import heapq
import collections
import sys

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = collections.defaultdict(list)
        # 그래프의 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append([v, w])
        k = 0
        # 방문처리 확인
        visit = {}
        # 큐 변수: [(가격, 정점, 남은 가능 경유지의 수)]
        Q = [(0, src, 0)]

        # 우선순위 큐 최솟값을 기준으로 도착점까지 최소 비용 판별
        while Q:
            price, node, k = heapq.heappop(Q)
            # 현재 노드와 목적지 노드가 같으면
            if node == dst:
                return price
            # 노드를 아직 방문하지 않았거나
            # 해당 노드를 방문하기 이전에 경유지가 더 적다면
            if node not in visit or visit[node] > k:
                # 방문처리
                visit[node] = k
                for v, w in graph[node]:
                    if k <= K:
                        alt = price + w
                        heapq.heappush(Q, (alt, v, k + 1))
        return -1

    """
    https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/115541/JavaC%2B%2BPython-Priority-Queue-Solution-(TLE-now)
    """

    def findCheapestPrice(self, n, flights, src, dst, k):
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, k + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1

    """
    https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/1698036/Python-BFS-approach-prevents-TLE-(with-explaination)
    """

    def findCheapestPrice(self, n, flights, src, dst, k):
        dict = collections.defaultdict(list)
        # 시작점, 도착점, 금액
        for start, end, price in flights:
            dict[start].append((end, price))

        visit = [sys.maxsize] * n # 최소 금액을 저장하기 위한 array
        # 금액, 시작점, 경유지
        Q = [(0, src, k)]

        while Q:
            cost, s, n = heapq.heappop(Q)
            # 경유지의 개수가 0보다 작거나 현재 노드가 도착지라면 패스
            if n < 0 or s == dst:
                continue
            for end, price in dict[s]:
                """
                현재 path의 금액이 이전 path보다 크다면, 이 path를 더이상 확인할 필요가 없다.
				If the cost of current path is already larger than previous path, we don't need to continue this path anymore, 
				which is a waste of time. This step can prevent the TLE. 
				"""	
                if cost + price > visit[end]:
                    continue
                visit[end] = cost + price
                heapq.heappush(Q, (cost + price, end, n - 1))
        
        return visit[dst] if visit[dst] != sys.maxsize else -1


n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0

solution = Solution()
print(solution.findCheapestPrice(n, flights, src, dst, k))