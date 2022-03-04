# 공간 복잡도는 O(1), 시간 복잡도는 O(n)으로 풀어라..
def oddEvenList(head):
    # 예외 처리
    if head is None:
        return None
        
    # 홀
    odd = head
    # 짝
    even = head.next
    even_head = head.next

    # 반복하면서 홀짝 노드 처리
    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    # 홀수 노드의 마지막을 짝수 헤드로 연결
    odd.next = even_head
    return head