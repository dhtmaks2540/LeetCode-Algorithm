class BinaryHeap(object):
    def __init__(self):
        # 1번 인덱스는 사용하지 않기 위해 아래와 같이 선언
        self.items = [None]

    def __len__(self):
        # 마지막 인덱스를 반환하도록 설정
        return len(self.items) - 1

    # 삽입 시 실행, 반복 구조 구현
    def _percolate_up(self):
        # 마지막 인덱스
        # 새로 삽입된 값의 인덱스
        i = len(self)
        # 부모 노드(왼쪽 자식은 2i, 오른쪽 자식은 2i + 1이기에)
        parent = i // 2
        # 그 인덱스가 0보다 큰 동안
        while parent > 0:
            if self.items[i] < self.item[parent]:
                self.items[parent], self.items[i] = \
                    self.items[i], self.items[parent]

            i = parent
            parent = i // 2

    # 실제 삽입 시 호출하는 메소드
    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    # 추출 시 실행, 재귀 구조로 구현
    def _precolate_down(self, idx):
        # 왼쪽 노드
        left = idx * 2
        # 오른쪽 노드
        right = idx * 2 + 1
        # 부모 노드
        smallest = idx

        # 왼쪽이 배열 길이 안에 들어있고 값이 더 작다면 작은 값 갱신
        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left
        
        # 오른쪽이 배열 길이 안에 들어있고 값이 더 작다면 작은 값 갱신
        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        # 값이 갱신 되었다면
        if smallest != idx:
            # 위치 변경
            self.items[idx], self.items[smallest] = \
                self.items[smallest], self.items[idx]

    def extract(self):
        # 루트 값
        extracted = self.items[1]
        # 루트 값에 마지막 요소 셋팅
        self.items[1] = self.items[len(self)]
        # 마지막 요소 제거
        self.items.pop()
        self._precolate_down(1)
        return extracted