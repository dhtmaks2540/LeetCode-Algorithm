"""
deque를 구현하라
"""

import collections
import sys

class Deque:
    def __init__(self):
        self.deque = collections.deque()
        
    def push_front(self, value):
        self.deque.appendleft(value)
        
    def push_back(self, value):
        self.deque.append(value)
        
    def pop_front(self):
        if not self.deque:
            print(-1)
        else:
            print(self.deque.popleft())
            
    def pop_back(self):
        if not self.deque:
            print(-1)
        else:
            print(self.deque.pop())
            
    def size(self):
        print(len(self.deque))
        
    def empty(self):
        if not self.deque:
            print(1)
        else:
            print(0)
            
    def front(self):
        if not self.deque:
            print(-1)
        else:
            print(self.deque[0])
    
    def back(self):
        if not self.deque:
            print(-1)
        else:
            print(self.deque[-1])
            
            
    def check_order(self, order, value):
        if order == "push_front":
            self.push_front(value)
        elif order == "push_back":
            self.push_back(value)
        elif order == "pop_front":
            self.pop_front()
        elif order == "pop_back":
            self.pop_back()
        elif order == "size":
            self.size()
        elif order == "empty":
            self.empty()
        elif order == "front":
            self.front()
        elif order == "back":
            self.back()
            
deque = Deque()
# 명령의 수
N = int(sys.stdin.readline())
# 명령
orders = []
for _ in range(N):
    orders.append(sys.stdin.readline().strip())
    
for order in orders:
    try:
        x, y = order.split(" ")
        deque.check_order(x, y)
    except:
        deque.check_order(order, 0)