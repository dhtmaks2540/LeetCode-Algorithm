from typing import List
import itertools
import collections

class Solution:
    # 재귀 호출을 사용(DFS)
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일 때 결과 추가
            if len(elements) == 0:
                # 값을 복사하는 방식
                results.append(prev_elements[:])

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                # e값 제거
                next_elements.remove(e)

                # e값 추가
                prev_elements.append(e)
                # 재귀 호출
                dfs(next_elements)
                # e값 제거
                prev_elements.pop()

        dfs(nums)
        return results
        
    # itertools의 permutations 라이브러리 사용
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
            
nums = [1,2,3]
solution = Solution()
print(solution.permute(nums))