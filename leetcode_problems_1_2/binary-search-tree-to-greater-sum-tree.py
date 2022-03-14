import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 계속 누적할 값
    val = 0

    def bstToGst(self, root):
        # 중위 순회 노드 값 누적
        # 오른쪽 노드 - 자기 자신 - 왼쪽 노드를 들리는 순서
        # 자신보다 같거나 큰 값을 구하려면 자기 자신을 포함한
        # 우측 자식 노드의 합을 구하면 됨
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)

        return root

root = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]