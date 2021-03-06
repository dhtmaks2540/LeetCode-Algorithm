"""
가장 긴 증가하는 부분 수열을 구하라

가장 긴 증가하는 부분 수열 문제는 DP 또는 이분 탐색을 통해 문제를 풀이할 수 있다. DP의 시간 복잡도
는 수열의 개수만큼 현재 인덱스 - 1번을 탐색해야 하므로 O(1 + 2 + 3 + ... + N - 1)이므로
O((N - 1) * N / 2) = O((N^2 - N) / 2) 이므로 최종 시간복잡도는 O(N^2)이 된다. 하지만 현재
문제는 수열 A의 최대 크기가 1,000,000이므로 DP를 통해 풀이하면 시간 제한안에 절대 풀이할 수 없다.
따라서 이분 탐색을 통해 풀이해야 한다.

방법은 다음과 같다. 탐색을 수행하는 배열은 오름차순으로 정렬되어 있는 최장 증가 부분 수열을 기록하는
곳이다. 그리고 찾으려는 값은 만약 현재 값이 가장 최근에 저장된 값보다 크다면 단지 추가하고, 작다면
그 값이 들어갈 위치를 찾아 갱신하는 것이다.

이분 탐색에서 중복된 값이 없는 경우는 단지 이분 탐색 코드 그대로를 사용해서 탐색값을 찾아나가는
방법으로 풀이할 수 있다. 하지만 중복된 값이 있는 경우는 Lower Bound(하한값) 또는 Upper Bound(상한값)
을 사용해서 문제를 풀이해야 하는데, Lower Bound는 목표값보다 같거나 큰값이 처음 나온 인덱스를 나타내고
Upper Bound는 목표값보다 처음으로 큰 값이 나오는 인덱스를 리턴하는 알고리즘이다.
예를 들어, {1,2,2,3,3,3,4,6,7}에 있어서 목표값을 3으로 잡고 Lower Bound는 3보다 같거나 큰 값이
처음으로 나오는 인덱스인 3이 답이 된다. 따라서 값이 같거나 큰 경우는 high를 계속해서 값을 계속해서
낮춰서 같거나 큰 값이 처음으로 나오도록 만들어 줘야 한다.
이와는 다르게 Upper Bound는 3보다 처음으로 큰 값이 나오는 인덱스인 6이 답이 된다. 이 경우는 큰 값을
찾아야 하므로 값이 같거나 작은 경우 low를 늘려서 큰 값을 찾도록 해야 한다.

현재 문제 LIS(최장 증가 부분 수열)은 위에서 설명한 듯이 DP와 이분 탐색을 통해 풀이할 수 있다.
여기서 이분 탐색을 응용할 수 있는 이유는 이분 탐색은 우선 정렬된 배열에서 목표값을 찾는다는
조건이 무조건 들어간다. 현재 문제의 답인 최장 증가 부분 수열은 정렬이 되어 있는 상태이다.
따라서 최장 증가 부분 수열을 탐색의 범위로 삼고 탐색의 대상은 주어진 배열의 값들로 선정하면 된다.
그리고 최장 증가 부분 수열에 마지막 값이 현재 값보다 작다면 단지 추가해서 최장 증가 부분 수열을 늘려주고,
그렇지 않다면 이분 탐색을 통해 값을 갱신해서 더 작은 값이 들어가도록 수행해주면 된다. 다만 여기서
원하는 값을 명확히 찾을 수 없기에 Lower Bound를 사용해서 현재 값과 같거나 큰 값이 처음으로
나오는 인덱스를 반환하도록 하는 방식으로 풀이하는 것이다.
"""

import sys

# Lower Bound 사용(주어진 값과 같거나 큰 값이 처음으로 나오는 인덱스 반환)
def binary_search(left, right, target):
    while left < right:
        mid = left + (right - left) // 2
        
        if target <= longest_array[mid]:
            right = mid
        else:
            left = mid + 1
            
    return left

# 수열의 크기
N = int(sys.stdin.readline().strip())
# 수열
array = list(map(int, sys.stdin.readline().strip().split(" ")))
# 가장 긴 부분 수열을 저장할 배열
longest_array = []
# 첫 번째 원소 추가
longest_array.append(array[0])

for i in range(1, N):
    # 마지막에 저장된 원소보다 현재 원소가 더 크다면 단지 추가
    if longest_array[-1] < array[i]:
        longest_array.append(array[i])
    # 그 밖의 경우는 갱신
    else:
        index = binary_search(0, len(longest_array), array[i])
        longest_array[index] = array[i]
        
print(len(longest_array))