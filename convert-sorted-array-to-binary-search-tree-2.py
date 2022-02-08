# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 분할정복으로 접근
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(nums):
            # exit condition
            if not nums:
                return None
            
            # mid node
            middle = len(nums) // 2
            node = TreeNode(nums[middle])

            # left
            left = dfs(nums[:middle])
            # right
            right = dfs(nums[middle+1:])

            node.left = left
            node.right = right 

            return node

        root = dfs(nums)

        return root

    # 이진 검색 결과로 트리 구성 -> 책 정답
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2

        # 분할 정복으로 이진 검색 결과 트리 구성
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])

        return node

nums = [-10,-3,0,5,9]
solution = Solution()
print(solution.sortedArrayToBST(nums))