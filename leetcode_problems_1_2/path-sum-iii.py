# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)
    """
    # Brute Force로 접근
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 반환값
        self.numOfpaths = 0
        # 각각의 노드를 이동하는 첫 번째 층의 DFS
        self.dfs(root, targetSum)
        return self.numOfpaths

    # traverse through the tree, at each treenode, call another DFS to test if a path sum include the answer
    # 노드를 순회하면서 각 노드에서 DFS를 호출
    def dfs(self, node, targetSum):
        # exit condition
        if node is None:
            return

        # dfs break down
        self.test(node, targetSum) # you can move the line to any order, here is pre-order
        self.dfs(node.left, targetSum)
        self.dfs(node.right, targetSum)

    # for a given node, DFS to find any path that sum == target, if find self.numOfPaths += 1
    # 현재 노드에서 왼쪽, 오른쪽 노드로 DFS를 호출하면서 목표값 비교
    def test(self, node, targetSum):
        # exit condition
        if node is None:
            return

        if node.val == targetSum:
            self.numOfpaths += 1

        # test break down
        self.test(node.left, targetSum - node.val)
        self.test(node.right, targetSum - node.val)

    """
    Memorization of path sum: O(n)

    1. 브루드 포스 접근을 최적화하기 위해서, 중간의 결과를 저장한다.
    위의 브루드 포스 접근에서, 반복되는 계산을 수행함. 예를 들어, 1->3->5라고 하면, 우리는 1, 1+3, 1+3+5, 3, 3+5, 5를 수행

    2. 이것은 일반적인 "공간과 시간의 tradeoff"에 해당. 모든 path의 합과 빈도(root에서 현재 노드까지)를 저장하는
    dictionary를 만든다.

    3. 계속해서 tree를 순회하면서, 각 노드에서 currPathSum(루트에서 현재 노드까지)를 획득한다. 만약 이 path 안에서
    정답이 존재한다면, currPathSum - oldPathSum = target이 되는 oldPathSum이 반드시 존재하다.

    4. 단지 oldPathSum의 빈도를 결과에 추가한다.

    5. DFS가 아래로 내려가는 동안에, cache[currPathSum]에 -1을 해야한다. 왜냐하면 이 경로는 이후의 탐색에서는
    사용할 수 없기 떄문이다.

    """
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 결과변수
        self.result = 0
        # 딕셔너리(해시 테이블 선언)
        cache = {0:1}

        # 결과를 얻기위한 재귀(DFS)
        self.dfs(root, targetSum, 0, cache)

        return self.result

    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return

        # currPathSum과 oldPathSum을 계산 
        # currPathSum = 루트부터 현재 노드까지의 합
        # oldPathSum = currPathSum에서 target을 뺀 값
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # result와 cache(딕셔너리) update
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1

        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one
        cache[currPathSum] -= 1


root = TreeNode(10, \
    TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))),
    TreeNode(-3, None, TreeNode(11)))

targetSum = 8
solution = Solution()
print(solution.pathSum(root, targetSum))