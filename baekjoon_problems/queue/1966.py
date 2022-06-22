"""
queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내라.

중요도라는 말이 나와서 Queue를 사용하지 않고 heapq를 사용하여 풀 수 있는지 생각해봤는데 같은 값이
있는 경우 heapq는 먼저 나온 것을 먼저 처리하지만, 현재 문제는 그렇지 않기에 heapq를 사용하지 않고
단지 문제에서 나온대로 queue를 사용하여 구현하였다. 우선 중요도를 내림차순으로 정렬한 후, 현재 큐의
최상단 값과 비교하여 값이 다르다면 현재 최상단 값을 pop 한 후 다시 push 한다. 만약 값이 같다면
현재 값을 pop하고 몇 번째 순서인지를 체크해준다. 이때, 찾아야 하는 문서라면 몇 번째로 출력됬는지
순서를 출력해주면 문제의 정답이 된다.

위에서 heapq를 사용하면 안되는 이유를 예로 들어보자. 문제에서 입력으로 주어진 (1,1,9,1,1,1)을
heapq로 사용하여 처리한다면 2번 인덱스의 9가 가장 먼저 나오게 되고, 그 다음은 0번 인덱스의 1이
나오게 된다. 따라서 문제에서 찾는 문서이기에 2가 정답으로 나오지만 문제의 정답은 5번이다. 그 이유는
현재 자신보다 중요도가 높은 문서가 하나라도 있다면, 현재 문서를 인쇄하지 않고 Queue의 가장
뒤에 배치하기 때문이다. 따라서 0번, 1번 인덱스의 1이 큐의 뒤로 간 후, 2번 인덱스의 9가 출력된 후
모두 중요도가 1이기에 차례대로 출력되므로 2 -> 3 -> 4 -> 5 -> 0 -> 1 순으로 출력이 되고
0번 문서는 5번째로 출력되게된다.

queue의 개념을 알고 있는지와 이를 문제에 적용할 수 있는지 묻는 문제인듯하다. 또한 문제의 조건을
잘 파악해서 구현해야하는 것이 포인트이다.

"""

import sys
from collections import deque

# 테스트케이스
T = int(sys.stdin.readline().strip())

for _ in range(T):
    # 문서의 개수, 확인해야 하는 문서
    N, M = map(int, sys.stdin.readline().strip().split(" "))
    # 중요도
    array = list(map(int, sys.stdin.readline().strip().split(" ")))
    # 큐의 역할을 수행할 Deque
    queue = deque()
    # 중요도 내림차순
    importance_array = sorted(array, reverse=True)
    
    for index in range(N):
        queue.append((array[index], index))
        
    cnt = 0
    index = 0
    
    while queue:
        # 현재 큐의 최상단이 가장 높은 우선순위를 가진 경우
        if queue[0][0] == importance_array[index]:
            # 출력 처리
            cnt += 1
            index += 1
            importance, now_index = queue.popleft()
            # 목표값과 같다면
            if now_index == M:
                print(cnt)
                break
        # 최상단이 가장 높은 우선순위가 아닌 경우
        else:
            queue.append(queue.popleft())