"""
요세푸스 문제를 풀이하라

요세푸스는 순서대로 K번째 사람을 제거하는 문제이다. 사람들을 원으로 이루어져있다고 생각하고 N명의
사람들이 모두 제거되는 과정을 나타내는 문제인데, 이는 큐를 사용하면 쉽게 풀이할 수 있다.
예를 들어보면서 설명해보자. 문제와 같이 사람은 7명, 3번째 사람을 제거하라고 가정한다면
1,2,3,4,5,6,7과 같이 세워놓은 후 처음은 1부터 시작해 3번째 사람인 3이 제거되고, 그 후 4부터 시작해
3번째 사람인 6이 제거, 그 후 7부터 시작해 3번째 사람인 2제거하는 과정이 반복되는데 이를 그림을
그려서 생각해보면 Queue가 바로 떠오른다.

1. 1 2 3 4 5 6 7 에서 1과 2를 모두 poll한 후 push하고 세 번째인 3을 pop하면 세 번째 값이 된다.
2. 4 5 6 7 1 2 에서 4와 5를 모두 poll한 후 push하고 세 번째인 6을 pop하면 세 번째 값이 된다.
3. 7 1 2 4 5 에서 7과 2를 모두 poll한 후 push하고 세 번째인 2를 pop하면 세 번째 값이 된다.
...

위와 같은 과정을 N번 반복하게 되면 문제에서 원하는 요세푸스 순열이 되고 정답이 출력되는 것이다.
위의 과정의 시간 복잡도는 매번 O(1)의 연산을 K번 반복하므로 O(K)이고, 이 O(K)의 연산을 N번 반복하므로
총 시간 복잡도는 O(N * K)가 된다. 이는 두 수가 모두 최대 1,000이므로 최대 1,000,000의 시간복잡도가
걸리고 시간 제한 2초안에 문제를 충분히 풀이할 수 있다.

현재 문제는 큐를 응용하여 문제를 풀이하는데 사용할 수 있는지 묻는 문제인듯하다. 이 문제는 특히
그림을 그려서 풀이해보니 정답이 명확히 보였는데, 이러한 문제가 나오면 예시로 주어진 입력을 가지고
그림을 그려보며 규칙을 찾아내고, 이 규칙을 통해 제한된 시간안에 풀이할 수 있는 자료구조, 방법등을
찾는 것이 핵심 포인트같다.
"""

import collections
import sys

# 원소의 개수, 몇 번째 사람인지
N, K = map(int, sys.stdin.readline().strip().split(" "))
# 큐의 역할을 수행하는 Deque
queue = collections.deque()
# 순열 정답 변수
answer = []
# 큐에 숫자 삽입
for i in range(1, N + 1):
    queue.append(i)

cnt = 0
while queue:
    cnt += 1
    
    # 현재 K번째라면 제거
    if cnt == K:
        cnt = 0
        answer.append(queue.popleft())
    # K번째가 아니라면 뒤로 다시 넣기
    else:
        queue.append(queue.popleft())

print("<", end="")       
print(", ".join(map(str, answer)), end="")
print(">", end="")