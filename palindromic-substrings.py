class Solution:
    # 투 포인터를 이용하여 풀이
    def countSubstrings(self, s: str) -> int:
        # 팰린드롬 여부 확인
        def palindrome(left, right, count = 0):
            # left와 right 포인터를 이용하여 값이 같으면 늘려나가는 식으로
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            
            return count

        # 한 글자는 모두 팰린드롬이므로 문자의 길이만큼 일단 추가
        result = len(s)

        n = len(s)

        # 오른쪽 포인터 이동
        for i in range(n):
            # 짝수 팰린드롬
            result += palindrome(i, i + 1)
            # 홀수 팰린드롬
            result += palindrome(i, i + 2)

        return result

    # dp를 이용한 풀이
    def countSubstrings(self, s: str) -> str:
        # 한 글자에 해당
        result = len(s)
        n = len(s)

        dp = [[0] * n for _ in range(n)]

        # 대각선 True로 채우기(한 글자에 해당)
        for i in range(len(s)):
            dp[i][i] = True

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                """
                if len slicied sub_string is just one letter if the characters are equal,
                we can say they are palindomr dp[i][j] =True

                if the slicied sub_string is longer than 1, 
                then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                
                """
                # 글자가 같다면
                if s[i] == s[j]:
                    # j와 i의 차가 1이거나(바로 옆 글자거나)
                    # 자신의 안쪽도 팰린드롬이면 True
                    if j - i == 1 or dp[i + 1][j - 1] is True:
                        dp[i][j] = True
                        result += 1

        return result

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        res = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and ((j-i+1) < 3 or dp[i+1][j-1])
                res += dp[i][j]
        return res

s = "aaa"
solution = Solution()
print(solution.countSubstrings(s))