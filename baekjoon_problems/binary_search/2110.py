"""
가장 인접한 두 공유기 사이의 최대 거리를 출력하라

https://www.acmicpc.net/board/view/68623

좌표의 범위가 0 ~ 1000000000으로 완전 탐색으로는 절대 풀이할 수 없는 문제이다.
따라서 다른 방법을 생각해야 하는데 공유기를 설치하는 범위는 첫 번째 집부터 가장 마지막 집까지의 
범위에서 설치하는 것이므로 집들의 좌표를 정렬한 후 이분 탐색을 통해 풀이하면 O(NlogN + logN)의
시간복잡도로 풀이할 수 있다.

target(key)를 공유기의 설치된 개수로 두고 이분 탐색을 수행. 문제에서 최대 거리를 출력하라고 했으므로
하항식(low, start)를 늘리는 방식으로 풀이하면 된다(Upper Bound).
"""

import sys

# 집의 개수, 공유기의 개수
N, C = map(int, sys.stdin.readline().strip().split(" "))
# 집의 좌표
array = [int(sys.stdin.readline().strip()) for _ in range(N)]
# 이분 탐색을 위해 집의 좌표 정렬
array.sort()

# 공유기를 0으로 설치하는 경우는 없으니깐 시작점은 1
low = 1
# 최대 거리는 가장 큰 좌표 - 시작점
high = array[-1] - array[0]

while low <= high:
    mid = low + (high - low) // 2
    
    # 시작 위치 추가
    router_count = 1
    temp_sum = array[0]
    
    for index in range(1, N):
        if array[index] >= temp_sum + mid:
            router_count += 1
            temp_sum = array[index]
        
    if router_count < C:
        high = mid - 1
    elif router_count >= C:
        low = mid + 1
        
    # print(f"router_count : {router_count}, low : {low}, high : {high}, mid : {mid}")
        
print(low - 1)