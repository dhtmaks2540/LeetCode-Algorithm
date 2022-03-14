from typing import List


class Solution:
    # DFS를 사용하여 접근
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def dfs(index, path):
            # 매번 결과를 추가
            result.append(path[:])

            for i in range(index, n):
                # 현재의 값을 추가
                path.append(nums[i])
                dfs(i + 1, path)
                # 현재의 값 빼기
                path.pop()

        dfs(0, [])
        return result

    # 책에 나온 DFS(깔끔한 코드)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def dfs(index, path):
            # 매번 결과를 추가
            result.append(path)

            for i in range(index, n):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return result

nums = [0]
solution = Solution()
print(solution.subsets(nums))