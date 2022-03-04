from typing import Optional
import collections

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 연결 리스트의 값을 받기위한 리스트
        node_list = []

        # next가 존재하는 동안에
        while head.next:
            node_list.append(head.val)
            head = head.next

        # 마지막 값 추가
        node_list.append(head.val)

        return node_list[:] == node_list[::-1]

    # 스택을 이용하여 풀이
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = []

        if not head:
            return True

        node = head

        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        
        return True

    # 데크를 이용하여 스택의 pop연산을 최적화
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = collections.deque()

        if not head:
            return True

        node = head

        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

    # 런너 기법을 활용하여 풀이
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 역순으로 연결 리스트를 만드는 변수
        rev = None
        slow = fast = head

        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            # 다중 할당(동시에 수행함)
            rev, rev.next, slow = slow, rev, slow.next
        # 노드의 개수가 홀수라면 가운데는 무시해야 하므로
        # 슬로우의 위치를 한칸 이동
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        # 팰린드롬이라면 rev나 slow나 모두 None까지 도착했기에 이와같이 반환
        return not slow