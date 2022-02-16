from typing import List


class Solution:
    # 네덜란드 3색 국기에 해당하는 문제
    # 3개의 포인터를 사용(red, white, blue)
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 삼색 국기
        # red는 1보다 작은값, blue는 1보다 큰값, white는 계속 움직이는 포인터
        red, white, blue = 0, 0, len(nums)

        while white < blue:
            # middle 값보다 작은 경우
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            # middle 값보다 큰 경우
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            # middle 값과 같은 경우
            else:
                white += 1

nums = [2,0,2,1,1,0]
solution = Solution()
print(solution.sortColors(nums))