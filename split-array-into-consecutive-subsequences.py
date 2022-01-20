from typing import List
import collections

"""
https://leetcode.com/problems/split-array-into-consecutive-subsequences/
"""

class Solution:
    """
    https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/106514/C%2B%2BPython-Esay-Understand-Solution
    """
    
    # Hash Table과 그리디 알고리즘 사용
    def isPossible(self, A):
        left = collections.Counter(A)
        end = collections.Counter()
        for i in A:
            if not left[i]: continue
            left[i] -= 1

            # 가능하다면 i를 존재하는 subsequence로 넣기
            if end[i - 1] > 0:
                end[i - 1] -= 1
                end[i] += 1
            # 새로운 subsequence에 넣기(i + 1과 i + 2가 존재하면)
            elif left[i + 1] and left[i + 2]:
                left[i + 1] -= 1
                left[i + 2] -= 1
                end[i + 2] += 1
            # i를 어디에 둘지 모르면 False 반환
            else:
                return False
        return True

    """
    https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/106495/Java-O(n)-time-and-O(1)-space-solution-greedily-extending-shorter-subsequence
    """

    def isPossible(self, nums: List[int]) -> bool:
        # p1: number of length 1 sequence ending at previous value
        # p2: number of length 1 sequence ending at previous value
        # p3: number of length 3 sequence ending at previous value
        # prev: value of previous element
        prev, p1, p2, p3 = None, 0, 0, 0

        # one pass, O(n)
        i, n = 0, len(nums)
        while i < n:
            curr = nums[i]

            # count the number of appearances for current value
            count = 0
            while i < n and nums[i] == curr:
                count += 1
                i += 1

            # case 1: current value != previous value + 1
            if prev is None or curr != prev + 1:
                # there shall be no length 1 or 2 sequences ending at previous value
                if p1 or p2:
                    return False

                # c1: number of length 1 sequence ending at current value
                # c2: number of length 2 sequence ending at current value
                # c3: number of length 3 sequence ending at current value
                # the number of length 1 sequence ending at current value will
                # be equal to the total count of this element
                c1, c2, c3 = count, 0, 0

            else:
                # there shall be enough values to fill the previous length 1 and
                # length 2 sequences
                if p1 + p2 > count:
                    return False

                # highest priority will be given to previous length 1 sequences
                c2 = p1
                # then priority will be given to previous length 2 sequences
                # if there are still some remainings, to the previous length 3
                # sequences as well
                c3 = p2 + min(p3, count - (p1 + p2))

                # if there are even some values left after we fill length 1,2,3
                # sequences, then these values have to become the start of new
                # length 1 sequences
                c1 = max(0, count - p1 - p2 - p3)

            # update
            prev, p1, p2, p3 = curr, c1, c2, c3

        # in the end, there shall be no length 1 or 2 sequence unfilled
        return not p1 and not p2

nums = [1,2,3,3,4,5]
solution = Solution()
print(solution.isPossible(nums))