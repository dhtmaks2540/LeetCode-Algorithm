# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 결과 변수
    result = 0
    # low에서 high의 범위 안에 들어가는 노드의 합
    def rangeSumBST(self, root, low, high):
        # 현재 노드가 low와 high의 범위 안에 들어가면
        if low <= root.val and root.val <= high:
            # 값 더해주기
            self.result += root.val

        # 현재의 값이 low보다 크거나 같다면 오른쪽 노드만 확인
        # 현재의 값이 low보다 작다면 오른쪽에는 더 큰값이 있을 수 있으므로 오른쪽 확인
        if (root.val >= low or root.val < low) and root.right:
            self.rangeSumBST(root.right, low, high)

        # 현재의 값이 high보다 크거나 작다면 왼쪽 노드만 확인
        # 현재의 값이 high보다 크다면 왼쪽 노드에 더 작은 값이 있을 수 있으므로 왼쪽 노드 확인
        if (root.val <= high or root.val > high) and root.left:
            self.rangeSumBST(root.left, low, high)

        return self.result

    # 재귀 구조 DFS로 브루드 포스 탐색
    def rangeSumBST(self, root, low, high):
        if not root:
            return 0
        
        return (root.val if low <= root.val <= high else 0) + \
            self.rangeSumBST(root.left, low, high) + \
                self.rangeSumBST(root.right, low, high)

    # DFS 가지치기 탐색
    def rangeSumBST(self, root, low, high):
        def dfs(node):
            if not node:
                return 0

            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            
            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)

    # 반복 구조 DFS로 필요한 노드 탐색
    def rangeSumBST(self, root, low, high):
        stack, sum = [root], 0

        # 스택 이용 필요한 노드 DFS 반복
        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val

        return sum

    # 반복 구조 BFS로 필요한 노드 탐색
    def rangeSumBST(self, root, low, high):
        stack, sum = [root], 0
        # 큐 연산을 이용해 반복 구조 BFS로 필요한 노드 탐색
        while stack:
            node = stack.pop(0)
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val

        return sum