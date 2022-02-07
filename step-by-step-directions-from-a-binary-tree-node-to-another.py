# Definition for a binary tree node.
from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/discuss/1612105/3-Steps

    1. Build directions for both start and destination from the root
    -> get "LLRRL" and "LRR"

    2. Remove common prefix path
    -> remove "L". and now start directions is "LRRL". and destination "RR"

    3. Replace all steps in the start direcion to "U" and add destination direction
    => the result is "UUUU" + "RR"
    """
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find(node, val, path):
            # 현재의 값이 목표값과 같다면 True 반환
            if node.val == val:
                return True

            if node.left and find(node.left, val, path):
                path += "L"
            elif node.right and find(node.right, val, path):
                path += "R"
            return path

        start_path, dest_path = [], []
        find(root, startValue, start_path)
        find(root, destValue, dest_path)

        print(start_path)
        print(dest_path)

        while len(start_path) and len(dest_path) and start_path[-1] == dest_path[-1]:
            start_path.pop()
            dest_path.pop()

        return "".join("U" * len(start_path)) + "".join(reversed(dest_path))

root = TreeNode(5, \
    TreeNode(1, TreeNode(3)), \
        TreeNode(2, TreeNode(6), TreeNode(4)))
startValue = 3
destValue = 6
# root = TreeNode(2, TreeNode(1))
# startValue = 2
# destValue = 1
solution = Solution()
# print(solution.getDirections(root, startValue, destValue))
test = []