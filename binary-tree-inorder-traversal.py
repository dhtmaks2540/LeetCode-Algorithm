# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 중위 순회 구조로 node의 value 반환
    # DFS와 중위 순회(LNR)을 사용하여 풀이
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            # exit condition
            if not node:
                return None

            # 왼쪽 순회
            dfs(node.left)
            # 현재 노드 순회
            result.append(node.val)
            # 오른쪽 순회
            dfs(node.right)

        dfs(root)

        return result

    # 스택(DFS)과 중위 순회를 사용하여 풀이
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        node = root
        
        result = []

        while stack or node:
            # 왼쪽 노드 순회
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            # 현재 노드 방문
            result.append(node.val)
            
            node = node.right

        return result

root = TreeNode(1)
solution = Solution()
print(solution.inorderTraversal(root))