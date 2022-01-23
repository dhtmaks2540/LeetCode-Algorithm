from typing import List


class Solution:
    # DFS와 백트래킹을 이용하여 접근
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(csum, index, path):
            # 종료 조건
            if csum < 0: # 목표값 초과
                return
            if csum == 0: # 일치하는 정답
                result.append(path)
                return
            
            # 자신부터 하위 원소까지의 나열 재귀 호출
            # 목표값에서 현재의 값을 빼는 형태로 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])
                
        dfs(target, 0, [])
        return result

candidates = [2,3,6,7]
target = 7 
solution = Solution()
print(solution.combinationSum(candidates, target))