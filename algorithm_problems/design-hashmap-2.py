import collections

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

# 개별 체이닝 방식으로 구현
class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    # 삽입
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # 인덱스에 노드가 없으면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index]
        while p:
            # 같은 키가 존재하면 갱신
            if p.key == key:
                p.value = value
                return
            # 다음 값이 없다면 break
            if p.next is None:
                break
            # 다음 값으로 이동
            p = p.next
        # p의 다음 값을 연결
        p.next = ListNode(key, value)
    
    # 조회
    def get(self, key: int) -> int:
        index = key % self.size
        # 값이 존재하지 않음
        if self.table[index].value is None:
            return -1

        # 노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next

        return -1
        
    # 삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        # 노드가 존재하지 않음
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)