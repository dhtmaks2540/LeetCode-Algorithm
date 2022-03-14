# Definition for a binary tree node.
from typing import List, Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 3가지의 순회(전위, 중위, 후위) 중 2가지만 있어도 이진 트리 복원할 수 있다.
    # 순회의 결과와 이진 트리를 비교하며 공통점 찾아내는게 키 포인트
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            # 전위 순회 결과는 중위 순회 분할 인덱스
            index = inorder.index(preorder.pop(0))

            # 중위 순회 결과 분할 정복
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index+1:])

            return node

    # queue를 사용하여 위의 문제를 최적화
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = collections.deque(preorder)

        def dfs(preorder, inorder):
            if inorder:
                # 전위 순회 결과는 중위 순회 분할 인덱스
                index = inorder.index(preorder.popleft())

                # 중위 순회 결과 분할 정복
                node = TreeNode(inorder[index])
                node.left = dfs(preorder, inorder[0:index])
                node.right = dfs(preorder, inorder[index+1:])

                return node

        result = dfs(preorder, inorder)
        return result
    

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
solution = Solution()
print(solution.buildTree(preorder, inorder))
# print(solution.pre_order(root))