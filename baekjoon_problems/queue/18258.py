"""
큐를 구현하라는 문제이다.

큐는 스택의 후입선출과는 다르게 선입선출의 특징을 가지는 자료구조이다. 예시를 들면 놀이공원에서
표를 사기위해서 대기하는 사람들을 예시로 들 수 있고, 프린터의 대기 목록 등 많은 곳에서 사용하는
중이다. 이번 문제는 큐를 구현하는 문제로, 모든 연산이 O(1)의 시간복잡도를 가지도록 해야한다.
따라서 큐의 선입선출의 특징을 따라서 큐의 맨 앞에 있는 원소를 O(1)의 시간으로 poll 해야하고, 큐의 맨
뒤로 원소를 O(1)의 시간으로 push 해야한다. 파이썬이나 코틀린 모두 Deque라는 자료구조를 사용하면
쉽게 이를 구현할 수 있는데, Deque는 양쪽에서 모두 삽입하고 삭제하는데 O(1)의 시간 복잡도를 
가지는 연산으로 이를 수행할 수 있다. 따라서 이번 문제에서 Deque를 사용해서 풀이하였다.

큐를 구현할 수 있는지 묻는 문제로, 딱히 제한이 없으니 해당 언어의 큐를 구현하는 라이브러리를 아느냐고
묻는 문제인듯하다.
"""

from collections import deque
import sys

# 명령의 수
N = int(sys.stdin.readline().strip())
# 큐의 역할을 수행하는 데크
queue = deque()

for _ in range(N):
    now_order = sys.stdin.readline().strip()
    try:
        order, value = now_order.split(" ")
        queue.append(value)
    except:
        if now_order == "front":
            if not queue:
                print(-1)
            else:
                print(queue[0])
        elif now_order == "back":
            if not queue:
                print(-1)
            else:
                print(queue[-1])
        elif now_order == "empty":
            if not queue:
                print(1)
            else:
                print(0)
        elif now_order == "pop":
            if not queue:
                print(-1)
            else:
                print(queue.popleft())
        elif now_order == "size":
            print(len(queue))