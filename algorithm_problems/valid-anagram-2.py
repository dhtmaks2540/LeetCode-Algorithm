class Solution:
    """
    문자열을 정렬 후 비교하게 되면 같은 값을 가지고 있는지 확인할 수 있기에 정렬 후 비교
    """
    # 정렬을 이용하여 문제 풀이
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    # 정렬을 이용하여 문제 풀이
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s = sorted(s)
        t = sorted(t)

        for i in range(len(s)):
            if s[i] != t[i]:
                return False

        return True
    """
    https://leetcode.com/problems/valid-anagram/discuss/66499/Python-solutions-(sort-and-dictionary).
    """
    # dict(HashTable)을 사용
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}

        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        for j in t:
            if j not in dic:
                return False
            else:
                dic[j] -= 1

        for val in dic.values():
            if val != 0:
                return False

        return True


s = "anagram"
t = "nagaram"
solution = Solution()
print(solution.isAnagram(s, t))