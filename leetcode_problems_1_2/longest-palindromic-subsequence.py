class Solution:
    # O(n) 공간 복잡도를 가진 다이나믹 프로그래밍
    def longestPalindromeSubseq(self, s: str) -> int:
        # 예외처리
        if len(s) < 2 or s == s[::-1]:
            return len(s)

        # 문자열의 길이
        n = len(s)
        # 0으로 초기화된 dp
        dp = [0 for _ in range(n)]
        # dp의 마지막은 1로 초기화
        dp[n - 1] = 1

        # 거꾸로 이터레이션
        for i in range(n - 1, -1, -1):
            newdp = dp[:]
            # 한 글자는 팰린드롬 이므로 1로 설정
            newdp[i] = 1

            # i + 1 부터 마지막 인덱스까지
            for j in range(i + 1, n):
                # i의 값과 j의 값이 같다면
                if s[i] == s[j]:
                    newdp[j] = 2 + dp[j - 1]
                # 다르다면
                else:
                    newdp[j] = max(dp[j], newdp[j - 1])
            # newdp의 변수 가르키기
            dp = newdp
        
        return dp[n - 1]

    # 탑다운 방식 dp -> 시간 초과
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        # 예외처리
        if n < 2 or s == s[::-1]:
            return n

        def dp(l, r):
            if l > r: return 0 # 빈 단어이므로 0 반환
            if l == r: return 1 # 1 글자를 가졌으므로 1 반환
            if s[l] == s[r]:
                return dp(l + 1, r - 1) + 2       
            return max(dp(l, r - 1), dp(l + 1, r))

        return dp(0, n - 1)

    # 보텀업 방식 dp
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        # 예외처리
        if n < 2 or s == s[::-1]:
            return n

        # 2차원 배열
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            print(f"back : {dp}")
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

            print(f"after : {dp}")

        return dp[0][n - 1]

        

s = "bbbab"
solution = Solution()
print(solution.longestPalindromeSubseq(s))