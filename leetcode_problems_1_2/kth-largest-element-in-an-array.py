import heapq

class Solution:
    def findKthLargest(self, nums, k):
        # 우선순위 큐를 위한 리스트
        q = []
        # 최대 힙으로 측정하기 위해 음수로 삽입
        for num in nums:
            heapq.heappush(q, -num)

        index = 0

        # 큐가 비어있지 않으면
        while q:    
            # 인덱스 증가
            index += 1

            now = -heapq.heappop(q)

            if index == k:
                return now

    def findKthLargest(self, nums, k):
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)

        for _ in range(1, k):
            heapq.heappop(heap)

        return -heapq.heappop(heap)

    # heapify 활용
    # 주어진 자료구조가 힙 특성을 만족하도록 바꿔주는 연산
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)

        # k번째 최댓 값을 찾는 문제이므로
        # 길이에서 k를 뺀 만큼 반복
        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)

    # nlargest 활용(nsmallest도 존재)
    # k번째만큼 큰 값이 가장 큰 값부터 순서대로 리턴
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

    # 정렬 활용
    def findKthLargest(self, nums, k):
        return sorted(nums, reverse=True)[k - 1]