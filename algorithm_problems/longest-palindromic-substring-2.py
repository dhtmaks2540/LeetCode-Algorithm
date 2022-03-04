class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 마지막에 left의 값을 1 빼므로 1 더해서 반환
            return s[left + 1: right]

        # 해당 사항이 없을 때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ""

        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            # 짝수와 홀수 팰린드롬 확인
            result = max(result, expand(i, i + 1), expand(i, i + 2), key = len)

        return result

    # 다이나믹 프로그래밍 방식
    """
    
    https://leetcode.com/problems/longest-palindromic-substring/discuss/900639/Python-Solution-%3A-with-detailed-explanation-%3A-using-DP
    
    """
    def longestPalindrome(self, s: str) -> str:
        longest_palindrom = ''
        dp = [[0]*len(s) for _ in range(len(s))]
        # 대각선 True로 채우기(한 글자에 해당)
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]

        # dp 테이블 채우기
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)):
                """
                if len slicied sub_string is just one letter if the characters are equal,
                we can say they are palindomr dp[i][j] =True

                if the slicied sub_string is longer than 1, 
                then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                
                """
                if s[i] == s[j]:
                    if j-i ==1 or dp[i+1][j-1] is True:
                        dp[i][j] = True

                        # maximum palindrome sequence
                        if len(longest_palindrom) < len(s[i:j+1]):
                            longest_palindrom = s[i:j+1]

        return longest_palindrom


s = "babad"
solution = Solution()
print(solution.longestPalindrome(s))