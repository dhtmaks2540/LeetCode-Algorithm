# Definition for a binary tree node.
from typing import Optional, Set
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 이진 탐색 트리에서 두 노드의 합이 target이 되는지
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        values = []

        queue = collections.deque([root])

        # BFS
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        dic = {}

        # dic를 사용하여 target 검사
        for i, num in enumerate(values):
            if k - num in dic:
                return True
            dic[num] = i

        return False

    """
    https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/106059/JavaC%2B%2B-Three-simple-methods-choose-one-you-like
    """

    # inorder(중위 순회 LEFT-NOW-RIGHT)와 투 포인터 사용
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = []

        def inorder(node, nums):
            # exit condition
            if not node:
                return
            inorder(node.left, nums)
            nums.append(node.val)
            inorder(node.right, nums)

        inorder(root, nums)

        i, j = 0, len(nums) - 1
        while not i == j:
            if nums[i] + nums[j] == k:
                return True
            elif nums[i] + nums[j] > k:
                j -= 1
            else:
                i += 1
        
        return False

    # Hash Table 사용
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(node, record: Set, k):
            # exit condition
            if not node:
                return False
            
            if k - root.val in record:
                return True

            record.add(node.val)

            return dfs(root.left, record, k) or dfs(root.right, record, k)

        record = set()
        return dfs(root, record, k)

root = TreeNode(5, \
    TreeNode(3, TreeNode(2), TreeNode(4)), \
        TreeNode(6, None, TreeNode(7)))
root = TreeNode(2, \
    TreeNode(1), TreeNode(3))
solution = Solution()
print(solution.findTarget(root, 4))