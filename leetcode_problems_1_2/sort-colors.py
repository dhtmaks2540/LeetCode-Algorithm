from typing import List


class Solution:
    # 네덜란드 국기 문제
    # 두 개의 포인터를 사용
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 작은 값, 중앙 값, 큰 값의 인덱스
        red, white, blue = 0, 0, len(nums)
        
        # white와 blue가 겹칠 때 까지
        while white < blue:
            # 중앙 값보다 작다면
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            # 중앙 값보다 크다면
            elif nums[white] > 1:
                blue -= 1
                nums[blue], nums[white] = nums[white], nums[blue]
            # 중앙 값이라면
            else:
                white += 1
                
        
nums = [2,0,2,1,1,0]
solution = Solution()
solution.sortColors(nums)