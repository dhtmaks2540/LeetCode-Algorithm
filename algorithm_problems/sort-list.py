# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next

        # 예외처리
        if not result:
            return None
        
        # 정렬
        result.sort()
        root = ListNode(result[0])
        node = root

        for i in range(1, len(result)):
            node.next = ListNode(result[i])
            node = node.next

        return root

    # 런너 기법과 병합 정렬을 사용한 정렬
    # 두 정렬 리스트를 병합
    def mergeTwoLists(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 or l2

    def sortList(self, head):
        # 예외 처리
        if not (head and head.next):
            return head

        # 런너 기법 활용
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        # 분할 재귀 호출
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1, l2)

    def sortList(self, head):
        # 연결 리스트 -> 파이썬 리스트
        p = head
        list = []
        while p:
            list.append(p.val)
            p = p.next

        # 정렬
        list.sort()

        # 파이썬 리스트 -> 연결 리스트
        p = head
        # 값만 변경해주는 방식
        for i in range(len(list)):
            p.val = list[i]
            p = p.next
        return head