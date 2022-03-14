# Definition for a binary tree node.
from typing import Optional
import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 최솟값 변수
    result = sys.maxsize
    # 이전 값을 저장하기 위한 변수
    prev = -sys.maxsize
    # 중위 순회(LNR)과 DFS를 사용하여 풀이
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 왼쪽 순회
        if root.left:
            self.getMinimumDifference(root.left)

        # 최솟값 갱신(현재 노드 방문)
        self.result = min(self.result, root.val - self.prev)
        # 이전 노드 갱신
        self.prev = root.val

        # 오른쪽 순회
        if root.right:
            self.getMinimumDifference(root.right)

        return self.result


root = TreeNode(4, \
    TreeNode(2, TreeNode(1), TreeNode(3)), \
        TreeNode(6))
solution = Solution()
print(solution.getMinimumDifference(root))