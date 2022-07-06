"""
최소힙 라이브러리를 사용해봐라

최소힙은 루트 노드가 가장 작은 값이 있는 특수한 형태의 트리이다. 파이썬에서는 heapq가 기본적으로
최소힙으로 구현되어 있고, 코틀린(자바)에서는 PriorityQueue가 최소힙으로 구현되어있다. 이 둘을
사용해서 문제를 풀이할 수 있다.

현재 문제는 최소힙 라이브러리를 해당 언어에서 사용할 수 있는지 묻는 문제인듯하다.
"""

import sys
import heapq

queue = []

# 연산의 개수
N = int(sys.stdin.readline().strip())
for _ in range(N):
    # 연산
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if not queue:
            print("0")
        else:
            print(heapq.heappop(queue))
    else:
        heapq.heappush(queue, x)