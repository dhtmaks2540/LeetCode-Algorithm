# Definition for a binary tree node.
from typing import List, Optional
import collections 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # BFS를 사용하여 접근
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # 결과변수
        result = []

        # 예외처리
        if root is None:
            return result

        # 노드, 노드의 합, 노드 경로
        queue = collections.deque([(root, root.val, [root.val])])

        while queue:
            for _ in range(len(queue)):
                node, currSum, path = queue.popleft()
                check = False

                if node.left:
                    check = True
                    queue.append((node.left, currSum + node.left.val, path + [node.left.val]))
                if node.right:
                    check = True
                    queue.append((node.right, currSum + node.right.val, path + [node.right.val]))

                # 리프 노드이며, 현재의 합이 목표의 합과 같다면
                if not check and currSum == targetSum:
                    result.append(path)

        return result

    # DFS를 사용하여 접근
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, targetSum, path = []):
            # exit condition
            if not node:
                return 

            # 리프노드이며 현재의 값이 목표값과 같다면
            if not node.left and not node.right and targetSum == node.val:
                result.append(path)

            # 목표값 및 경로 업데이트
            targetSum -= node.val
            path.append(node.val)

            dfs(node.left, targetSum, path[:])
            dfs(node.right, targetSum, path[:])

        dfs(root, targetSum, [])

        return result

    """
    https://leetcode.com/problems/path-sum-ii/discuss/36829/Python-solutions-(Recursively-BFS%2Bqueue-DFS%2Bstack)
    """
    # DFS로 접근
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, targetSum, path = []):
            if node:
                if not node.left and not node.right and targetSum == node.val:
                    path.append(node.val)
                    result.append(path)

                dfs(node.left, targetSum-node.val, path+[node.val])
                dfs(node.right, targetSum-node.val, path+[node.val])

        dfs(root, targetSum, [])
        return result

    # BFS로 접근
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = [(root, root.val, [root.val])]

        while queue:
            curr, val, ls = queue.pop(0)
            if not curr.left and not curr.right and val == targetSum:
                res.append(ls)
            if curr.left:
                queue.append((curr.left, val + curr.left.val, ls + [curr.left.val]))
            if curr.right:
                queue.append((curr.right, val + curr.right.val, ls + [curr.right.val]))

        return res

root = TreeNode(5, \
    TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), \
        TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
targetSum = 22
solution = Solution()
print(solution.pathSum(root, targetSum))