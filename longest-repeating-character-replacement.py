import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 왼쪽, 오른쪽 포인터
        left = right = 0
        counts = collections.Counter()

        # 오른쪽 포인터를 이동하며
        for right in range(1, len(s) + 1):
            # 글자 count 추가
            counts[s[right - 1]] += 1
            # 가장 흔하게 등장하는 문자 탐색
            max_char_n = counts.most_common(1)[0][1]

            # k 초과시 왼쪽 포인터 이동
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1

        return right - left

    def characterReplacement(self, s: str, k: int) -> int:
        # 왼쪽 포인터
        left = result = 0
        counts = collections.Counter()

        # 오른쪽 포인터
        for right in range(len(s)):
            counts[s[right]] += 1
            # 가장 흔하게 등장하는 문자 탐색
            max_char_n = counts.most_common(1)[0][1]

            # k 초과시 왼쪽 포인터 이동
            if right - left + 1 - max_char_n > k:
                counts[s[left]] -= 1
                left += 1

            # 최댓값을 계산하여 가독성 높이기
            result = max(result, right - left + 1)

        return result

        
solution = Solution()
s = "AABABBA"
k = 1
print(solution.characterReplacement(s, k))