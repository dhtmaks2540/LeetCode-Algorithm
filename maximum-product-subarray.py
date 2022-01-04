from typing import List


class Solution:
    # 카데인 알고리즘 사용
    def maxProduct(self, nums: List[int]) -> int:
        prev_max = nums[0] # n - 1 까지의 max 값
        prev_min = nums[0] # n - 1 까지의 min 값
        max_to_n = nums[0] # n 까지의 max 값
        min_to_n = nums[0] # n 까지의 min 값
        ans = nums[0]

        for i in nums[1:]:
            # 이전의 max / min * 현재의 i 값 또는 i부터 재시작 
            # 최소값의 절대값이 더 클 수도 있으므로 저장
            max_to_n = max(max(prev_max * i, prev_min * i), i)
            min_to_n = min(min(prev_max * i, prev_min * i), i)
            prev_max = max_to_n
            prev_min = min_to_n
            ans = max(ans, max_to_n)

        return ans

    def maxProduct(self, nums: List[int]) -> int:
        ## 카데인 알고리즘을 사용하여 접근
        ## 시간 복잡도는 O(N)
        ## 공간 복잡도는 O(1)

        # 음수 * 음수가 더 큰 양수가 될 수 있기에 최소값도 따로 저장
        global_max = prev_max = prev_min = nums[0]
        
        for num in nums[1:]:
            curr_min = min(prev_max * num, prev_min * num, num)
            curr_max = max(prev_max * num, prev_min * num, num)
            global_max = max(global_max, curr_max)
            prev_max = curr_max
            prev_min = curr_min

        return global_max

nums = [2,-5,-2,-4,3]
solution = Solution()
print(solution.maxProduct(nums))