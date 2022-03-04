# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 예외 처리
        if not head:
            return head
        
        # 길이 구하기
        curr, length = head, 0
        while curr:
            curr, length = curr.next, length + 1

        # 연결 리스트의 길이와 같은 횟수를 회전시키면 똑같기에 나머지만 가져오기
        k %= length

        # 예외 처리
        if k == 0 or k == length:
            return head

        node, prev = head, head

        for _ in range(length - k):
            node, prev = node.next, node

        # 연결 끊기
        prev.next = None

        root = node
        # 마지막 노드까지 찾아가기
        while node and node.next:
            node = node.next
        
        # 마지막 노드와 헤드 연결
        node.next = head

        return root

    """
    https://leetcode.com/problems/rotate-list/discuss/348197/96-faster-Simple-python-solution-with-explanation
    """
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 예외처리
        if not head:
            return None
        
        # 마지막 요소 노드
        lastElement = head
        length = 1
        # 리스트의 길이 구하기
        while ( lastElement.next ):
            lastElement = lastElement.next
            length += 1

        # k가 length와 같으면 값이 그대로기에 나머지 처리
        k = k % length
            
        # 마지막 노드가 헤드 노드를 가리키도록 설정
        # 원과 같은 구조를 가지게됨
        lastElement.next = head
        
        # 순회하기
        # 1->2->3->4->5, k=2 라면 Node(3)을 획득하게 됨
        tempNode = head
        for _ in range( length - k - 1 ):
            tempNode = tempNode.next

        # temp 노드의 다음 값을 답으로 지정
        # Example: In 1->2->3->4->5, and k = 2
        #          tempNode = Node(3)
        #          answer = Node(3).next => Node(4)
        #          Node(3).next = None ( cut the linked list from here )
        answer = tempNode.next
        tempNode.next = None
        
        return answer