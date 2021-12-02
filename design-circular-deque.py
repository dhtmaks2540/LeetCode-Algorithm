class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        # head, tail
        self.head, self.tail = ListNode(None), ListNode(None)
        # 크기, 길이
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    # 이중 연결 리스트에 신규 노드 삽입
    def _add(self, node, new):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    # 이중 연결 리스트에 노드 삭제
    def _del(self, node):
        n = node.right.right
        node.right = n
        n.left = node        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True     

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True
        

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True
        

    def getFront(self):
        """
        :rtype: int
        """
        return self.head.right.val if self.len else -1

    def getRear(self):
        """
        :rtype: int
        """
        return self.tail.left.val if self.len else -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.len == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.len == self.k