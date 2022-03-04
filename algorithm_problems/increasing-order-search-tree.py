# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # BFS와 정렬을 사용해 풀이 -> 좋은 정답은 X
    def increasingBST(self, root: TreeNode) -> TreeNode:
        queue = [root]
        result = []

        # BFS를 사용하여 트리 탐색
        while queue:
            for _ in range(len(queue)):
                node = queue.pop()

                result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        # 정렬 수행
        result.sort()

        root = TreeNode(result[0])
        node = root

        for i in range(1, len(result)):
            node.right = TreeNode(result[i])
            node = node.right

        return root

    # DFS로 접근
    def increasingBST(self, root: TreeNode) -> TreeNode:
        result = []

        def dfs(node):
            if not node:
                return None

            left = dfs(node.left)
            result.append(node.val)
            right = dfs(node.right)

        dfs(root)

        root = TreeNode(result[0])
        node = root
        for i in range(1, len(result)):
            node.right = TreeNode(result[i])
            node = node.right

        return root

    """
    https://leetcode.com/problems/increasing-order-search-tree/discuss/165885/C%2B%2BJavaPython-Self-Explained-5-line-O(N)
    
    Straight forward idea : result = inorder(root.left) + root + inorder(root.right)
    """
    # Recursive
    def increasingBST(self, root: TreeNode, tail = None) -> TreeNode:
        # if this null node was a left child, tail is its parent
        # if this null node was a right child, tail is its parent's parent
        if not root: return tail
        
        # recursive call, traversing left while passing in the current node as tail
        res = self.increasingBST(root.left, root)
        
        # we don't want the current node to have a left child, only a single right child
        root.left = None
        
        # we set the current node's right child to be tail
        # what is tail? this part is important
        # if the current node is a left child, tail will be its parent
        # else if the current node is a right child, tail will be its parent's parent
        root.right = self.increasingBST(root.right, tail)

        # throughout the whole algorithm, res is the leaf of the leftmost path in the original tree
        # its the smallest node and thus will be the root of the modified tree
        return res

    # Iteration
    def increasingBST(self, root: TreeNode, tail = None) -> TreeNode:
        dummy = TreeNode(0)
        prev = dummy
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            curr.left = None
            prev.right = curr
            prev = curr
            curr = curr.right

        return dummy.right

    """
    https://donic0211.medium.com/leetcode-897-increasing-order-search-tree-d2bd38c310fa
    """

            
root = TreeNode(5, TreeNode(1), TreeNode(7))
solution = Solution()
print(solution.increasingBST(root))