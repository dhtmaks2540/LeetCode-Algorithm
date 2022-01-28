# Definition for a binary tree node.
from optparse import Option
from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    왜 BFS로 접근?

    모든 노드를 탐색해야하며 같은 레벨에 있는 노드는
    같은 깊이이므로, 큐를 사용하는 BFS로 접근
    """

    # 깊이 : 루트 노드에서 현재 노드까지의 거리
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 예외 처리
        if root is None:
            return 0

        queue = collections.deque([root])
        depth = 0

        while queue:
            # 깊이 증가
            depth += 1
            # 큐 연산 추출 노드의 자식 노드 삽입
            # 현재 레벨의 노드의 개수만큼 반복하기에 부모 노드만 사용
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                # 왼쪽 노드가 존재
                if cur_root.left:
                    queue.append(cur_root.left)
                # 오른쪽 노드가 존재
                if cur_root.right:
                    queue.append(cur_root.right)

        return depth

    # DFS로 접근
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
root = TreeNode(3, \
     TreeNode(9), TreeNode(20, \
         TreeNode(15), TreeNode(7)))

solution = Solution()
print(solution.maxDepth(root))
