import collections

# longest-repeating-character-replacement와 비슷

class Solution:
    # 투포인터, 슬라이딩 윈도우, Counter를 활용
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # left, right point
        left = right = 0
        # for maximum frequency char
        counts = collections.Counter()
        
        # move right index
        for right in range(1, len(answerKey) + 1):
            # 현재 문자열 기록
            counts[answerKey[right - 1]] += 1
            # 가장 흔하게 등장하는 문자 탐색
            most_char = counts.most_common(1)[0][1]
            
            # k초과시 왼쪽 포인터 이동
            if right - left - most_char > k:
                counts[answerKey[left]] -= 1
                left += 1
                
        return right - left
    
    """
    https://leetcode.com/problems/maximize-the-confusion-of-an-exam/discuss/1499049/JavaC%2B%2BPython-Sliding-Window-strict-O(n)
    """
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # max value, left pointer
        maxf = i = 0
        count = collections.Counter()
        for j in range(len(answerKey)):
            # 현재 포인터의 값 기록
            count[answerKey[j]] += 1
            # 최댓값 갱신(가장 많이 나오는 값으로)
            maxf = max(maxf, count[answerKey[j]])
            # 가장 많이 나온 값과 변경할 숫자(가장 긴 같은 값의 크기)보다 오른쪽 포인터 - 왼쪽 포인터가 크다면
            # 즉, 범위를 벗어난다면
            if j - i + 1 > maxf + k:
                count[answerKey[i]] -= 1
                i += 1
        return len(answerKey) - i
    
answerKey = "TTFTTFTT"
k = 1
solution = Solution()
print(solution.maxConsecutiveAnswers(answerKey, k))