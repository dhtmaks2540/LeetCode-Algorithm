from typing import List
import itertools

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # only numbers 1 through 9
        nums = [i for i in range(1, 10)]
        len_n = len(nums)
        result = []

        # DFS와 백트래킹을 활용
        def dfs(target, index, path):
            # backtracking
            if target < 0 or len(path) > k:
                return
            if target == 0 and len(path) == k:
                result.append(path)
                return

            for i in range(index, len_n):
                # 현재의 값이 target보다 크다면
                # 이후의 값은 볼 필요 X(정렬되어 있으므로)
                if nums[i] > target:
                    break
                dfs(target - nums[i], i + 1, path + [nums[i]])

        dfs(n, 0, [])
        return result

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        nums = range(1, 10)
        len_n = len(nums)

        # DFS와 백트래킹을 사용
        def dfs(target, index, k, path):
            # backtracking
            if target < 0 or k < 0:
                return
            if k == 0 and target == 0:
                result.append(path)
                return
            
            for i in range(index, len_n):
                if nums[i] > target:
                    break

                dfs(target - nums[i], i + 1, k - 1, path + [nums[i]])

        dfs(n, 0, k, [])
        return result


    # itertools를 활용
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        for num in list(itertools.combinations(range(1, 10), k)):
            if sum(num) == n:
                result.append(num)
            

        return result

k = 3
n = 9
solution = Solution()
print(solution.combinationSum3(k, n))