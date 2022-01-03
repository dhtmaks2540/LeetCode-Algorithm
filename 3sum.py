from typing import List


class Solution:
    # 로 접근
    # 투 포인터는 대개 정렬이 되어있어야 하기에 정렬수행
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # 예외처리
        if n < 3:
            return []

        # 정렬 수행
        nums.sort()

        result = []

        for index, num in enumerate(nums):
            # 왼쪽, 오른쪽 포인터
            left, right = index + 1, n - 1
            # 왼쪽이 오른쪽보다 작은 동안
            while left < right:
                # 0이면 추가
                if num + nums[left] + nums[right] == 0:
                    if [num, nums[left], nums[right]] not in result:
                        result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                # 0보다 크면 오른쪽 포인터 이동
                elif num + nums[left] + nums[right] > 0:
                    right -= 1
                # 0보다 작으면 왼쪽 포인터 이동
                else:
                    left += 1

        return result

    # 브루드 포스로 접근 -> 시간초과
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        # 브루트 포스 n^3 반복
        for i in range(len(nums) - 2):
            # 중복된 값 건너 뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i], nums[j], nums[k]])

        return results

    # 투 포인터 사용
    # 직접 푼 문제에서 중복된 값은 건너뛰는 코드를 추가하여 최적화
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 간격을 좁혀가며 합 sum 계산
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # sum이 0인 경우이므로 정답 및 스킵 처리
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

        return results
    

nums = [-1,0,1,2,-1,-4]
solution = Solution()
print(solution.threeSum(nums))