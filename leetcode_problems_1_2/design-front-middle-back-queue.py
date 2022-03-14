import collections

class FrontMiddleBackQueue:

    """
    https://leetcode.com/problems/design-front-middle-back-queue/discuss/952062/Python-1-line-Solution-and-O(1)-Solution
    https://leetcode.com/problems/design-front-middle-back-queue/discuss/951992/Clean-Python-3-O(1)-time-for-each-method
    
    """

    def __init__(self):
        self.A, self.B = collections.deque(), collections.deque()

    # a.size() >= b.size()를 유지
    def balance(self):
        if len(self.A) > len(self.B) + 1:
            self.B.appendleft(self.A.pop())
        if len(self.A) < len(self.B):
            self.A.append(self.B.popleft())

    def pushFront(self, val: int) -> None:
        self.A.appendleft(val)
        self.balance()
        

    def pushMiddle(self, val: int) -> None:
        if len(self.A) > len(self.B):
            self.B.appendleft(self.A.pop())
        self.A.append(val)
        

    def pushBack(self, val: int) -> None:
        self.B.append(val)
        self.balance()
        

    def popFront(self) -> int:
        val = self.A.popleft() if self.A else -1
        self.balance()
        return val
        
    def popMiddle(self) -> int:
        val = (self.A or [-1]).pop()
        self.balance()
        return val

    def popBack(self) -> int:
        val = (self.B or self.A or [-1]).pop()
        self.balance()
        return val


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()