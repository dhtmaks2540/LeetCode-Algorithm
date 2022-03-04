from typing import List


class Solution:
    # 두 개의 숫자만 한번씩 나타나고 나머지는 두번씩 나타남 -> 그 두 숫자를 찾아라
    """
    https://leetcode.com/problems/single-number-iii/discuss/68900/Accepted-C%2B%2BJava-O(n)-time-O(1)-space-Easy-Solution-with-Detail-Explanations
    """
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Pass 1 :
        # Get the XOR of the two numbers we need to find
    
nums = [1,2,1,3,2,5]
solution = Solution()
print(solution.singleNumber(nums ))