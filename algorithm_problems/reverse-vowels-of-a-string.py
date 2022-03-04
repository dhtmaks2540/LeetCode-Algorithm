class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_list = []
        
        result = []
          
        for char in s:
            # 모음이면 추가
            if char in 'aeiou' or char in 'aeiou'.upper():
                vowel_list.append(char)

        for char in s:
            # 모음이라면
            if char in 'aeiou' or char in 'aeiou'.upper():
                # 모음만 뒤집기 위해 뒤에서부터 pop해서 추가
                result.append(vowel_list.pop())
            else:
                result.append(char)
                
        return ''.join(result)