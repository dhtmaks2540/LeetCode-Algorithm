# Definition for a binary tree node.
from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # BFS로 접근
    """
    왜 BFS로 접근?
    BFS는 큐를 사용해 가까운 인자(노드)부터 접근하게 된다.
    따라서 트리의 루트 노드에서 가까운 자식 노드부터 접근하며 왼쪽과 오른쪽의 값을 변경하기 위해 BFS를 사용함
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 예외 처리
        if root is None:
            return root

        # queue 선언
        queue = collections.deque([root])

        # 큐가 비어있지 않는 동안에
        while queue:
            node = queue.popleft()

            # 왼쪽 노드가 존재
            if node.left is not None:
                left = node.left
            # 존재 X
            else:
                left = None
            # 오른쪽 노드가 존재
            if node.right is not None:
                right = node.right
            # 존재 X
            else:
                right = None

            # 서로 변경
            node.left, node.right = right, left

            if left is not None:
                queue.append(left)
            if right is not None:
                queue.append(right)

        return root

    # DFS로 접근
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 예외 처리
        if root is None:
            return root

        def dfs(node):
            # 왼쪽 노드 존재
            if node.left:
                left = dfs(node.left)
            else:
                left = None
            # 오른쪽 노드 존재
            if node.right:
                right = dfs(node.right)
            else:
                right = None

            # 왼쪽, 오른쪽 변경
            node.left, node.right = right, left

            return node

        dfs(root)
        
        return root

    # 파이썬 다운 방식
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = \
                self.invertTree(root.right), self.invertTree(root.left)
            
            return root
        # 아무것도 리턴하지 않으면 파이썬은 자연스럽게 None을 할당하기에 생략가능
        return None

    # 책에나온 BFS 접근(탑다운 방식 - 부모 노드부터 스왑하면서 계속 아래로 내려감)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            # 부모 노드부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root

    # 반복 구조로 DFS
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            # 부모 노드부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)

        return root

    # 반복 구조로 DFS 후위 순회
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            # 부모 노드부터 하향식 스왑
            if node:
                stack.append(node.left)
                stack.append(node.right)

                node.left, node.right = node.right, node.left # 후위 순회(왼쪽 - 오른쪽 - 자기자신)

        return root
root = TreeNode(4, \
    TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))

solution = Solution()
print(solution.invertTree(root))