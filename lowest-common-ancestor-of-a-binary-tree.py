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

"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/

각 노드의 parent pointers를 갖고 있다면, p와 q의 조상을 얻기 위한 백트래킹을 수행할 수 있다.

이 과정동안 얻는 첫 번째 공통 노드가 LCA 노드일 것이다. 트리를 traverse할 때, 부모 포인터를 딕셔너리에 저장한다.

1. root node에서 시작하여 트리를 traverse
2. p,q를 찾기 전까지 딕셔너리에 부모 포인터를 저장
3. p와 q를 모두 찾으면, 부모 딕셔너리를 사용해 p의 모든 조상을 구하고 ancestors라는 set에 추가
4. 동일하게 q에 대해 조상을 traverse한다. p의 ancestors 집합에 조상이 존재한다면, 이것은 
p와 q 사이에 공통되는 첫 번째 조상임을 의미하고 따라서 이것이 LCA 노드
"""

class Solution:

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Stack for tree traversal
        # 트리 순회를 위한 Stack
        stack = [root]

        # Dictionary for parent pointers
        # parent pointers(부모 노드를 가리키는 포인터)를 위한 딕셔너리
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        # p와 q 모두를 찾기 전까지 반복
        while p not in parent or q not in parent:
            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            # 트리를 순회하는 동안에, parent pointer를 계속해서 저장
            if node.left:
                # node.left의 부모는 node(현재 노드)
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                # node.right의 부모는 node(현재 노드)
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        # p를 위한 조상 집합
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        # parent pointer를 사용하여 노드 p의 모든 조상을 처리
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        # p의 조상 집합 안에서 나타난 q의 첫 번째 조상이 그들의 lca이다.
        while q not in ancestors:
            q = parent[q]
        return q

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