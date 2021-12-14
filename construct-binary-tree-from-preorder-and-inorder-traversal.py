# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 재귀 구조로 구현
    # 순회 결과는 서로 연관 관계가 있음
    # 그 관계 파악를 파악하고 소스 코드로 담는게 핵심
    def buildTree(self, preorder, inorder):
        if inorder:
            # 전위 순회 결과는 중위 순회 분할 인덱스
            # 전위 순회의 값을 중위 순회에 넣으면
            # 왼쪽은 왼쪽 노드에 해당, 오른쪽은 오른쪽 노드에 해당
            index = inorder.index(preorder.pop(0))

            # 중위 순회 결과 분할 정복
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildtree(preorder, inorder[index + 1:])

            return node

# 전위
preorder = [3,9,20,15,7]
# 중위
inorder = [9,3,15,20,7]