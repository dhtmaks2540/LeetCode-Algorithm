"""
배열이 주어질 때, X라는 수가 배열에 존재하는지 찾아라

배열의 최대 개수는 100,000이고 찾아야 하는 정수의 최대 개수는 100,000이다. 따라서 주어진 정수마다
O(N)의 시간 복잡도를 가지는 index 함수를 사용하면 100,000,000의 시간이 걸리게되어 절대 시간 제한내에
풀이할 수 없다. 따라서 다른 방법을 사용해야 하는데 이분 탐색을 사용하면 풀이할 수 있다. 이분 탐색은
O(logN)의 시간 복잡도가 걸리므로 100,000개의 원소에 100,000번의 탐색을 수행해도 총 시간 복잡도는
O(N * logN)의 시간이 걸리며 여기에 정렬의 시간 복잡도인 O(N * logN)을 더해도 O(2NlogN) = O(NlogN)
으로 문제를 풀이할 수 있다.'

"""

import sys

# 수의 개수
N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split(" ")))
# 이분 탐색을 수행하기 위해 정렬
array.sort()

# 탐색을 수행할 수들
M = int(sys.stdin.readline().strip())
target_array = list(map(int, sys.stdin.readline().strip().split(" ")))

def binary_search(start, end, target):
    while start <= end:
        mid = start + (end - start) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
            
    return -1

start, end = 0, N - 1
for target in target_array:
    index = binary_search(start, end, target)
    if index == -1:
        print(0)
    else:
        print(1) 