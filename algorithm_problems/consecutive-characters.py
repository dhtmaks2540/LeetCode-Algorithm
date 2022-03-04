# 하나의 문자로 이루어진 가장 긴 문자열
class Solution:
    """
    이전 인덱스의 값을 기록하여 현재의 인덱스의 값과 비교
    그 값이 같으면 frequency를 계속해서 증가, 아니면 처음부터 시작하는 방식으로 풀이
    """
    def maxPower(self, s: str) -> int:
        # max frequency of char, temp frequency of char
        max_freq = temp_freq = 1
        # now char
        now_char = s[0]
        
        # compare the char from the second one.
        for i in range(1, len(s)):
            if now_char == s[i]:
                temp_freq += 1
            else:
                temp_freq = 1

            # update now char
            now_char = s[i]
            max_freq = max(max_freq, temp_freq)

        return max_freq

    """
    https://leetcode.com/problems/consecutive-characters/discuss/635269/JavaPython-3-Simple-code-w-brief-explanation-and-analysis.
    
    1. Increase the counter by 1 if current char same as the previous one. otherwise, reset the counter to 1.
    2. Update the max value of the counter during each iteration.
    """
    def maxPower(self, s: str) -> int:
        cnt = ans = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
                ans = max(cnt, max)
            else:
                cnt = 1

        return ans

s = "leetcode"
solution = Solution()
print(solution.maxPower(s))