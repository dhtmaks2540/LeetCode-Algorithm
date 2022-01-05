class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        str_x = str(x)
        n = len(str_x)

        # 왼쪽과 오른쪽의 값을 비교하는 형식
        for i in range(n // 2):
            if str_x[i] != str_x[n - 1 - i]:
                return False

        return True

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        # 슬라이싱을 사용해 접근
        return str(x)[:] == str(x)[::-1]

    def isPalindrome(self, x: int) -> bool:
        # 음수면 False 반환
        # 또는 양수인데 마지막 값이 0이라면 팰린드롬이 아니므로 False 반환
        if x < 0 or (x > 0 and x % 10 == 0):
            return False 

        result = 0
        
        """
        Example, if x = 15951, then let's create reverse of x in loop. Initially, x = 15951, revX = 0

        x = 1595, revX = 1
        x = 159, revX = 15
        x = 15, revX = 159
        """

        # 중간지점까지 나누기
        while x > result:
            result = result * 10 + x % 10
            x = x // 10

        return True if (x == result or x == result // 10) else False

x = 121
solution = Solution()
print(solution.isPalindrome(x))