class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q = [None] * k
        self.maxlen = k
        # front
        self.p1 = 0
        # rear
        self.p2 = 0
        
    # rear 포인터 이동
    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        # 데이터 삽입 가능
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    # front 포인터 이동
    def deQueue(self):
        """
        :rtype: bool
        """
        # 데이터 없어서 삭제 불가
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    # 큐의 front 원소 반환
    def Front(self):
        """
        :rtype: int
        """
        # None이라면 -1 아니면 self.p1 위치의 값
        return -1 if self.q[self.p1] is None else self.q[self.p1]
        
    # 큐의 마지막 원소 반환
    def Rear(self):
        """
        :rtype: int
        """
        # rear 포인트의 전이 None이라면 비어있는 것이므로 -1
        # 아니면 그 값 반환
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self):
        """
        :rtype: bool
        """
        return self.p1 == self.p2 and self.q[self.p1] is not None