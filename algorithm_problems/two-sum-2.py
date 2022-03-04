class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, num in enumerate(nums):
            temp = target - num
            
            if temp in nums[index + 1:]:
                return [index, nums[index + 1:].index(temp) + (index + 1)]

    # 키를 사용
    def twoSum(self, nums, target):
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            # target - num의 값이 존재하고 같은 값이 아니라면
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]

nums = [2,7,11,15]
target = 9

solution = Solution()
print(solution.twoSum(nums, target))