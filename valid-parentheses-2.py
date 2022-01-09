class Solution:
    def isValid(self, s: str) -> bool:
        # 괄호 dict
        dict = {"(" : ")",
         "[" : "]",
          "{":"}"
        }

        stack = []

        for char in s:
            # 열린 괄호라면(딕셔너리의 키에 있다면)
            if char in dict:
                # 값 넣기
                stack.append(dict[char])
            # 닫힌 괄호라면
            else:
                # 스택에 값이 있고 가장 마지막 값과 같으면
                if stack and stack[-1] == char:
                    # 빼기
                    stack.pop()
                else:
                    return False
        # 모두 처리를 하였는데 값이 남아있다면
        if stack:
            return False
        return True

    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        # 스택 이용 예외 처리 및 일치 여부 판별
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False

        return len(stack) == 0

s = "(]"
solution = Solution()
print(solution.isValid(s))