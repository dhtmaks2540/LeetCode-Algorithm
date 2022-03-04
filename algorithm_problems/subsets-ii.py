from typing import List


class Solution:
    # DFS를 이용하여 접근
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 결과변수
        result = []
        n = len(nums)
        # 정렬수행
        nums.sort()

        def dfs(index, path):
            result.append(path)

            for i in range(index, n):
                # 중복 검사
                # i의 값이 index보다 크고, 이전 값과 동일하면 패스
                if i > index and nums[i] == nums[i - 1]:
                    continue
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return result

    """
    https://leetcode.com/problems/subsets-ii/discuss/30166/Simple-python-solution-without-extra-space.
    """

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()

        for i in range(len(nums)):
            # nums[i]와 nums[i-1]이 같으면 모든 subset을 추가할 필요가 없고,
            # s[i-1]까지의 마지막 subset까지만 추가하면됨
            if i == 0 or nums[i] != nums[i - 1]:
                # res의 길이
                l = len(res)
            
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])

        return res

nums = [1,2,2]
solution = Solution()
print(solution.subsetsWithDup(nums))