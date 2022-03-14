# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 두 개 노드 이하는 그대로 반환(예외처리)
        if head is None or head.next is None or head.next.next is None:
            return head

        # 홀수 노드
        odd = odd_node = ListNode()
        # 짝수 노드
        even = even_node = ListNode()

        while head and head.next:
            odd_node.next = head
            even_node.next = head.next

            odd_node = head
            even_node = head.next

            head = head.next.next

        # 홀수인 경우
        if head is not None:
            odd_node.next = head

        # 두 연결 리스트 묶기
        odd_node.next = even.next

        return odd.next

    # 코드 개선
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 예외 처리
        if head is None:
            return None

        odd = head
        even = even_head = head.next

        # 반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        # 홀수 노드의 마지막을 짝수 헤드로 연결
        odd.next = even_head

        return head