"""
두 수열의 연속된 부분 수열의 합이 목표값이 되는 모든 방법의 가지 수를 출력하라

https://jaimemin.tistory.com/1110

아래에서 사용된 알고리즘은 다음과 같다.
1. 우선 A 피자와 B 피자의 모든 가능한 합을 미리 전처리(subSum_A, subSum_B)해준다.
2. subSum_A[i]에 대해 lower_bound와 upper_bound를 사용해서 B 피자의 전처리된 값에서
(target - subSum[i])가 몇 개 있는지 확인하고 결과에 더한다.

우선 연속된 부분 수열을 미리 전처리 처리하려고 했으나 생각해내지 못했다.. 그리고 Upper Bound와 
Lower Bound에 대한 개념도 정확히 모르니 아예 풀이 방법을 떠올리지 못했다... 하나의 개념도
정확히 알고 그것에 대한 응용을 생각하자
"""

import sys
import bisect

# 목표값
target = int(sys.stdin.readline().strip())
# 피자 조각의 개수
A, B = map(int,sys.stdin.readline().strip().split(" "))
# 피자 조각의 크기
array_A = []
array_B = []

for _ in range(A):
    array_A.append(int(sys.stdin.readline().strip()))

for _ in range(B):
    array_B.append(int(sys.stdin.readline().strip()))

# 아무 원소도 포함하지 않은 상황으로 0을 미리 삽입
subSum_A, subSum_B = [0], [0]

# 전처리(A)
low = high = interval_sum = 0

while low < A:
    # high 인덱스의 값 추가
    interval_sum += array_A[high]
    high += 1
    
    # 목표값보다 작다면 포함
    if interval_sum <= target:
        subSum_A.append(interval_sum)
    # 목표값보다 크다면 low를 1 증가시키고 다시 시작
    else:
        low += 1
        high = low
        interval_sum = 0
        
    # 원형 배열(마지막 인덱스를 넘어섰다면 0으로 이동)
    if high == A:
        high = 0
        
    # 전체 다 더한 값 중복 방지(둘다 0이거나 high의 위치가 low - 1이라면)
    if (not low and not high) or high + 1 == low:
        low += 1
        high = low
        interval_sum = 0
        
low = high = interval_sum = 0

# 전처리(B)
while low < B:
    interval_sum += array_B[high]
    high += 1
    
    if interval_sum <= target:
        subSum_B.append(interval_sum)
    else:
        low += 1
        high = low
        interval_sum = 0
        
    # 원형 배열
    if high == B:
        high = 0
    # 전체 다 더한 값 중복 방지
    if (not low and not high) or high + 1 == low:
        low += 1
        high = low
        interval_sum = 0

# 이분 탐색을 수행하기 위해서 정렬   
subSum_A.sort()
subSum_B.sort()

answer = 0

# Lower Bound, Upper Bound 구하기
for i in range(len(subSum_A)):
    # Lower Bound
    low = bisect.bisect_left(subSum_B, target - subSum_A[i])
    # Upper Bound
    high = bisect.bisect_right(subSum_B, target - subSum_A[i])
    
    print(f"low : {low}, high : {high}, target : {target}, value : {subSum_A[i]}")
    
    # Upper Bound - Lower Bound를 계산하여 target - subSum_A[i]의 값이 subSum_B에 몇개 있는지 확인
    answer += high - low
    
print(answer)