# left, right까지만 역순으로 정렬
def reverseBetween(head, left, right):
    # 예외 처리
    if not head or left == right:
        return head

    # 루트 노드 생성
    root = start = ListNode(None)
    # 루트 노드의 다음 값은 연결 리스트의 head로
    root.next = head
    # start, end 지정
    for _ in range(left - 1):
        start = start.next
    end = start.next

    # 반복하면서 루트 노드 차례대로 뒤집기
    for _ in range(right - left):
        tmp = start.next
        start.next = end.next
        end.next = end.next.next
        start.next.next = tmp

    # root.next로 head 반환
    return root.next