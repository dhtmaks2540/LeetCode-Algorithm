# 시간 복잡도는 n^2
# 배열 전체를 모두 살피는 것을 n번 하기때문에
def bubblesort(A):
    for i in range(len(A)):
        for j in range(0, len(A) - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


# 퀵 정렬
# 항상 맨 오른쪽의 피벗을 택하는 로무토 파티션
# 해당 퀵 정렬은 이미 정렬이 되어있는 경우는 시간 복잡도가 O(n^2)
# 퀵 정렬은 불안정 알고리즘에 해당
def quicksort(A, lo, hi):
    def partition(lo, hi):
        # 피벗은 오른쪽
        pivot = A[hi]
        left = lo
        for right in range(lo, hi):
            # 피벗의 값보다 right값이 더 작다면
            if A[right] < A[pivot]:
                # left와 right 스왑
                A[left], A[right] = A[right], A[left]
                # left 인덱스 증가
                left += 1
        # 피벗의 값과 left 값을 바꾼 후 left(pivot)을 반환
        A[left], A[hi] = A[hi], A[left]
        return left

    if lo < hi:
        pivot = partition(lo, hi)
        quicksort(A, lo, pivot - 1)
        quicksort(A, pivot + 1, hi)