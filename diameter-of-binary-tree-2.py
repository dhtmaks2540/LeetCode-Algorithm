# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
https://leetcode.com/problems/diameter-of-binary-tree/discuss/101132/Java-Solution-MaxDepth
"""
class Solution:
    longest = 0

    # DFS를 이용하여 접근
    # 재귀 구조로 왼쪽, 오른쪽 자식 노드로 접근하기 위해서
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # 존재하지 않는 노드에는 -1 상태값
            if node is None:
                return -1

            # 왼쪽, 오른쪽의 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로(거리 = 왼쪽 자식 노드 상태값 + 오른쪽 자식 노드 상태값 + 2)
            """
            왼쪽 자식 노드의 리프 노드에서 현재 노드까지의 거리(상태값) + 
            오른쪽 자식 노드의 리프 노드에서 현재 노드까지의 거리(상태값) + 2

            2는 현재 노드와 왼쪽, 오른쪽 자식 노드와의 거리

            즉, 왼쪽과 오른쪽 노드의 리프 노드에서 왼쪽-오른쪽 노드까지의 거리
            + 현재 노드에서 왼쪽 오른쪽 노드와의 거리
            """
            self.longest = max(self.longest, left + right + 2)
            # 상태값(리프 노드에서 현재 노드까지의 거리)
            return max(left, right) + 1

        dfs(root)
        return self.longest

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
solution = Solution()
print(solution.diameterOfBinaryTree(root))