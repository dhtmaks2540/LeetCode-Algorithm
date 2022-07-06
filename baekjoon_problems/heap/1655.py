"""
지금까지 말한 수 중에서 중간값을 말하는 프로그램을 작성해라

우선 주어지는 정수의 최대 개수가 100,000이고 시간제한은 0.1초이기 때문에 시간 복잡도가 O(N)까지 가지는
알고리즘으로 문제를 풀이해야 한다. 즉, 매번 정렬하는 방법으로는 절대 풀이할 수 없다.
파이썬이나 코틀린이나 결국 힙은 최소힙 또는 최대힙으로 활용할 수 밖에 없다. 즉, 하나의 힙을 사용해서
루트를 중간값으로 설정하는 방법은 없다는 것이다. 하지만 최소힙과 최대힙 두 개의 힙을 사용하면
중간값을 사용할 수 있다. 우선 left_heap과 right_heap이라는 두 개의 힙을 선언하고 left_heap에는
중간값보다 작거나 같은 수가 들어가고, right_heap에는 중간값보다 큰 값이 들어간다. 즉, left_heap에
중간값이 들어가게 되는 것이다. 이와 같이 설정을 하고 left_heap에는 중간값이 루트가 오게끔 설정해준다.

이제 전체적인 풀이 방법을 알아보자.

1. left_heap과 right_heap의 길이가 같다면 중간값이 존재해야하는 left_heap에 수를 넣는다. 하지만
길이가 같지 않다면 right_heap에 넣는다.

2. 만약 left_heap의 루트가 right_heap의 루트보다 크다면 두 루트의 값을 변경한다. 그 이유는 
right_heap은 중간값보다 큰 값들이 있어야 하기에 중간값보다 같거나 작은 값들인 left_heap에 큰
값이 있다면 오류가 생기기 때문이다.

위와 같이 구현을 하면 left_heap은 중간값보다 같거나 작은 최대힙이 되고, right_heap은 중간값보다
큰 최소힙이 되기에 중간값을 계속해서 left_heap 루트의 값으로 설정할 수 있게 되는 것이다.

현재 문제는 우선순위 큐를 응용할 수 있는지 묻는 문제이다. 우선 문제에서 계속해서 정렬되어 있다는 의미로
중간값을 계속해서 출력하라고 했기 때문에 우선순위 큐를 사용해야 한다는 생각은 떠올릴 수 있다. 하지만
한 개의 우선순위 큐로는 절대 풀이할 수 없으므로 이와 같이 두 개의 우선순위 큐를 응용하도록 심화된
문제이다. 단지 한 개만 응용하는 것이 아닌 여러 개를 사용할 수 도 있다는 것을 알아두자!
"""

import sys
import heapq

N = int(sys.stdin.readline().strip())

# 중간값이 저장되는 최대힙
left_heap = []
# 중간값보다 큰 값들이 저장되는 최소힙
right_heap = []
answer = []

for _ in range(N):
    value = int(sys.stdin.readline().strip())
    
    # left_heap과 right_heap의 길이가 같다면 left_heap에 값 추가
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -value)
    # 그렇지 않다면 right_heap에 값 추가
    else:
        heapq.heappush(right_heap, value)
        
    if left_heap and right_heap:
        # left_heap은 중간값보다 작거나 같은 값이 들어가야 하고 right_heap은 중간값보다 큰 값이
        # 들어가야 하기에 만약 아래와 같다면 두 개의 루트를 변경
        if -left_heap[0] > right_heap[0]:
            max_value = heapq.heappop(right_heap)
            min_value = -heapq.heappop(left_heap)
            
            heapq.heappush(right_heap, min_value)
            heapq.heappush(left_heap, -max_value)
            
    # 중간값은 left_heap의 루트에 저장     
    answer.append(-left_heap[0])
    
for value in answer:
    print(value)