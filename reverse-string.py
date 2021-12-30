from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 문자열 절반의 길이
        half_len = len(s) // 2
        
        for i in range(half_len):
            # 앞과 뒤에서부터 이터레이션하며 문자열 교체
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
            
        return s
    
s = ["h","e","l","l","o"]
solution = Solution()
print(solution.reverseString(s))