# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        list = []

        while head is not None:
            list.append(head.val)
            head = head.next

        list.reverse()

        node = ListNode(list[0])
        temp = node

        if len(node) < 1:
            return node

        for i in range(1, len(list)):
            temp.next = ListNode(list[i])
            temp = temp.next

        return node

    # 재귀 구조로 뒤집기
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev

            next, node.next = node.next, prev
            return reverse(next, node)

        return reversed(head)

    # 반복 구조로 뒤집기
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev