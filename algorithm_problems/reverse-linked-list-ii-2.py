# Definition for singly-linked list.
from typing import Optional


"""
https://leetcode.com/problems/reverse-linked-list-ii/discuss/30709/Talk-is-cheap-show-me-the-code-(and-DRAWING)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 그림을 그려가면서 변경되는 구조를 파악하고 그에 대한 풀이를 생각하는 방식으로...
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 예외 처리
        if not head or left == right:
            return head

        # 루트 노드
        root = start = ListNode(None)
        root.next = head
        # start, end 지정
        for _ in range(left - 1):
            start = start.next
        end = start.next

        # 반복하면서 노드 차례대로 뒤집기
        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp

        return root.next