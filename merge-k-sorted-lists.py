import heapq

def mergeKLists(lists):
    q = []

    # 리스트를 for문 돌며
    for list in lists:
        node = list

        # 다음 노드가 존재하는 동안
        while node:
            # 우선순위큐에 값 넣기
            heapq.heappush(q, node.val)
            node = node.next

    # q가 비어있다면 None 반환
    if not q:
        return None

    head = ListNode(heapq.heappop(q))
    node = head
    
    # 큐가 비어있지 않는 동안에
    while q:
        # 큐에서 값 빼오기(최소힙이라 작은놈 먼저)
        temp = ListNode(heapq.heappop(q))
        node.next = temp
        node = temp

    return head

def mergeKLists(lists):
    root = result = ListNode(None)
    heap = []

    # 각 연결 리스트의 루트를 힙에 저장
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (list[i].val, i, lists[i]))

    # 힙 추출 이후 다음 노드는 다시 저장
    while heap:
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]

        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))

    return root.next