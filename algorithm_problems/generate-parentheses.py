from typing import List


class Solution:
    """
    https://leetcode.com/problems/generate-parentheses/discuss/10096/4-7-lines-Python
    https://leetcode.com/problems/generate-parentheses/discuss/10110/Simple-Python-DFS-solution-with-explanation
    """
    # 재귀 구조로 접근 - DFS(이취코 +,-,*,/ 문제와 비슷)
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(p, left, right, parens=[]):
            # 왼쪽의 값이 있다면 왼쪽 괄호 추가 후 left - 1
            if left: generate(p + "(", left - 1, right)
            # 오른쪽 값이 왼쪽 보다 크다면 오른쪽 괄호 추가 후 right - 1
            if right > left: generate(p + ")", left, right - 1)
            # 오른쪽 값이 없다면 리스트에 값 추가
            if not right: parens += p,
            return parens

        # 빈 문자열과 왼쪽 괄호의 개수, 오른쪽 괄호의 개수
        return generate('', n, n)

    """
    https://leetcode.com/problems/generate-parentheses/discuss/10369/Clean-Python-DP-Solution
    """
    # 다이나믹 프로그래밍을 사용(보텀업 방식)
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]         

n = 3
solution = Solution()
print(solution.generateParenthesis(n))