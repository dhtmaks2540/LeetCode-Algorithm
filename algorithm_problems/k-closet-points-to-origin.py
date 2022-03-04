from typing import List
import heapq


class Solution:
    # 정렬을 이용
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []

        for point in points:
            # 거리, x, y좌표
            distance.append((point[0]**2 + point[1]**2, point[0], point[1]))

        # 정렬 수행
        distance.sort()

        result = []

        for i in range(k):
            result.append([distance[i][1], distance[i][2]])

        return result

    # 우선 순위 큐를 이용
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []

        for point in points:
            # 거리, x좌표, y좌표
            heapq.heappush(q, (point[0]**2 + point[1]**2, point[0], point[1]))

        result = []

        for i in range(k):
            dis, x, y = heapq.heappop(q)

            result.append([x, y])

        return result

    # 우선순위 큐 책 정답코드
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = x**2 + y**2
            heapq.heappush(heap, (dist, x, y))

        result = []
        for _ in range(k):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x, y))

        return result


points = [[1,3],[-2,2]]
k = 1

solution = Solution()
print(solution.kClosest(points, k))