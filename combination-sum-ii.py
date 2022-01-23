from typing import List
import collections

class Solution:
    # DFS와 백트래킹을 이용하여 접근
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        # 정렬 수행
        candidates.sort()

        def dfs(csum, index, path):
            # backtracking
            if csum < 0:
                return
            if csum == 0:
                res.append(path)
                return

            # 자기 자신 이후로 결과 추가(한 번만 사용되야 하므로)
            for i in range(index, n):
                # 같은 값이면 패스
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                # 현재 값이 목표값보다 크다면 break(이후에는 어차피 안되므로)
                if candidates[i] > csum:
                    break
                dfs(csum - candidates[i], i + 1, path + [candidates[i]])

        dfs(target, 0, [])
        return res

    

candidates = [10,1,2,7,6,1,5]
target = 8
candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 30
solution = Solution()
print(solution.combinationSum2(candidates, target))