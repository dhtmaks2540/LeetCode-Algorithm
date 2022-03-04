from typing import List


class Solution:
    # 브루드 포스로 접근
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        # 첫 번째 인덱스부터 이터레이션
        for i in range(n):
            count = 0
            # 해당 인덱스 + 1부터 검사
            for j in range(i + 1, i + n):
                # 성립하면 count + 1
                if nums[j % n] >= nums[(j - 1) % n]:
                    count += 1
                else:
                    break

            if count == n - 1:
                return True
        
        return False

    """
    https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/discuss/1053508/JavaC%2B%2BPython-Easy-and-Concise
    """
    def check(self, A):
        # a > b의 개수가 1개 이상으로 넘어가면 정렬된 후 회전한 것이 아니기 때문에
        return sum(nums[i] < nums[i-1] for i in range(len(nums))) <= 1


nums = [2,1,3,4]
solution = Solution()
print(solution.check(nums))