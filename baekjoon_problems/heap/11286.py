"""
우선순위큐를 응용하라

현재 문제는 절대값이 작다면 작은 값을 먼저 출력하고, 절대값이 같다면 원래 값이 작은 순서대로 출력하는
문제이다. 즉, 원소가 두 개 있는 자료구조를 사용하여 첫 번째 원소를 우선순위로 잡고 같으면 두 번째
원소를 우선순위로 잡도록 풀이해야한다. 파이썬은 heapq 라이브러리에서 컬렉션(리스트, 튜플 등...)을
넣으면 차례대로 원소들을 비교하며 최소힙으로 구현되어 있기에 그냥 사용하면 된다. 하지만 코틀린(자바)는
우선순위 큐에서 그러한 구현이 안되어있기 때문에 Comparator를 사용하여 이를 구현해줘야 한다.
따라서 최소힙을 구현하기 위한 람다식을 만든 후, Comparator에서 첫 번째 원소를 먼저 람다식으로
비교한 후 두번째 원소를 비교하도록 구현하면 된다.

우선순위 큐 라이브러리에 원소가 한 개가 아닌 두 개 이상이 들어갔을 경우 대처할 수 있는지 묻는 문제
인듯하다.

"""

import sys
import heapq

# 연산의 개수
N = int(sys.stdin.readline().strip())
queue = []

for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if not queue:
            print("0")
        else:
            abs_value, value = heapq.heappop(queue)
            print(value)
    else:
        heapq.heappush(queue, (abs(x), x))