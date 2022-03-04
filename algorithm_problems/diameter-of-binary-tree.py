# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest = 0
    # 리프노드에서 올라가는 방식으로 구현
    def diameterOfBinaryTree(self, root: Optional[TreeNode]):
        def dfs(node):
            # 리프노드일 경우 -1, -1이 left와 right값으로 지정
            if not node:
                return -1

            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로(현재 노드에서 왼쪽 노드 + 오른쪽 노드 + 2)
            self.longest = max(self.longest, left + right + 2)
            # 상태값(리프노드에서 현재 노드까지의 거리)
            return max(left, right) + 1

        dfs(root)
        return self.longest