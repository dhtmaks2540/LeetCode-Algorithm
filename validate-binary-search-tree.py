from typing import Optional
import collections

"""
https://leetcode.com/problems/validate-binary-search-tree/discuss/32112/Learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-(Java-Solution)

Concept behind isBST : if we perform inorder traversal on BST,
we will get the elements in sorted increasing order

Step 1 : init all required variables
    values = List
Step 2 : Perform inorder traversal and add the data part to to list
Step 3 : check whether the elements of list are in increasing sorted order
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 해당 트리가 BST(Binary Search Tree)인지 아닌지 
# 이진 탐색 트리는 현재 노드의 왼쪽 노드는 현재 노드보다 작고,
# 오른쪽 노드는 현재 노드보다 큰 노드가 존재하는 트리
class Solution:
    prev = None
    # 스택과 inorder를 이용하여 문제 풀이
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        node = root
        prev = None
        stack = []

        while stack or node:
            # left node
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()

            # prev(이전노드)가 있고, prev.val이 node.val보다 크다면
            if prev and prev.val >= node.val:
                return False

            # 갱신
            prev = node
            # 오른쪽 방문
            node = node.right

        return True

    # Recursive inorder - 1
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []

        def recursive_inorder(node):
            # exit condition
            if not node:
                return

            # 왼쪽 -> 현재 노드 -> 오른쪽 노드 방문(inorder)
            recursive_inorder(node.left)
            values.append(node.val)
            recursive_inorder(node.right)

        recursive_inorder(root)

        # 정상적인 BST에 inorder를 수행하면 오름차순으로 정렬됨
        for i in range(1, len(values)):
            if values[i - 1] >= values[i]:
                return False

        return True

    # Recursive inorder - 2(Prev 사용)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if not self.isValidBST(root.left):
            return False

        if self.prev and self.prev.val >= root.val:
            return False

        self.prev = root

        if not self.isValidBST(root.right):
            return False

        return True
        

root = TreeNode(2, TreeNode(1), TreeNode(3))
# root = TreeNode(5, TreeNode(1), \
#     TreeNode(4, TreeNode(3), TreeNode(6)))
# root = TreeNode(2, TreeNode(2), TreeNode(2))
# root = TreeNode(5, \
#     TreeNode(4), \
#         TreeNode(6, TreeNode(3), TreeNode(7)))
solution = Solution()
print(solution.isValidBST(root))