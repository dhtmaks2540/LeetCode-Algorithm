class Solution:
    # 전가산기를 이용하여 풀이
    def addStrings(self, num1: str, num2: str) -> str:
        # 자리올림 수
        carry = 0
        # 결과 변수
        result = ""

        # 리스트형식으로 변환
        list1 = list(num1)
        list2 = list(num2)

        while list1 or list2 or carry:
            # 자릿수 총합
            sum = 0

            if list1:
                sum += int(list1.pop())
            if list2:
                sum += int(list2.pop())

            # 몫, 나머지로 변환
            carry, val = divmod(sum + carry, 10)

            result += str(val)

        return result[::-1]

    # ord(유니코드 반환) 함수와 전가산기를 이용한 구현
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = list(num1), list(num2)
        carry, res = 0, []

        while num1 or num2 or carry:
            sum = 0
            if num1:
                # 0의 유니코드 값을 빼서 숫자 계산
                sum += ord(num1.pop()) - ord('0')
            if num2:
                sum += ord(num2.pop()) - ord('0')

            # 몫, 나머지로 변환
            carry, val = divmod(sum + carry, 10)
            
            res.append(val)

        return "".join(str(d) for d in res)[::-1]


num1 = "11"
num2 = "123"

solution = Solution()
print(solution.addStrings(num1, num2))