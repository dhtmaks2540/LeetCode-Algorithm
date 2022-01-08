# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    https://leetcode.com/problems/split-linked-list-in-parts/discuss/109284/Elegant-Python-with-Explanation
    """
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # 연결 리스트의 개수 세기
        curr, length = head, 0
        while curr:
            curr, length = curr.next, length + 1

        # 각 요소의 길이 정하기
        chunk_size, longer_chunks = length // k, length % k
        res = [chunk_size + 1] * longer_chunks + [chunk_size] * (k - longer_chunks)

        # 리스트로 나누기
        prev, curr = None, head
        for index, num in enumerate(res):
            # 리스트로 나누기 위해 연결된 노드를 끊는 역할
            if prev:
                prev.next = None
            # 인덱스에 노드 셋팅
            res[index] = curr

            for _ in range(num):
                prev, curr = curr, curr.next

        return res

head = ListNode(1, ListNode(2, ListNode(3)))
k = 5
solution = Solution()
solution.splitListToParts(head, k)