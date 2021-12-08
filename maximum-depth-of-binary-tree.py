import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        # 아무런 값이 없으면 0 반환
        if root is None:
            return 0

        # 데크자료형 활용
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            # 큐 연산 추출 노드이 자식 노드 삽입
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                # 왼쪽노드가 존재한다면
                if cur_root.left:
                    queue.append(cur_root.left)
                # 오른쪽 노드가 존재한다면
                if cur_root.right:
                    queue.append(cur_root.right)
            
        # BFS 반복 횟수 == 깊이    
        return depth

root = [3,9,20,None,None,15,7]
solution = Solution()
print(solution.maxDepth(root))