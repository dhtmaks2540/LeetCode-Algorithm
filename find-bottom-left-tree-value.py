# Definition for a binary tree node.
from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 가장 끝에 있는 왼쪽 값을 반환
class Solution:
    max_depth = 0
    result = 0
    # BFS로 접근
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # BFS를 위한 큐 선언
        queue = collections.deque([root])
        # 해당 레벨의 노드를 저장하기 위한 리스트
        value = []

        while queue:
            temp = []
            # 자식 노드의 개수만큼 이터레이션
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 해당 레벨의 노드를 누적
            value.append(temp)

        # 마지막 리프 노드 리스트의 제일 왼쪽값 반환
        return value[-1][0]

    """
    https://bcp0109.tistory.com/202
    """

    # DFS로 접근
    # max_depth : 최고 깊이, result : 결과값
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # Preoder로 트리를 순회 -> depth가 1 높아졌을 때 마주하는 노드가 가장 왼쪽 노드
        def dfs(node, depth = 1):
            if node is None:
                return

            if depth > self.max_depth:
                self.result = node.val
                self.max_depth = depth

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 1)
        return self.result

    """
    https://joomn11.tistory.com/39
    """

    # BFS로 접근
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])

        result = 0
        while queue:
            # 현재 노드의 자식 노드 확인
            for i in range(len(queue)):
                node = queue.popleft()
                # i == 0 즉, 가장 왼쪽 노드에 해당
                if i == 0:
                    result = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

# root = TreeNode(1, \
#     TreeNode(2, TreeNode(4)), \
#         TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(6)))

root = TreeNode(2, TreeNode(1), TreeNode(3))

solution = Solution()
print(solution.findBottomLeftValue(root))