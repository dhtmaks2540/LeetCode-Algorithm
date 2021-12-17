from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = parent = ListNode(None)
        while head:
            # cur.next의 값이 있고 값이 head보다 작을 경우
            while cur.next and cur.next.val < head.val:
                # 다음 값으로 이동
                cur = cur.next

            # 이 세 개의 변수를 동시에 변경
            cur.next, head.next, head = head, cur.next, head.next
            # 다시 루트노드로 돌아가기
            cur = parent
        return cur.next

    # 개선 버전
    # 실제 삽입 정렬은 오른쪽의 큰 값부터 차례대로 비교
    # 연결 리스트에서 큰 값부터 비교하기 위해 조건을 추가
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = parent = ListNode(0)
        while head:
            # cur.next의 값이 있고 값이 head보다 작을 경우
            while cur.next and cur.next.val < head.val:
                # 다음 값으로 이동
                cur = cur.next

            # 이 세 개의 변수를 동시에 변경
            cur.next, head.next, head = head, cur.next, head.next
            # 필요한 경우에만 cur 포인터가 되돌아가도록 처리
            if head and cur.val > head.val:
                cur = parent
        return parent.next

head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))

solution = Solution()
solution.insertionSortList(head)