from typing import List


class Solution:
    # 문자열의 인덱싱을 사용하여 -, +를 구분
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0

        for oper in operations:
            # - operation
            if oper[1] == '-' or oper[-1] == '-':
                x -= 1
            # + operation
            elif oper[0] == '+' or oper[-1] == '+':
                x += 1

        return x

operations = ["++X","++X","X++"]
solution = Solution()
print(solution.finalValueAfterOperations(operations))