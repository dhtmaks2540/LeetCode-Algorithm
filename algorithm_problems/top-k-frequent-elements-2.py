from typing import List


import collections
import heapq

class Solution:
    # Counter 활용
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Counter를 이용하여 개수 딕셔너리
        counts = collections.Counter(nums)
        # 많이 나온 순서대로 k 반환
        most_value = counts.most_common(k)

        return [i[0] for i in most_value]

    # Counter와 우선순위 큐 활용
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []
        # 힙에 음수로 삽입
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = list()
        # k번 만큼 추출, 최소 힙이므로 가장 작은 음수 순으로 추출
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk

    # 파이썬다운 방식
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # most_common()은 빈도 수가 높은 순서대로 아이템을 추출하는 기능
        return list(zip(*collections.Counter(nums).most_common(k)))[0]

nums = [1,1,1,2,2,3]
k = 2
solution = Solution()
print(solution.topKFrequent(nums, k))