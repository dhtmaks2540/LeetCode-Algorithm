from typing import List

import collections
import itertools

class Solution:
    # itertools의 combinations 라이브러리 사용
    def combine(self, n: int, k: int) -> List[List[int]]:
        array = [i for i in range(1, n + 1)]

        return list(map(list, itertools.combinations(array, k)))

    # DFS를 사용하여 접근
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start, k):
            print(elements)

            if k == 0:
                results.append(elements[:])

            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return results

    """
    https://leetcode.com/problems/combinations/discuss/27024/1-liner-3-liner-4-liner
    """
    def combine(self, n, k):
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]

n = 4
k = 2
solution = Solution()
print(solution.combine(n, k))