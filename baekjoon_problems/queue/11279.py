"""
최대힙을 사용해봐라

파이썬에서는 heapq 라는 최소힙 라이브러리가 있다. 힙은 가장 작은 값이 루트에 존재하는
트리의 구조를 가지게 된다. 힙은 대부분 0번 인덱스를 사용하지 않는 배열을 사용하여 구현하는데
그 이유는 부모 노드와 자식 노드의 관계를 인덱스를 통해 나타낼 수 있기 때문이다. 예를 들어 1번
인덱스의 자식 노드 중 왼쪽 노드는 인덱스 * 2에 해당하는 2번 인덱스의 노드가 되고, 오른쪽
노드는 인덱스 * 2 + 1에 해당하는 3번 인덱스의 노드가 된다. 그리고 원소의 삽입과 삭제에
있어서는 최상위의 노드가 최솟값을 가지는 노드가 유지되어야 하기 때문에 부모 노드와 자식 노드를
비교해가며 위치를 변경해야한다.

파이썬은 최소힙으로 구현되어 있으므로 최대힙으로 사용하기 위해서 값을 추가하거나 삭제하는 경우
-를 추가해준다.

현재 문제는 해당 언어에서 heap 라이브러리를 사용할 수 있는지 묻는 문제인듯하다.
"""

import sys
import heapq

# 연산의 개수 
N = int(sys.stdin.readline().strip())
# 최소힙
queue = []

for _ in range(N):
    # 연산
    x = int(sys.stdin.readline().strip())
    # 값이 0이라면 값을 출력 후 제거
    if x == 0:
        # 큐에 값이 있다면 제거
        if queue:
            print(-heapq.heappop(queue))
        else:
            print(0)
    else:
        heapq.heappush(queue, -x)