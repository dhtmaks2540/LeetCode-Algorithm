# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 값을 누적하기 위한 변수
    sum_value = 0
    # 중위 순회(R->N->L)와 DFS를 사용하여 접근
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            # 오른쪽 탐색
            self.bstToGst(root.right)
            # 현재 노드 탐색
            self.sum_value += root.val
            root.val = self.sum_value
            # 왼쪽 탐색
            self.bstToGst(root.left)

        return root

root = TreeNode(4, \
    TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))), \
        TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8))))
solution = Solution()
solution.bstToGst(root)