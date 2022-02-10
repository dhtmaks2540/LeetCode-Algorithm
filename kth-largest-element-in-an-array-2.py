from typing import List
import heapq


# 배열의 K번쨰 큰 요소
class Solution:
    # 정렬을 이용하여 풀이 -> O(nlogn)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 정렬 수행
        nums.sort(reverse=True)

        return nums[k - 1]

    # 우선순위 큐를 활용하여 풀이
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = []

        # 최대힙으로 수행하기 위해 음수 연산 추가
        for i in range(len(nums)):
            heapq.heappush(queue, -(nums[i]))

        while queue:
            num = -heapq.heappop(queue)
            k -= 1

            if k == 0:
                return num

    # heapq 모듈의 heapify 활용
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapify : 주어진 자료구조가 힙 특성을 만족하도록 바꿔주는 연산
        # 하나라도 값이 추가되면 힙 특성은 깨짐
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)

    # heapq 모듈의 nlargest 활용
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nlargest는 k번째만큼 큰 값이 가장 큰 값부터 순서대로 리스트로 리턴
        # 마지막 인덱스 -1이 k번째 값이 된다.
        # nsmallest는 동일한 방식으로 n번째 작은 값 추출
        return heapq.nlargest(k, nums)[-1]

nums = [3,2,1,5,6,4]
k = 2
solution = Solution()
print(solution.findKthLargest(nums, k))