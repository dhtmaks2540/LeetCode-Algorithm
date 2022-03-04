# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:        
    """
    https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/discuss/755767/Python-Postorder-Traversal
    """
    
    # DFS를 활용
    def countPairs(self, root: TreeNode, distance: int) -> int:
        count = 0
        def dfs(node):
            nonlocal count
            # exit condition
            if not node:
                return []
            # leaf node
            if not node.left and not node.right:
                return [1]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            count += sum(l + r <= distance for l in left for r in right)
            return [n + 1 for n in left + right if n + 1 < distance]
        
        dfs(root)
        return count

root = TreeNode(1, \
    TreeNode(2, None, TreeNode(4)), \
        TreeNode(3))
root = TreeNode(1, \
    TreeNode(2, TreeNode(4), TreeNode(5)), \
        TreeNode(3, TreeNode(6), TreeNode(7)))
distance = 3
solution = Solution()
print(solution.countPairs(root, distance))