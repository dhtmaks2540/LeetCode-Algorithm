import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def dfs(node):  
            # 왼쪽 노드나 오른쪽 노드가 존재 할 경우          
            if node.left or node.right:
                # 위치 변경
                node.left, node.right = node.right, node.left

            # not가 존재하지 않을 경우 return
            if not node:
                return

            # 왼쪽과 오른쪽에 대해 재귀적 호출
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root

    # 파이썬다운 방식
    def invertTree(self, root):
        if root:
            root.left, root.right = \
                self.invertTree(root.left), self.invertTree(root.right)
            return root
        return None

    # BFS 활용
    def invertTree(self, root):
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            # 부모 노드로부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root

    # DFS 활용
    def invertTree(self, root):
        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            # 부모 노드로부터 하향식 스왑
            if node:
                node.left, node.rught = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)

        return root

    # 반복구조로 DFS 후위 순휘
    def invertTree(self, root):
        stack = collections.deque([root])

        while stack:
            node = stack.pop()

            if node:
                stack.append(node.left)
                stack.append(node.right)

                node.left, node.right = node.right, node.left

        return root