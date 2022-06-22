"""
2번 연산이나 3번 연산을 통해서 주어진 원소를 뽑는 연산의 최솟값을 출력하라

주어진 큐에서 원하는 목표값의 인덱스를 우선 파악한다(O(N)). 
1. 인덱스가 중간보다 앞에 있다면 2번 연산을 사용해서 목표값을 맨 앞으로 이동시키고 뽑아낸다.
or
2. 인덱스가 중간보다 뒤에 있다면 3번 연산을 사용해서 목표값을 맨 앞으로 이동시키고 뽑아낸다.
이 두 연산의 시간 복잡도 또한 O(N)에 해당한다.

따라서 최대 50개의 원소가 주어졌을 경우 50개의 원소에 대해서 O(2N)의 연산을 수행하는 것이므로
O(2N^2)이 최종 시간복잡도가 되고, 이는 O(N^2)에 해당한다. 시간 제한이 2초이기에 충분히 시간제한안에
풀이할 수 있다.

데크의 개념을 묻는 문제로 데크는 큐에서 더 발전해서 양쪽에서 삽입과 추출을 O(1)의 시간 복잡도를
가지는 연산을 수행할 수 있다.
"""

import sys
from collections import deque

# 큐의 크기, 뽑아내려 하는 수
N, M = map(int, sys.stdin.readline().strip().split(" "))
# 뽑아내려는 수
target_array = list(map(int, sys.stdin.readline().strip().split(" ")))
# Deque
queue = deque()
# 수 삽입
for i in range(1, N + 1):
    queue.append(i)
    
# 연산의 개수를 체크하는 변수
oper_cnt = 0
index = 0
    
while index < M:
    # 현재 목표값의 인덱스를 체크
    target_index = queue.index(target_array[index])
    
    # 중간보다 앞에 있다면 -> 2번 연산 사용
    if target_index <= len(queue) // 2:
        while queue[0] != target_array[index]:
            queue.append(queue.popleft())
            oper_cnt += 1
    # 중간보다 뒤에 있다면 -> 3번 연산 사용
    else:
        while queue[0] != target_array[index]:
            queue.appendleft(queue.pop())
            oper_cnt += 1
            
    # 목표값에 도달했으므로 큐에서 제거 및 다음 목표로 이동
    queue.popleft()
    index += 1
    
print(oper_cnt)