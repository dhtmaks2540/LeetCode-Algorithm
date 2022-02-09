# Definition for a binary tree node.
from typing import Optional
import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    # DFS를 이용하여 노드를 탐색하고 정렬을 사용하여 풀이
    # 시간복잡도는 nlogn
    # 이진 탐색 트리의 이점을 사용하지 않는 브루드 포스 접근
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        node_list = []
        def dfs(node):
            # exit condition
            if not node:
                return None

            node_list.append(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        node_list.sort()

        for i in range(1, len(node_list)):
            self.result = min(self.result, node_list[i] - node_list[i - 1])

        return self.result

    # 재귀 구조 중위 순회(LNR) 비교 결과
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # 왼쪽 순회
        if root.left:
            self.minDiffInBST(root.left)

        # 최솟값 갱신
        self.result = min(self.result, root.val - self.prev)
        # 이전 노드 갱신
        self.prev = root.val

        # 오른쪽 순회
        if root.right:
            self.minDiffInBST(root.right)

        return self.result

    # 반복 구조로 중위 순회
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = -sys.maxsize
        result = sys.maxsize

        stack = []
        node = root

        # 반복 구조로 중위 순회
        while stack or node:
            # 왼쪽 순회
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()

            # 최솟값 갱신
            result = min(result, node.val - prev)
            # 이전 노드 갱신
            prev = node.val

            # 오른쪽 순회
            node = node.right

        return result

root = TreeNode(4, \
    TreeNode(2, TreeNode(1), TreeNode(3)), \
        TreeNode(6))
solution = Solution()
print(solution.minDiffInBST(root))