# Definition for a binary tree node.
from typing import Optional


"""
https://leetcode.com/problems/balanced-binary-tree/discuss/35708/VERY-SIMPLE-Python-solutions-(iterative-and-recursive)-both-beat-90
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # DFS로 접근
    """
    왜 DFS로 접근?
    리프노드까지 찾아간 후 리프 노드부터 백트래킹하면서
    자식 노드들의 높이를 부모 노드에게 반환하고 그 값을 비교하는 방식으로 풀이하기 위해서
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            # None이면 0반환
            if not node:
                return 0

            # 왼쪽 자식노드 높이
            left = dfs(node.left)
            # 오른쪽 자식노드 높이
            right = dfs(node.right)

            # 왼쪽 또는 오른쪽 자식노드가 -1이거나
            # 높이의 차가 1이 넘을 경우
            if left == -1 or \
                right == -1 or \
                    abs(left - right) > 1:
                    return -1

            # 왼쪽, 오른쪽 자식 노드의 높이 최댓값 + 1 반환
            return max(left, right) + 1

        return dfs(root) != -1         

root = TreeNode(3, \
    TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

# root = TreeNode(1, \
#     TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), \
#         TreeNode(2))

solution = Solution()
print(solution.isBalanced(root))