class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 2진수를 int형으로 변경
        sum = int(a, 2) + int(b, 2)
        
        # 2진수 -> str로 변경 후 접두사는 빼기
        return str(bin(sum))[2:]

    # 전가산기를 이용한 풀이
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        # 리스트로 변환
        a = list(a)
        b = list(b)

        while a or b or carry:
            # 뒤에서 pop
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            
            # carry에 2를 나눈 나머지 더하기
            result += str(carry % 2)
            # 2의 몫(자리 올림 수)
            carry //= 2

        # 역으로 되어있으므로 역순으로 출력
        return result[::-1]

a = "11"
b = "1"
solution = Solution()
print(solution.addBinary(a, b))