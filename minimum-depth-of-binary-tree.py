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
    # 최소 깊이는 루트에서 가장 가까운 자식 라프 노드이므로
    # 루트 노드부터 시작하여 자식 노드로 탐색하면서 리프 노드 찾기
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 예외처리
        if root is None:
            return 0

        # 깊이 변수
        depth = 0

        # BFS를 위한 데크(큐)
        queue = collections.deque([root])

        # 큐가 있는 동안
        while queue:
            # 깊이 증가
            depth += 1

            # 부모 노드의 개수 만큼
            for _ in range(len(queue)):
                cur_root = queue.popleft()

                # 자식 노드가 모두 존재하지 않다면 minimum-depth
                if cur_root.left is None and cur_root.right is None:
                    return depth

                # 자식 노드가 존재하면 큐에 추가
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)

    """
    https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/36239/Python-BFS-and-DFS-solutions.
    """

    # DFS로 접근
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 현재 노드가 없다면 0 반환
        if not root:
            return 0
        
        # 왼쪽 노드나 오른쪽 노드가 없다면
        if not root.left or not root.right:
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))
        
        # 두 노드 모두 존재한다면 
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))