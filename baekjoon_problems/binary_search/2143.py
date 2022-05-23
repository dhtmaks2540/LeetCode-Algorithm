"""
두 배열이 주어졌을 때, 두 배열의 연속된 부분 수열의 합이 목표값이 되는 경우의 수를 구하라

2632번의 문제에서 조건이 조금 달라진 문제로 우선 각 배열의 개수가 최대 1000개이다.
따라서 미리 연속된 부분 배열의 합(subSum_A, subSum_B)을 모두 계산한다. 그리고 정렬을 수행한 후
subSum_A의 원소들을 iteration하면서 subSum_B에 target - 현재 subSum_A 원소의 Upper Bound와
Lower Bound를 구한다. 이렇게 되면 목표값을 만드는 개수가 출력되고 이를 계속해서 누적해나가며
풀이할 수 있다.

다만 이 문제는 양수뿐만 아니라 음수도 포함이 되므로 연속된 부분 수열의 모든 값을 기록하여
처리한다.
"""

import sys
import bisect

# 목표값
T = int(sys.stdin.readline().strip())
A = int(sys.stdin.readline().strip())
array_A = list(map(int, sys.stdin.readline().strip().split(" ")))
B = int(sys.stdin.readline().strip())
array_B = list(map(int, sys.stdin.readline().strip().split(" ")))

subSum_A = []
subSum_B = []

# 연속된 부분 수열 전처리
start = end = interval_sum = 0

while start < A:
    # 끝점을 마지막 인덱스까지 증가시키며 합 누적
    while end < A:
        interval_sum += array_A[end]
        subSum_A.append(interval_sum)
        end += 1

    # 시작점 1 증가
    start += 1
    end = start
    interval_sum = 0

# 연속된 부분 수열 전처리    
start = end = interval_sum = 0

while start < B:
    # 끝점을 마지막 인덱스까지 증가시키며 합 누적
    while end < B:
        interval_sum += array_B[end]
        subSum_B.append(interval_sum)
        end += 1
    
    # 시작점 1 증가
    start += 1
    end = start
    interval_sum = 0
    
answer = 0

# 이분 탐색을 수행하기 위해 정렬
subSum_A.sort()
subSum_B.sort()

for i in range(len(subSum_A)):
    # Lower Bound와 Upper Bound를 구해
    # 목표값에서 A의 연속된 부분 수열의 합 중 한 값을 구한 값이 있는지
    # 계산하여 그 값을 결과변수에 누적
    
    # 즉, subSum_A[i] + subSum_B[j] = T를 이분 탐색을 통해 수행한다
    lower_index = bisect.bisect_left(subSum_B, T - subSum_A[i])
    upper_index = bisect.bisect_right(subSum_B, T - subSum_A[i])
    
    answer += (upper_index - lower_index)
    
print(answer)