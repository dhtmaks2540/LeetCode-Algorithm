# Definition for a binary tree node.
from typing import List, Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# root -> leaf 노드까지의 경로
class Solution:
    # BFS로 접근
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        queue = collections.deque([(root, str(root.val))])

        while queue:
            for _ in range(len(queue)):
                curr_node, path = queue.popleft()

                if curr_node.left:
                    queue.append((curr_node.left, path + "->" + str(curr_node.left.val)))
                if curr_node.right:
                    queue.append((curr_node.right, path + "->" + str(curr_node.right.val)))

                if not curr_node.left and not curr_node.right:
                    result.append(path)

        return result

    # DFS로 접근
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path):
            if not node:
                return []
            
            # 현재값 추가
            path += str(node.val)

            # 리프노드라면 결과 반환
            if not node.left and not node.right:
                return [path]

            path += "->"

            return dfs(node.left, path) + dfs(node.right, path)

        return dfs(root, "")

root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
solution = Solution()
print(solution.binaryTreePaths(root))