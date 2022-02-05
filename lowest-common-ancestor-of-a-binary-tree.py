import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 이 정답으로도 풀려야 한다고 생각
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # BFS를 위한 큐
        queue = collections.deque([(root, [root.val])])
        result = []

        while queue:
            for _ in range(len(queue)):
                node, path = queue.popleft()

                if node.val == p.val or node.val == q.val:
                    result.append(path[:])

                if node.left:
                    queue.append((node.left, path + [node.left.val]))
                if node.right:
                    queue.append((node.right, path + [node.right.val]))

        print("done!!")

        for i in range(len(result[0])):
            if result[0][i] != result[1][i]:
                return result[0][i - 1]

        return result[0][-1]

    """
    https://youtu.be/13m9ZCB8gjw

    https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65225/4-lines-C%2B%2BJavaPythonRuby
    """
    # DFS로 접근
    # 그림을 그려보며 코드를 이해해야함
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # None이면 None 반환
        if not root: return None
        # 현재 노드의 값이 p나 q의 노드의 값과 같다면 현재 노드 반환
        if root.val == p.val or root.val == q.val: return root
        
        # left와 right의 값 받기
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # left와 right 모두 값이 있다면 현재 노드 반환 아니면 left 또는 right의 값 반환
        # if left and right: return root
        # if not left and not right: return None
        # return left or right
        return root if left and right else left or right

root = TreeNode(3)
left = TreeNode(5)
left.left = TreeNode(6)
left_right = TreeNode(2)
left_right.left = TreeNode(7)
left_right.right = TreeNode(4)
left.right = left_right

root.left = left

right = TreeNode(1)
right.left = TreeNode(0)
right.right = TreeNode(8)

root.right = right

solution = Solution()
print(solution.lowestCommonAncestor(root, TreeNode(5), TreeNode(1)))