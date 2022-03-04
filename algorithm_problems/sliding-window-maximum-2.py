from typing import List
import collections

class Solution:
    # brute-force로 접근 -> Time Limit Exceeded
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        for i in range(len(nums) - k + 1):
            max_value = max(nums[i : i + k])
            result.append(max_value)

        return result

    # deque를 활용하여 문제 풀이 -> Time Limit Exceeded
    """
    정렬되지 않은 슬라이딩 윈도우에서 최댓값으 추출하려면 어떠한 알고리즘이든 결국 한 번 이상은 봐야함
    따라서 최댓값 계산을 O(n) 이내로 줄일 수 있는 방법이 없어서 가급적 최댓값 계산을 최소화 하기위해
    이전의 최댓값을 저장해뒀다가 한 칸씩 이동할 때 새 값에 대해서만 더 큰값인지 확인하는 방식
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        current_max = float('-inf')
        for i, v in enumerate(nums):
            # 큐에 값 넣기
            window.append(v)
            if i < k - 1:
                continue

            # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v

            results.append(current_max)

            # 최댓값이 윈도우에서 빠지면 초기화
            if current_max == window.popleft():
                current_max = float('-inf')

        return results

    """
    https://leetcode.com/problems/sliding-window-maximum/discuss/65884/Java-O(n)-solution-using-deque-with-explanation
    
    1. If an element in the deque and it is out of i-(k-1), we discard them. We just neet to
    poll from the head, as we are using a deque and elements are ordered as sequence in the array

    2. Now only those elements within [i-(k-1), i] are in the deque. We then discard elements smaller than
    a[i] from the tail. This is because if a[x] < a[i] and x < i, then a[x] has no chance to
    be the :max" in [i-(k-1), i], or any other subsequent window: a[i] would always be a better candidate

    3. As a result elements in the deque are ordered in both sequence in array and their value.
    At each step the head of the deque is the max element in [i-(k-1), i]
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 예외처리
        if not nums:
            return []

        # 결과변수
        result = []
        # store index
        queue = collections.deque()

        # nums iterate
        for i in range(len(nums)):
            # out of the window - 1
            if queue and queue[0] < i - k + 1:
                queue.popleft()

            # remove smaller numbers in k range as they are useless - 2s
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            
            # append index
            queue.append(i)

            # append max num - 3
            if i > k - 2:
                result.append(nums[queue[0]])

        return result


nums = [1,3,-1,-3,5,3,6,7]
k = 3
nums = [1]
k = 1
solution = Solution()
print(solution.maxSlidingWindow(nums, k))