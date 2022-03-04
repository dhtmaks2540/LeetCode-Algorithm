# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 후위 순회와 중위 순회의 규칙을 찾아 분할정복으로 풀이
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            # 후위 순회의 결과는 중위 순회 분할 인덱스
            index = inorder.index(postorder.pop())
            
            # 중위 순회 결과 분할 정복
            node = TreeNode(inorder[index])
            node.right = self.buildTree(inorder[index+1:], postorder)
            node.left = self.buildTree(inorder[0:index], postorder)

            return node

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
solution = Solution()
print(solution.buildTree(inorder, postorder))