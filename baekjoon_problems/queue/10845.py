"""
큐를 구현하라

파이썬의 deque를 사용해서 queue를 구현
"""

import collections
import sys

class Queue:
    def __init__(self):
        self.queue = collections.deque()
        
    def check_order(self, order, value):
        if order == "push":
            self.push(value)
        elif order == "pop":
            self.pop()
        elif order == "front":
            self.front()
        elif order == "back":
            self.back()
        elif order == "empty":
            self.empty()
        elif order == "size":
            self.size()
        
    def push(self, value):
        self.queue.append(value)
        
    def pop(self):
        if not self.queue:
            print(-1)
        else:
            print(self.queue.popleft())
        
    def size(self):
        print(len(self.queue))
    
    def empty(self):
        print(0 if self.queue else 1)
    
    def front(self):
        if not self.queue:
            print(-1)
        else:
            print(self.queue[0])
        
    def back(self):
        if not self.queue:
            print(-1)
        else:
            print(self.queue[-1])
        
# 명령의 수
N = int(sys.stdin.readline())
# 명령
array = []
for _ in range(N):
    array.append(sys.stdin.readline().strip())
    
queue = Queue()

for order in array:
    try:
        push_order, va = order.split(" ")
        queue.check_order(push_order, va)
    except:
        queue.check_order(order, 0)