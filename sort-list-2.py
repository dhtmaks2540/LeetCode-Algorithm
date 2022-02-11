# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 파이썬 정렬을 사용하여 수행
    # 시간 복잡도 : O(nlogn)
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = []

        node = head

        while node:
            result.append(node.val)
            node = node.next

        # 정렬 수행
        result.sort()

        node = head

        # 값 변경
        for value in result:
            node.val = value
            node = node.next

        return head

    # 두 정렬 리스트 병합
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 두 값이 모두 존재
        if l1 and l2:
            # l1 값이 더 크다면
            if l1.val > l2.val:
                # 위치 변경
                l1, l2 = l2, l1
            # 연결
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 or l2

    # 병합정렬을 사용하여 문제 풀이
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # exit condition
        if not (head and head.next):
            return head

        # 런너 기법 활용
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        # 분할 재귀 호출 -> 가장 작은 노드로 쪼개졌다가 합쳐지면서 정렬 수행
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        # 정복 호출
        return self.mergeTwoLists(l1, l2)


head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
solution = Solution()
print(solution.sortList(head))