from typing import List
import heapq
import math

"""
유클리드 거리에 따라서 원점에서 가까운 k개의 좌표를 반환

point를 사용해 원점과의 유클리드 거리를 계산하고 가까운 순(작은 값)으로 답을 도출해내야하기에
정렬 또는 우선순위 큐(최소힙)을 사용하여 문제를 풀이
"""

class Solution:
    # 정렬을 사용
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []

        # 유클리드 거리 계산
        for index, point in enumerate(points):
            x, y = point
            distance = x**2 + y**2
            result.append((distance, index))

        # 정렬 수행
        result.sort()
        
        return [points[index] for _, index in result[:k]]

    # 우선순위 큐 사용
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        queue = []

        # 유클리드 거리 계산
        for (x, y) in points:
            # dist = math.sqrt((0 - x) ** 2 + (0 - y) ** 2)
            dist = x ** 2 + y ** 2
            heapq.heappush(queue, (dist, x, y))

        result = []

        # 최소힙이므로 작은 값 먼저 pop
        for _ in range(k):
            (dist, x, y) = heapq.heappop(queue)
            result.append([x, y])

        return result

points = [[3,3],[5,-1],[-2,4]]
k = 2
points = [[1,3],[-2,2]]
k = 1
solution = Solution()
print(solution.kClosest(points, k))