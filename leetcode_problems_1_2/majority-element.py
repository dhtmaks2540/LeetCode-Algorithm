from typing import List

import collections

class Solution:
    # Counter를 활용
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)

        return counter.most_common(1)[0][0]

    # 브루드 포스로 접근 -> 타임 아웃
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > len(nums) // 2:
                return num

    # 다이나믹 프로그래밍으로 최적화
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)
            
            if counts[num] > len(nums) // 2:
                return num

    # 분할 정복을 활용
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        print(f"a : {a}, b : {b}")

        """
        만약 a가 nums의 과반수를 차지하면 해당 인덱스는 1이됨
        (nums.count(a) > half에서 True를 반환하므로)
        -> a를 리턴(과반수인 엘리먼트)

        b가 과반수라면 False이므로 b를 리턴

        """
        return [b, a][nums.count(a) > half]

    # 파이썬 다운 방식
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]

nums = [2,2,1,1,1,2,2]
solution = Solution()
print(solution.majorityElement(nums))