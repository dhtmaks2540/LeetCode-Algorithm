"""
스코빌 지수를 담은 배열과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기
위해 섞어야 하는 최소 횟수를 return 하라

모든 음식이 스코빌 지수 K를 만족하지 않는다면 가장 낮은 두 개의 음식을 가져와서 공식을 사용해
새로운 스코빌로 만들라고 나와있다. 즉, 계속해서 값이 정렬이 되어 있으면 쉽게 풀 수 있다는 의미인데
매번 계산을 할 때 마다 정렬을 하면 scoville의 길이가 최대 1,000,000이므로 기본적으로 계산을 하는데만
시간 복잡도가 O(1,000,000 * 1,000,000 log 1,000,000)이 된다. 따라서 이와 같이 풀이할 수 없다.
여기서 매번 정렬되어 있다는 것에 집중하면 우선순위 큐를 떠올릴 수 있는데, 그중에서도 heapq를 사용하면
매우 쉽게 풀이할 수 있다. 파이썬에서의 heapq는 최소힙으로 구현이 되어 있어 매번 최상단의 값이
최소값으로 유지되어있다. 따라서 이 값을 사용해서 모든 음식이 스코빌 지수 K를 넘는지 판단할 수 있고,
넘지 않는다면 새로운 공식을 사용해서 스코빌 지수를 올린 후 다시 삽입하는 방식으로 풀이할 수 있다.

이번 문제를 통해 가장 작은 값을 매번 가져온다와 같은 매번 정렬되어 있다는 개념을 만나면 heapq를 우선
생각해보도록 떠올리면 좋을 것 같다. 그렇게 되면 시간 복잡도를 더 줄일 수 있기 때문이다. 또한
heapq의 최상단 값은 최솟값을 나타내므로 이를 사용해서도 모든 원소가 어떠한 대소비교를 만족하는지를
판단할 수 있다.
"""

import heapq

def solution(scoville, K):
    answer = 0
    
    queue = []
    # 스코빌 지수 heapq에 삽입
    for value in scoville:
        heapq.heappush(queue, value)
        
    while queue:
        # 현재 가장 작은 값이 K보다 크거나 같다는 것은
        # 최소힙이므로 나머지 모든 값들도 K보다 크거나 같다는 뜻 -> 정답 출력
        if queue[0] >= K:
            return answer
        else:
            # 현재 남아있는 값이 2개 이상이라면
            if len(queue) >= 2:
                # 섞은 후 heapq에 다시 삽입
                answer += 1
                
                first_min_value = heapq.heappop(queue)
                second_min_value = heapq.heappop(queue)
                
                mix_value = first_min_value + (second_min_value * 2)
                heapq.heappush(queue, mix_value)
            # 그렇지 않다면 만들 수 없는 경우이므로 종료
            else:
                break
    
    return -1

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))