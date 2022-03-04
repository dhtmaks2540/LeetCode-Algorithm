# Definition for a binary tree node.
from typing import Optional
import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    result = 0
    """
    DFS를 활용하여 접근

    동일 값의 경로를 체크하기 위해서 부모 노드와 자식 노드의 값을 비교하는 조건이 존재
    """
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0

            # 존재하지 않는 노드까지 DFS 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 왼쪽과 오른쪽 자식 노드 간 거리의 합 최댓값이 결과
            self.result = max(self.result, left + right)

            # 가장 큰 직경과 다르게 +1을 하지 않는 이유는
            # +1을 하면 부모 노드와 자식 노드의 값이 같은지 상관없이 무조건 상태값을 업데이트하는 것이고,
            # 이 코드는 같은 값일 경우 위에서 left와 right에 1을 증가하는 방식으로 구현하였기에

            # 자식 노드 상태값 중 큰 값 리턴
            return max(left, right)

        dfs(root)
        return self.result

root = TreeNode(5, \
    TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, None, TreeNode(5)))

# root = TreeNode(1, \
#     TreeNode(4, TreeNode(4), TreeNode(4)), TreeNode(5, None, TreeNode(5)))

solution = Solution()
print(solution.longestUnivaluePath(root))