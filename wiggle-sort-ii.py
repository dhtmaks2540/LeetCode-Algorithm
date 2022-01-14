from typing import List


class Solution:
    """
    https://leetcode.com/problems/wiggle-sort-ii/discuss/77678/3-lines-Python-with-Explanation-Proof
    """  
    # 짝수에는 작은 수, 홀수에는 큰 수를 배치
    def wiggleSort(self, nums):
        # 정렬
        nums.sort()
        # 짝수 인덱스의 개수
        half = len(nums[::2])
        # 짝수, 홀수 = 중간 - 1 까지 거꾸로, 중간부터 거꾸로
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

        return nums
        
    def wiggleSort(self, nums):
        nums.sort()
        half = len(nums[::2]) - 1
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]

        return nums

    """
    https://leetcode.com/problems/wiggle-sort-ii/discuss/155764/Python-3-lines-simplest-solution-for-everyone-to-understand
    """

    def wiggleSort(self, nums):
        # 정렬 수행
        arr = sorted(nums)
        # 홀수에는 큰 수부터 배치(pop을 수행하기에 큰 수부터 나옴)
        for i in range(1, len(nums), 2): nums[i] = arr.pop() 
        # 짝수에는 나머지 수 배치(홀수보다는 작은 수가 배치됨)
        for i in range(0, len(nums), 2): nums[i] = arr.pop() 

nums = [2,2,2,1,5]
solution = Solution()
print(solution.wiggleSort(nums))