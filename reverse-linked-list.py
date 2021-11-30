# 반복문을 이용한 풀이
def reverseList(head):
    node, prev = head, None

    # node가 None이 될 때까지
    while node:
        # node.next를 prev로 연결
        next, node.next = node.next, prev
        prev, node = node, next

    return prev

# 재귀 구조로 풀이
def reverseList(head):
    def reverse(node, prev = None):
        # node가 None이 될 때까지 재귀 호출
        # 마지막에는 백트래킹되면서 연결 리스트가 거꾸로 연결
        if not node:
            return prev
        # 다음에 올 노드를 node.next로 호출, node.next는 이전의 것과 연결
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)