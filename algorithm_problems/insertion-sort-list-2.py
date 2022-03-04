# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    연결 리스트에서 바로 삽입정렬을 수행하는 것은 불가능하다 생각하여 리스트로 변경 후 삽입정렬 수행
    
    삽입 정렬은 첫 번째 원소는 이미 정렬되어 있다고 가정하고 두 번째 원소부터 마지막 원소까지 이터레이션하며
    이전 원소와 크기를 비교하며 현재 원소를 삽입할 위치에 삽입하는 알고리즘으로
    """
    # 리스트로 만든 후 삽입정렬
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = []

        node = head
        while node:
            array.append(node.val)
            node = node.next

        # 삽입정렬 수행
        for i in range(1, len(array)): # 첫 번째 원소부터 이터레이션하며
            for j in range(i, 0, -1): # 이전의 원소와 비교
                if array[j] < array[j - 1]: # 오름차순이기에 현재의 원소보다 이전의 원소가 더 크다면 변경
                    array[j], array[j - 1] = array[j - 1], array[j]
                else:
                    break

        node = head

        for value in array:
            node.val = value
            node = node.next

        return head

    """
    그림을 그려서 이해하는 방식
    """
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # parent는 첫 번째 원소를 항상 가리키도록 셋팅
        cur = parent = ListNode(None)
        while head:
            # 이전의 원소와 비교
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            # 현재 노드의 다음 노드는 head를
            # head의 다음 노드는 cur의 다음 노드를
            # head는 head의 다음 노드를 가리키도록 이동하며 풀이
            cur.next, head.next, head = head, cur.next, head.next

            # 첫 번째 원소부터 비교하기 위해서
            cur = parent
        
        return cur.next

    # 삽입 정렬의 비교 조건 개선
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 초깃값 변경
        cur = parent = ListNode(0)

        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            # 필요한 경우에만 cur 포인터가 되돌아가도록 처리
            if head and cur.val > head.val:
                cur = parent
        
        return parent.next

head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
solution = Solution()
print(solution.insertionSortList(head))