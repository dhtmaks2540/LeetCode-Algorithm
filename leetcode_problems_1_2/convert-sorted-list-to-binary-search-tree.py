# Definition for singly-linked list.
from typing import Optional

"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/discuss/35474/Python-recursive-solution-with-detailed-comments-(operate-linked-list-directly).
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Runner 기법과 divide and conquer를 사용
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # exit codition
        if not head:
            return
        
        # head의 다음 노드가 없다면 반환
        if not head.next:
            return TreeNode(head.val)

        # Runner 기법을 통해 중심 노드 찾기
        slow, fast, prev = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            prev, slow = slow, slow.next
        # cut left sub list
        prev.next = None

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root

head = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
solution = Solution()
print(solution.sortedListToBST(head))