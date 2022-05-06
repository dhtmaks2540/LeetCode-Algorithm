array = [21, 10, 12, 20, 25, 13, 15, 22]
len_array = len(array)
sorted_array = [0] * len_array

# i : 정렬된 왼쪽 리스트에 대한 인덱스
# j : 정렬된 오른쪽 리스트에 대한 인덱스
# k : 정렬될 리스트에 대한 인덱스
# 2개의 인접한 배열 list[left...mid]와 list[mid+1...right]의 병합 과정
# 실제로 숫자들이 정렬되는 과정
def merge(lis, left, mid, right):
    i, j, k = left, mid + 1, left
    
    # 분할 정렬된 list의 합병
    while i <= mid and j <= right:
        if lis[i] <= lis[j]:
            sorted_array[k] = lis[i]
            i += 1
        else:
            sorted_array[k] = lis[j]
            j += 1
        k += 1
        
    # 남아 있는 값들을 일괄 복사
    if i > mid:
        for l in range(j, right + 1):
            sorted_array[k] = lis[l]
            k += 1
    # 남아 있는 값들을 일괄 복사
    else:
        for l in range(i, mid + 1):
            sorted_array[k] = lis[l]
            k += 1
            
    # 배열 sorted_array(임시 배열)의 리스트를 배열 lis로 재복사
    for l in range(left, right + 1):
        lis[l] = sorted_array[l]
        
# 합병 정렬
def merge_sort(lis, left, right):
    if left < right:
        # 중간 위치를 계산하여 리스트를 균등 불할 - 분할(Divide)
        mid = left + (right - left) // 2
        # 앞쪽 부분 리스트 정렬 - 정복(Conquer)
        merge_sort(lis, left, mid)
        # 뒤쪽 부분 리스트 정렬 - 정복(Conquer)
        merge_sort(lis, mid + 1, right)
        # 정렬된 2개의 부분 배열을 합병하는 과정 - 결합(Combine)
        merge(lis, left, mid, right)
        
# 합병 정렬 수행(left: 배열의 시작 = 0, right: 배열의 끝 = 배열의 길이 - 1)
merge_sort(array, 0, len_array - 1)

# 정렬 결과 출력
for value in array:
    print(value)