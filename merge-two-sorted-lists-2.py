# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        node = head

        # 두 리스트 모두 None이 아니라면
        while list1 is not None and list2 is not None:
            # list1 노드의 값이 더 작다면
            if list1.val < list2.val:
                node.next, list1 = list1, list1.next
            # list2 노드의 값이 더 작다면
            elif list1.val >= list2.val:
                node.next, list2 = list2, list2.next
            
            node = node.next

        # list1 노드가 더 남았다면
        if list1 is not None:
            node.next = list1
        # list2 노드가 더 남았다면
        elif list2 is not None:
            node.next = list2

        return head.next

    # 재귀 구조로 연결
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        
        return list1