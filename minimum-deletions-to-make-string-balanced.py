class Solution:
    """
    https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/discuss/935464/Python-DP-or-O(n)-or-short-or-With-Explanation
    """
    def minimumDeletions(self, s: str) -> int:
        cnt_b = 0
        dp = [0]
        
        # a를 만날 경우
        # 이전에 만난 모든 b를 삭제하던가 -> total cost = count_of_b
        # 현재의 a를 삭제하던가 -> total_cost = cur_total_cost + 1

        for char in s:
            if char == 'b':
                cnt_b += 1
                dp.append(dp[-1])
            else:
                dp.append(min(cnt_b, dp[-1] + 1))

        return dp[-1]

    """
    https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/discuss/936436/JavaPython-3-Two-codes%3A-1-pass-and-2-passes-w-brief-explanation-and-analysis.
    """

    def minimumDeletions(self, s: str) -> int:
        cnt, stack = 0, []
        for c in s:
            if stack and stack[-1] == 'b' and c == 'a':
                stack.pop()
                cnt += 1
            else:
                stack.append(c)
        return cnt


s = "aababbab"
solution = Solution()
print(solution.minimumDeletions(s))