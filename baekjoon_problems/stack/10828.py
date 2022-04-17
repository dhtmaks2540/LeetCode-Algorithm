"""
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 만들라.

스택을 구현할 수 있는지 묻는 문제로, 파이썬의 리스트는 스택의 모든 기능을 지원하므로
이를 사용해서 스택을 구현하였다. 스택의 가장 큰 특징은 FILO으로 가장 먼저 삽입된것이
가장 마지막에 나오는 구조를 가지고 있다.
"""

import sys

# 명령의 수
N = int(sys.stdin.readline())
# 명령
array = []
for _ in range(N):
    array.append(sys.stdin.readline().strip())

# 스택
class Stack:
    def __init__(self):
        self.arr = []
        
    def check_order(self, oper, value):
        if oper == "top":
            self.top()
        elif oper == "push":
            self.push(value)
        elif oper == "size":
            self.size()
        elif oper == "empty":
            self.empty()
        elif oper == "pop":
            self.pop()
        
    def size(self):
        print(len(self.arr))
        
    def empty(self):
        if len(self.arr) == 0:
            print(1)
        else:
            print(0)
            
    def push(self, num):
        self.arr.append(num)
        
    def pop(self):
        if len(self.arr) == 0:
            print(-1)
        else:
            value = self.arr.pop()
            print(value)
            
    def top(self):
        if len(self.arr) == 0:
            print(-1)
        else:
            print(self.arr[-1])
            
stack = Stack()

for oper in array:
    try:
        value = oper.split(" ")
        stack.check_order(value[0], value[1])
    except:
        stack.check_order(oper, 0)