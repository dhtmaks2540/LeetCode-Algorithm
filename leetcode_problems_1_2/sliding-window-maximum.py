from typing import List
import collections


class Solution:

    # 브루드 포스로 접근 -> 시간 초과
    """
    아래의 브루드 포스 정답코드와 비교하면
    for문을 사용하면 될것을 쓸데없이 인덱스를 사용함..

    코드는 항상 깔끔하게 작성하는 것이 중요..

    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        
        back_index = 0
        next_index = k

        while next_index <= len(nums):
            result.append(max(nums[back_index:next_index]))
            back_index += 1
            next_index += 1

        return(result)

    # 브루드 포스로 접근 -> 시간 초과
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums

        r = []

        for i in range(len(nums) - k + 1):
            r.append(max(nums[i:i + k]))

        return r

    # 큐를 이용한 최적화
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        current_max = float('-inf')
        for i, v in enumerate(nums):
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
            # 즉, 범위를 벗어나면 다시 최댓값을 구하기 위해서 초기화
            if current_max == window.popleft():
                current_max = float('-inf')

        return results

    # 큐를 이용한 최적화 - 2
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = collections.deque()
        for i, num in enumerate(nums):
            # 윈도우(deque)에 값이 존재하고 현재값이 가장 마지막에 들어간 값보다 크다면
            while window and num >= nums[window[-1]]:
                window.pop()
            # 윈도우에 값 넣기
            window.append(i)
            
            if i + 1 >= k:
                res.append(nums[window[0]])
            
            if i - window[0] + 1 == k:
                window.popleft()
        
        return res

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
# Checking for base case
        if not nums:
            return []
        if k == 0:
            return nums
# Defining Deque and result list
        deq = collections.deque()
        result = []
        
# First traversing through K in the nums and only adding maximum value's index to the deque.
# Note: We are olny storing the index and not the value.
# Now, Comparing the new value in the nums with the last index value from deque,
# and if new valus is less, we don't need it

# 가장 먼저 k번 만큼 이터레이션하면서
# 가장 큰 값의 인덱스를 데크에 저장
        for i in range(k):
            while len(deq) != 0:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break

            deq.append(i)
            
# Here we will have deque with index of maximum element for the first subsequence of length k.
	
# Now we will traverse from k to the end of array and do 4 things
# 1. Appending left most indexed value to the result
# 2. Checking if left most is still in the range of k (so it only allows valid sub sequence)
# 3. Checking if right most indexed element in deque is less than the new element found, if yes we will remove it
# 4. Append i at the end of the deque  (Not: 3rd and 4th steps are similar to previous for loop)
 
        for i in range(k, len(nums)):
            # 가장 큰 값 넣기
            result.append(nums[deq[0]])
            
            # k의 범위를 벗어난다면 버리기
            if deq[0] < i - k + 1:
                deq.popleft()
            
            # 새로 나타난 값이 데크의 오른쪽부터 검사해서 그 값보다 크다면
            # 작은 값들 빼버리기
            while len(deq) != 0:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            
            deq.append(i)
        
#Adding the maximum for last subsequence
        result.append(nums[deq[0]])
        
        return result



nums = [1,3,-1,-3,5,3,6,7]
k = 3

solution = Solution()
print(solution.maxSlidingWindow(nums, k))