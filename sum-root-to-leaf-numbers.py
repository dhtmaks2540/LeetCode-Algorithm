# Definition for a binary tree node.
from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # BFS를 사용하여 접근
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0

        # BFS를 위한 queue
        queue = collections.deque([(root, str(root.val))])

        while queue:
            for _ in range(len(queue)):
                # 현재 노드와 경로
                node, path = queue.popleft()
                
                # 왼쪽, 오른쪽 자식 노드가 없다면 -> 리프 노드라면
                if not node.left and not node.right:
                    result += int(path)

                if node.left:
                    queue.append((node.left, path + str(node.left.val)))
                if node.right:
                    queue.append((node.right, path + str(node.right.val)))

        return result

    # BFS를 사용하여 접근
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0

        # BFS를 위한 queue
        queue = collections.deque([(root, root.val)])

        while queue:
            for _ in range(len(queue)):
                node, path = queue.popleft()

                # 리프 노드라면
                if not node.left and not node.right:
                    result += path

                if node.left:
                    queue.append((node.left, path * 10 + node.left.val))
                if node.right:
                    queue.append((node.right, path * 10 + node.right.val))

        return result

    # DFS로 접근
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # 결과 변수
        self.result = 0

        def dfs(node, path):
            # exit condition
            if not node:
                return

            # 이전값 * 10 + 현재 노드의 값
            path = path * 10 + node.val

            # 리프 노드라면
            if not node.left and not node.right:
                self.result += path

            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, 0)
        return self.result
    
root = TreeNode(4, \
    TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
root = TreeNode(1, TreeNode(2), TreeNode(3))
solution = Solution()
print(solution.sumNumbers(root))