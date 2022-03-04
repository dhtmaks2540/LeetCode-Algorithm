import heapq
import sys

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root):
        queue = []
        # dfs를 활용하여 우선순위 큐에 값 넣기
        def dfs(root):
            if not root:
                return

            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

            heapq.heappush(queue, root.val)

        dfs(root)

        # 현재 값
        now_value = heapq.heappop(queue)
        # 다음 값
        next_value = heapq.heappop(queue)

        # 최소 값
        min_value = next_value - now_value

        # 큐에 값이 있는 동안에
        while queue:
            now_value = next_value
            next_value = heapq.heappop(queue)
            # 갱신 시켜주기
            min_value = min(next_value - now_value, min_value)

        return min_value

class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    # 재귀 구조 중위 순회 비교 결과
    def minDiffInBST(self, root):
        if root.left:
            self.minDiffInBST(root.left)

        # 최소 값 갱신
        self.result = min(self.result, root.val - self.prev)
        # 이전 값 갱신
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result

    def minDiffInBST(self, root):
        prev = -sys.maxsize
        result = sys.maxsize

        stack = []
        node = root

        # 반복 구조 중위 순회 비교 결과
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()

            result = min(result, node.val - prev)
            prev = node.val

            node = node.right

        return result