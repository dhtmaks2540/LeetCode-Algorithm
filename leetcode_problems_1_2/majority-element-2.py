from typing import List
import collections

"""
접근방법

주어진 리스트에서 요소가 n/2 times보다 더 많은 요소를 찾으라고 하며 무조건 존재한다고 하였다.
따라서 가장 많이 존재하는 요소가 문제의 정답일 것이라고 추측하여 Counter 또는 HashTable을 이용하여
해당 num값의 빈도수를 체크하고, 가장 많은 빈도수를 가진 원소를 반환하여 문제를 풀이하였다.

다만, 책의 챕터 주제인 분할 정복으로는 접근하지 못하였다.
분할까지는 접근하더라도 정복을 통해 문제를 풀이해야 하는데, 정복을 위한 코드를 떠올리지 못했다.
"""

# majority element를 찾는 문제로 majority element는 n/2 times 보다 더 나타나는 요소를 말한다.
# 단, 문제를 선형 시간과 O(1)의 공간을 가지고 풀이
class Solution:
    # Counter를 활용하여 문제 풀이
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)

        return counts.most_common(1)[0][0]

    # sort를 이용
    def majorityElement(self, nums: List[int]) -> int:
        # majority element는 n/2 times보다 더 나온다 하였으므로 중간 인덱스의 값은 majority element에 해당
        nums.sort()
        return nums[len(nums) // 2]

    # HashTable을 이용
    def majorityElement(self, nums: List[int]) -> int:
        dic = collections.defaultdict(int)

        for num in nums:
            dic[num] += 1
            if dic[num] > len(nums) // 2:
                return num

    # 책의 정답(다이나믹 프로그래밍으로 접근)
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)

            if counts[num] > len(nums) // 2:
                return num

    """
    해결방법

    이 문제를 푸는 방법은 여러가지 있지만 책에서 정한 이 문제의 풀이법인 분할 정복에 대해서 적기
    
    우선, nums 리스트를 쪼갤 수 있는 가장 작은 단위로 쪼갠다(분할)
    다만 분할에 따른 예외처리를 하기 위해서 분할전에 예외처리와 가장 작은 단위인 경우를 처리하고 
    a, b의 값으로 분할을 한다.

    정복은 문제를 푸는 조건에 해당하는데 해당 문제에서는 요소의 빈도수 중 n/2 이상인 요소를 찾으라 했다.
    따라서 a와 b의 값 중 현재 리스트에서 개수가 절반을 넘는 값을 반환하도록 하였다.
    이것이 정복에 해당하는데 푸는 방법은 여러가지가 있을 수 있다.
    책에서는 count를 계산하여 더 많은 값을 넘기는 방식으로 풀이를 한 것이다.

    해당 문제를 꼭 분할 정복으로 풀 필요는 없겠지만 언뜻보면 병합 정렬과 비슷하며
    분할 정복의 기초 문제라고 생각된다. 따라서 이 구조를 기억하고, 정복하는 코드를 잘 생각하며 문제를
    풀어야 겠다.

    """

    # 책의 정답(분할 정복을 이용)
    def majorityElement(self, nums: List[int]) -> int:
        # 예외 처리
        if not nums:
            return None
        # 원소가 1개라면 현재 원소 return
        if len(nums)== 1:
            return nums[0]

        half = len(nums) // 2
        # 분할
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        # 정복 및 조합
        return [b, a][nums.count(a) > half]

    """
    https://leetcode.com/problems/majority-element/discuss/51613/O(n)-time-O(1)-space-fastest-solution
    """
    def majorityElement(self, nums: List[int]) -> int:
        # 첫 번쨰 변수 대입
        # major는 빈도수가 가장 높은 변수
        major, count = nums[0], 1

        for i in range(1, len(nums)):
            # count가 0이라면. 즉, 빈도수가 더 높은 값이 나타난다면 갱신
            if count == 0:
                count += 1
                major = nums[i]
            # count가 0이 아니라면
            elif major == nums[i]: # major와 같다면
                count += 1
            else: # major와 다르다면
                count -= 1

        return major

    
nums = [3,2,3]
# nums = [2,2,1,1,1,2,2]
solution = Solution()
print(solution.majorityElement(nums))