# Definition for singly-linked list.
from typing import List, Optional

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 우선순위 큐를 이용하여 접근
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []

        for node in lists:
            while node:
                heapq.heappush(q, node.val)
                node = node.next

        head = ListNode()
        node = head
        while q:
            node.next = ListNode(heapq.heappop(q))
            node = node.next

        return head.next

    # 리스트를 이용하여 접근
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        list = []

        for node in lists:
            while node:
                list.append(node.val)
                node = node.next

        # 정렬 수행
        list.sort()

        node = head = ListNode()

        for val in list:
            node.next = ListNode(val)
            node = node.next

        return head.next

    # 우선순위 큐를 이용한 책의 정답
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        heap = []

        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        # 힙 추출 이후 다음 노드는 다시 저장
        while heap:
            node = heapq.heappop(heap)
            # 인덱스
            idx = node[1]
            # 연결 리스트 연결
            result.next = node[2]
            # 갱신
            result = result.next

            # 다음 연결 노드가 있다면
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next