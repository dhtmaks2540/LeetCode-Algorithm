# Definition for a binary tree node.
from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # root - leaf 까지의 합이 targetSum이 되는 값
    # BFS로 접근
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 예외처리
        if root is None:
            return False
        
        # root노드
        queue = collections.deque([(root, root.val)])

        while queue:
            for _ in range(len(queue)):
                node, sum_val = queue.popleft()
                # 리프 노드인지 체크
                check = False

                if node.left:
                    check = True
                    queue.append((node.left, sum_val + node.left.val))
                if node.right:
                    check = True
                    queue.append((node.right, sum_val + node.right.val))

                # 리프 노드이며, 현재의 합이 목표값과 같다면
                if not check and sum_val == targetSum:
                    return True

        return False

    # DFS로 접근
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.result = 0
        def dfs(node, currSum, check):
            # 합에 현재 노드의 값 추가
            currSum += node.val

            if node.left:
                # 리프 노드인지 검사
                check = True
                dfs(node.left, currSum, False)
            if node.right:
                check = True
                dfs(node.right, currSum, False)

            # 리프 노드이고 루트부터 현재 노드까지의 합이 targetSum과 같다면
            if not check and currSum == targetSum:
                self.result += 1

        # 예외처리
        if root is None:
            return False

        dfs(root, 0, False)

        return True if self.result > 0 else False

    """
    https://leetcode.com/problems/path-sum/discuss/36360/Short-Python-recursive-solution-O(n)
    """
    # DFS로 접근
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # exit condition
        if not root:
            return False

        # 리프 노드이고 현재의 값이 목표값과 같다면
        if not root.left and not root.right and root.val == targetSum:
            return True

        # 목표값에서 현재 노드의 값 빼기
        targetSum -= root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

root = TreeNode(5, \
    TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), \
        TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))

# root = TreeNode(1, TreeNode(2))
# root = TreeNode(1)

# root = TreeNode(1, \
#     TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3)), TreeNode(-3, TreeNode(-2)))

targetSum = 22
# targetSum = 1
# targetSum = 2

solution = Solution()
print(solution.hasPathSum(root, targetSum))