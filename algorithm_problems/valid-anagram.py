class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 정렬한 후 비교
        return sorted(s) == sorted(t)

s = "rat"
t = "car"

solution = Solution()
print(solution.isAnagram(s, t))