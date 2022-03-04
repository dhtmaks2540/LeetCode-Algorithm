class Solution:
    # 투포인터
    def validPalindrome(self, s: str) -> bool:
        # 왼쪽 포인터
        start_index = 0
        # 오른쪽 포인터
        end_index = len(s) - 1
        
        # 문자열 없으면 바로 리턴
        if not s:
            return True
        
        while start_index < end_index:
            # 왼쪽 인덱스의 값과 오른쪽 인덱스의 값이 같다면
            if s[start_index] == s[end_index]:
                start_index += 1
                end_index -= 1
            # 다르다면
            elif s[start_index] != s[end_index]:
                # 왼쪽 인덱스 1 증가한것이 팰린드롬인지 또는 오른쪽 인덱스 하나 감소한것이 팰린드롬인지
                if s[start_index+1:end_index+1] == s[start_index+1:end_index+1][::-1] or s[start_index:end_index] == s[start_index:end_index][::-1]:   
                    return True
                # 그 외의 경우
                else:
                    return False
        
        return True
    
s = "abca"