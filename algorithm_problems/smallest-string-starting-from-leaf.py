# Definition for a binary tree node.
from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # DFS로 접근
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        result = []
        def dfs(node, path):
            if node is None:
                return

            path.append(chr(97 + node.val))

            # 리프 노드라면 경로 저장
            if not node.left and not node.right:
                result.append(path[::-1])

            dfs(node.left, path[:]) 
            dfs(node.right, path[:])

        dfs(root, [])

        result.sort()

        return "".join(result[0])      

    # BFS로 접근
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        result = []

        # BFS를 위한 큐 선언
        queue = collections.deque([(root, [root.val + 97])])

        while queue:
            for _ in range(len(queue)):
                node, path = queue.popleft()

                # 리프노드라면
                if not node.left and not node.right:
                    result.append(path[::-1])

                if node.left:
                    queue.append((node.left , path + [node.left.val + 97]))
                if node.right:
                    queue.append((node.right, path + [node.right.val + 97]))

        result.sort()

        return "".join(list(map(chr, result[0])))

    """
    https://leetcode.com/problems/smallest-string-starting-from-leaf/discuss/328119/Simple-Python-Solution%3A-top-down-DFS
    """

    # DFS로 접근
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(root, s):
            # 문자로 변경
            s = s + chr(ord('a') + root.val)
            # 리프노드라면
            if not root.left and not root.right:
                if result[0] == None:
                    result[0] = s[::-1]
                else:
                    result[0] = min(result[0], s[::-1])

            if root.left:
                dfs(root.left, s)
            if root.right:
                dfs(root.right, s)

        # 예외처리
        if not root:
            return ''
        
        result = [None]
        dfs(root, '')
        return result[0]

root = TreeNode(0, \
    TreeNode(1, TreeNode(3), TreeNode(4)), \
        TreeNode(2, TreeNode(3), TreeNode(4)))

root = TreeNode(25, \
    TreeNode(1, TreeNode(0, TreeNode(1, TreeNode(0))), TreeNode(0)))

solution = Solution()
print(solution.smallestFromLeaf(root))