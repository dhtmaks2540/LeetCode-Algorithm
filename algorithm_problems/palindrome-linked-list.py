from collections import deque

# 파이썬 리스트로 변환
def isPalindrome(head):
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

# 파이썬 데크로 변환
def isPalindrome(head):
    q = deque()

    if not head:
        return True

    node = head
    # 데크로 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬 판별
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    
    return True

# 런너를 활용
def isPalindrome(head):
    rev = None
    # 헤드에서 시작
    slow = fast = head
    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    # 홀 수 인지
    if fast:
        slow = slow.next

    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next

    return not rev

head = [1,2, 2, 1]
print(isPalindrome(head))