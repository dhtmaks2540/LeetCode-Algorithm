from typing import List
import itertools

class Solution:
    # Combination과 Xor를 활용하여 문제 풀이 -> Time Limit Exceed
    def totalHammingDistance(self, nums: List[int]) -> int:
        result = 0
        # iterate in combination
        for num_pair in itertools.combinations(nums, 2):
            x, y = num_pair
            if x == y:
                continue
            # xor in num_pair and count '1'(different bit)
            result += bin(x ^ y).count('1')

        return result

    """
    https://leetcode.com/problems/total-hamming-distance/discuss/96226/Java-O(n)-time-O(1)-Space
    """
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        # 32 bit Integer
        for j in range(32):
            # 1의 숫자를 체크하기 위한 값
            bit_count = 0
            for i in range(n):
                # 해당 인덱스에서 1의 값 체크
                bit_count += (nums[i] >> j) & 1
            # 1의 개수 * 0의 개수(전체 nums의 개수 - 1의 개수)
            total += bit_count * (n - bit_count)

        return total

    """
    https://leetcode.com/problems/total-hamming-distance/discuss/96228/Python-Explanation
    
    Total hamming distance는 각각의 i번째 bit에 대한 hamming distance의 합이다

    {0, 1}로 선택된 숫자들로 이루어진 i번째 열을 생각해보자. total hanning distance는 
    서로 다른 숫자의 쌍이 될 것이다.
    
    따라서, i번째 비트의 Total hamming distance =
    i번째 위치의 0의 개수 *
    i번째 위치의 1의 개수 이다.
    """
    def totalHammingDistance(self, nums: List[int]) -> int:
        bits = [[0, 0] for _ in range(32)]

        for num in nums:
            for bit in bits:
                bit[num % 2] += 1
                num //= 2
        
        return sum(x * y for x,y in bits)

    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            ones = zeros = 0
            for n in nums:
                ones += (n >> i) & 1
                zeros += not (n >> i) & 1
            res += ones * zeros

        return res

# nums = [4,14,2]
# solution = Solution()
# print(solution.totalHammingDistance(nums))

for i in range(32):
    print((14 >> i) & 1)