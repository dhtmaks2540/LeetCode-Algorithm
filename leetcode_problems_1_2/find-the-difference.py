class Solution:
    # t에 추가된 s에는 없는 글자를 찾아라
    # XOR를 활용(같은 값에 대해서 XOR 비트연산자를 사용하면 0이 된다)
    # 시간복잡도 len(s) + len(t) -> O(n)
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0

        # iterator s and use xor operation it's element
        for char in s:
            result ^= ord(char)

        # iterator t and use xor operation xor it's element
        for char in t:
            result ^= ord(char)

        return chr(result)

    # Sort를 활용 len(s)log(len(s)) + len(t)loglen(t) -> O(nlogn)
    def findTheDifference(self, s: str, t: str) -> str:
        # exit condition
        if not s:
            return t

        # sort
        s = sorted(s)
        t = sorted(t)
        
        # iterator s and t(range len(s))
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        
        # if not find difference, return t's last index value
        return t[-1]

s = "abcd"
t = "abcde"
solution = Solution()
print(solution.findTheDifference(s, t))