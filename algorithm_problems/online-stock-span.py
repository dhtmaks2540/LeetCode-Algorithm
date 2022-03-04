"""
https://leetcode.com/problems/online-stock-span/discuss/168311/C%2B%2BJavaPython-O(1)
"""

class StockSpanner:
    def __init__(self):
        # 스택 선언
        self.stack = []

    def next(self, price: int) -> int:
        res = 1
        # 스택에 값이 있고, 현재 값이 마지막 값보다 작은 동안에
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        # 금액과 res 추가
        self.stack.append([price, res])
        return res

# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
print(obj.next(100))
print(obj.next(80))
print(obj.next(60))
print(obj.next(70))
print(obj.next(60))
print(obj.next(75))