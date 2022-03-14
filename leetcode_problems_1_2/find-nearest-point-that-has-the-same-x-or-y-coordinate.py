from typing import List
import heapq

"""
주어진 포인트에서 x나 y의 좌표가 같은 값중에 가장 가까운 Manhattan distance를 가진 인덱스를 반환하라
이또한 k-closest-points-to-origin과 마찬가지로 값을중 최솟값을 가져오기 위해 정렬 또는 우선순위 큐를 사용
"""

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        result = []

        # 조건을 추가하고 Manhattan distance 구하기
        for index, point in enumerate(points):
            if point[0] == x or point[1] == y:
                dist = abs(x - point[0]) + abs(y - point[1])
                result.append((dist, index))

        # 정렬 수행
        result.sort(key=lambda value: (value[0], value[1]))

        if not result:
            return -1
        else:
            return result[0][1]

    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        heap = []

        # 조건을 추가하고 Manhattan distance 구하기
        for index, point in enumerate(points):
            if point[0] == x or point[1] == y:
                dist = abs(x - point[0]) + abs(y - point[1])
                heapq.heappush(heap, (dist, index))

        if not heap:
            return -1
        else:
            dist, index = heapq.heappop(heap)
            return index
        
x = 3
y = 4
points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
x = 3
y = 4
points = [[3,4]]
x = 3
y = 4
points = [[2,3]]
solution = Solution()
print(solution.nearestValidPoint(x, y, points))