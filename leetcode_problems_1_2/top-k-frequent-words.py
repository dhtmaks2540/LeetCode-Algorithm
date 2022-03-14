import collections
import heapq
from typing import List

class Solution:
    # Counter와 heapq(우선순위 큐)를 이용하여 접근
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqs = collections.Counter(words)
        freqs_heapq = []

        for f in freqs:
            heapq.heappush(freqs_heapq, (-freqs[f], f))

        result = []

        for _ in range(k):
            result.append(heapq.heappop(freqs_heapq)[1])

        return result

    # 파이썬다운 방식
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 정렬수행
        words.sort()

        return list(zip(*collections.Counter(words).most_common(k)))[0]

words = ["i","love","leetcode","i","love","coding"]
k = 3

solution = Solution()
print(solution.topKFrequent(words, k))