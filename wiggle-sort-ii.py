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
        
    def wiggleSort(self, nums):
        nums.sort()
        half = len(nums[::2]) - 1
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]