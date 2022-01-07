class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_value = 0
        num2_value = 0

        index = 1
        # num1의 숫자는 int형으로 변환
        for n in num1[::-1]:
            num1_value += index * (ord(n) - ord("0"))
            index *= 10

        # num2의 숫자는 int형으로 변환
        index = 1
        for n in num2[::-1]:
            num2_value += index * (ord(n) - ord("0"))
            index *= 10

        return str(num1_value * num2_value)

    def multiply(self, num1, num2):
        res = [0] * (len(num1)+len(num2))
        # 역순으로 접근
        for i in range(len(num1)-1, -1, -1):
            # 자리올림수
            carry = 0
            # 역순으로 접근
            for j in range(len(num2)-1, -1, -1):
                tmp = (ord(num1[i])-ord('0')) * (ord(num2[j])-ord('0')) + carry
                carry = (res[i+j+1]+tmp) // 10
                res[i+j+1] = (res[i+j+1]+tmp) % 10
            res[i] += carry
        res = ''.join(map(str, res))
        return '0' if not res.lstrip('0') else res.lstrip('0')




num1 = "123"
num2 = "456"
solution = Solution()
print(solution.multiply(num1, num2))