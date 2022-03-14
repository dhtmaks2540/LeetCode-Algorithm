import collections

# k번만큼 글자를 바꿔서 가장 긴 반복글자
class Solution:
    # 투포인터, 슬라이딩 윈도우, Counter를 활용하여 문제 풀이
    def characterReplacement(self, s: str, k: int) -> int:
        # 왼쪽, 오른쪽 포인터
        left = right = 0
        counts = collections.Counter()
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            # 가장 흔하게 등장하는 문자 탐색
            max_char_n = counts.most_common(1)[0][1]
            
            # k 초과시 왼쪽 포인터 이동
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
                
        return right - left
    
s = "ABAB"
k = 2
solution = Solution()
print(solution.characterReplacement(s, k))