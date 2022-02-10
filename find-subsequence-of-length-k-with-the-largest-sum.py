from typing import Counter, List
import heapq

# 길이 k subsequence 중 가장 큰값을 가지는 리스트
class Solution:
    # heapq와 정렬을 사용하여 풀이
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = []

        for index, num in enumerate(nums):
            heapq.heappush(queue, (-num, index))

        for _ in range(k):
            num, index = heapq.heappop(queue)
            result.append((-num, index))

        # 인덱스를 가지고 정렬
        result.sort(key= lambda num: num[1])

        return [num for num, _ in result]

    """
    https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/discuss/1623436/JavaPython-3-From-O(n-*-logn)-to-average-O(n)-w-brief-explanation-and-analysis.
    
    1. combine each index with its corresponding value to create a 2-d array
    2. sort the 2-d array reversely by value, copy the largest k ones
    3. sort the largest k ones by index, then return the corresponding values by index other
    """
    # 정렬을 수행하여 풀이
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # 인덱스를 포함하여 정렬 수행
        val_and_index = sorted([(num, i) for i, num in enumerate])
        return [num for num, _ in sorted(val_and_index[-k:], key=lambda x: x[1])]

    """
    Heapq 사용

    1. Traverse input and use heap to store k largest items, poll out if its size bigger than k
    2. Use dict to store the k, items in 1
    3. Traverse input again, if encounter any item in the afore-mentioned dict. save it into the 
    output array, then remove the item from the dict.
    """

    # dict와 heapq 사용
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)

        cnt = Counter(heap)
        res = []

        for n in nums:
            if cnt[n] > 0:
                cnt[n] -= 1
                res.append(n)

        return res
    
nums = [50, -75]
k = 2
solution = Solution()
print(solution.maxSubsequence(nums, k))