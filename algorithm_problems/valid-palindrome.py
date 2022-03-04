class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 문자열과 숫자만을 저장하기 위한 리스트
        list = []
        
        for char in s:
            if char.isdigit():
                list.append(char)
            elif char.isalpha():
                list.append(char.lower())

        print(list)
    
    
solution = Solution()
s = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s))