from typing import List


class Solution:
    # 투 포인터를 이용하여 접근
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        # 정렬 수행
        nums.sort()

        # 첫 번째 값 지정
        for i in range(len(nums) - 3):
            # 중복이면 패스
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 두 번째 값 지정
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # 왼쪽, 오른쪽 포인터
                left, right = j + 1, len(nums) - 1

                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if sum < target:
                        left += 1
                    elif sum > target:
                        right -= 1
                    else:
                        # target과 같은 경우이므로 추가하고 스킵 처리
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1

        return result

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            
            # If we have run out of numbers to add, return res.
            # 리스트가 비었다면 res 반환
            if not nums:
                return res
            
            # There are k remaining values to add to the sum. The 
            # average of these values is at least target // k.
            average_value = target // k
            
            # We cannot obtain a sum of target if the smallest value
            # in nums is greater than target // k or if the largest 
            # value in nums is smaller than target // k.
            if average_value < nums[0] or nums[-1] < average_value:
                return res
            # 개수가 두개가 된면
            if k == 2:
                return twoSum(nums, target)

            # 한 값 정해서 이터레이션
            for i in range(len(nums)):
                # 중복된 값이 아니라면
                if i == 0 or nums[i - 1] != nums[i]:
                    # 정해진 값을 뺀 나머지를 재귀로 호출
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)
    
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            # 투 포인터
            lo, hi = 0, len(nums) - 1
    
            while (lo < hi):
                curr_sum = nums[lo] + nums[hi]
                # 합이 타겟보다 작거나 중복된 값이라면
                if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    # 왼쪽 포인터 이동
                    lo += 1
                # 합이 타겟보다 크거나 중복된 값이라면
                elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    # 오른쪽 포인터 이동
                    hi -= 1
                else:
                    # 같다면
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                                                         
            return res

        # 정렬수행
        nums.sort()
        return kSum(nums, target, 4)

nums = [-2,-1,-1,1,1,2,2]
target = 0

solution = Solution()
print(solution.fourSum(nums, target))