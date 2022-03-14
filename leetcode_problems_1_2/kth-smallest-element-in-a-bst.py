# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# BST에서 K번째로 작은 값 찾기
class Solution:
    """
    BST는 현재 노드보다 왼쪽 노드(서브트리)의 값이 작고
    오른쪽 노드(서브트리)의 값은 큰 트리이다.

    따라서 왼쪽에 있는 값이 작은 값이고, 그 다음은 현재 노드, 그 다음은 오른쪽 노드순서로
    값의 크기가 정렬되어 있기 때문에 스택과 inorder를 이용하여 문제를 풀이
    """
    # Stack과 inorder(left-parent-right) 순회로 풀이
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root

        while stack or node:
            # 왼쪽 노드들을 먼저 방문하기 위해 stack에 추가
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            # 현재 노드 방문(몇 번째 방문인지 체크)
            k -= 1

            # 현재 노드가 원하는 노드라면 return
            if k == 0:
                return node.val
            
            node = node.right

root = TreeNode(3, \
    TreeNode(1, None, TreeNode(2)), \
        TreeNode(4))
solution = Solution()
print(solution.kthSmallest(root, 4))