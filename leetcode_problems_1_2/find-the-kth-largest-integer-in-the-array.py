from typing import List
import heapq

class Solution:
    # k번째 큰 값을 추출
    # 정렬로 풀이
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = list(map(int, nums))

        # 정렬 수행 후 k번째 큰 값 반환
        return str(sorted(nums, reverse=True)[k-1])

    # 우선순위 큐로 풀이
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = list(map(int, nums))

        queue = []

        for num in nums:
            heapq.heappush(queue, -num)
        
        for _ in range(1, k):
            heapq.heappop(queue)

        return str(-heapq.heappop(queue))

nums = ["3","6","7","10"]
k = 4
solution = Solution()
print(solution.kthLargestNumber(nums, k))