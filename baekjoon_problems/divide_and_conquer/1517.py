import sys

"""
https://loosie.tistory.com/328
https://jaimemin.tistory.com/1157

버블 소트라고 문제에서 주어졌지만 데이터의 개수가 500,000개이므로 O(NlogN)의 시간복잡도를 가지는 
알고리즘으로 풀이해야 하는데 버블 소트는 이를 만족하지 못하므로 버블 소트를 사용해서는 해결할 수 없다.
세그먼트 트리와 병합 정렬을 사용해서 문제를 풀이할 수 있다고 하는데 세그먼트 트리의 개념은 아직 배우지를 못해서
풀이 방법을 모르겠다.. 

해당 문제는 병합 정렬을 사용해서 풀이할 수 있다. 따라서 병합 정렬의 과정을 똑같이 수행한다. 기본적으로 병합 정렬은 분할정복 문제이므로,
분할 -> 정복 -> 결합의 과정을 가진다. 따라서 우선 분할을 통해 더 이상 분해할 수 없을 때까지 리스트를
분해해준다. 이를 통해서 정복하는 과정에서 현재 두 리스트를 정렬시키면서 이를 정렬된 리스트에 저장하고
이를 다시 원래의 리스트에 갱신하는 방법으로 계속해서 정렬시켜준다. 다만, 분할된 두 정렬을 정복하면서
오른쪽 리스트의 값이 왼쪽 리스트의 값보다 작은 경우 swap하는 과정이 이루어짐을 파악할 수 있다. 이를 사용해서
mid를 기준으로 왼쪽의 inversion 개수를 파악해서 이를 더해주면 된다. 즉, 반전되어 있는 길이만큼
결과에 누적해주는 것이다.
"""

N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split(" ")))
len_array = len(array)
sorted_array = [0] * len_array
answer = 0

# i : 정렬된 왼쪽 리스트에 대한 인덱스
# j : 정렬된 오른쪽 리스트에 대한 인덱스
# k : 정렬된 리스트에 대한 인덱스
# 2개의 인접한 배열 list[left...mid]와 list[mid+1...right]의 합병 과정
# 실제로 숫자들이 정렬되는 과정
def merge(lis, left, mid, right):
    global answer
    
    i, j, k = left, mid + 1, left
    
    # 분할 정렬된 list의 합병
    while i <= mid and j <= right:
        # 순서대로 존재한다면 정렬된 리스트에 추가
        if lis[i] <= lis[j]:
            sorted_array[k] = lis[i]
            i += 1
        # 순서대로 존재하지 않는다면 mid를 기준으로 왼쪽의 inversion 개수 파악
        else:
            answer += (mid + 1 - i)
            sorted_array[k] = lis[j]
            j += 1
        k += 1
        
    # 남아 있는 값들을 일괄 복사
    if i > mid:
        for l in range(j, right + 1):
            sorted_array[k] = lis[l]
            k += 1
    else:
        for l in range(i, mid + 1):
            sorted_array[k] = lis[l]
            k += 1
    
    # 배열 sorted_array(임시 배열)의 리스트를 배열 lis로 재복사
    for l in range(left, right + 1):
        lis[l] = sorted_array[l]
        
# 병합 정렬
def merge_sort(lis, left, right):
    if left < right:
        # 중간 위치를 계산하여 리스트를 균등 분할 - 분할(Divide)
        mid = left + (right - left) // 2
        # 앞쪽 부분 리스트 정렬 - 정복(Conquer)
        merge_sort(lis, left, mid)
        # 뒤쪽 부분 리스트 정렬 - 정복(Conquer)
        merge_sort(lis, mid + 1, right)
        # 정렬된 2개의 부분 배열을 합병하는 과정 - 결합(Combine)
        merge(lis, left, mid, right)
        
merge_sort(array, 0, len_array - 1)
print(answer)