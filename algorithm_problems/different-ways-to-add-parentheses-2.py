from typing import List

"""
접근방법

동빈나 알고리즘 책에서 해당 문제와 비슷한 문제를 DFS로 풀이한적이 있어 DFS로 접근하려함
해결방법이 안 떠오르면 메모하며 풀어보던가 입력값, 출력값의 연관 관계등을 찾아보려고 애써야함!

이 문제는 분할 정복에 해당되는 충분히 큰 문제이며, 이 문제를 쪼갠(sub-problem) 또한 같은 문제를
풀이한다. 따라서 분할 정복으로 접근해볼 수 있는데 우선 분할을 생각해보자.
분할정복은 대개 재귀로 문제를 풀이하기에 분할할 때 조건이 매우 중요(어디까지 작게 만들 것인지)
따라서 분할의 조건으로 해당 값이 숫자인지 판별하고 숫자라면 int형을 취해서 반환한다.
분할의 경우 현재 입력값을 iterate하며 현재 값이 연산자라면 해당 위치를 기준으로 왼쪽, 오른쪽으로 분할한다.
이와 같이 분할하다보면 모든 연산자에 있어서 왼쪽과 오른쪽을 분할하여 풀이할 수 있다.

그리고 분할된 값이 나오면 이 값을 계산하여 정복을 하면 되는 것이다.
"""

class Solution:
    # 분할 정복으로 문제 풀이
    def diffWaysToCompute(self, input: str) -> List[int]:
        # 계산하는 함수
        def compute(left, right, op):
            results = []
            
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))

            return results

        # 분할의 최후 조건(현재 값이 숫자라면)
        if input.isdigit():
            return [int(input)]

        results = []
        # input iterate(이 코드가 정말 중요하다)
        for index, value in enumerate(input):
            # 현재 값이 연산자라면
            if value in "-+*":
                # 분할에 해당(연산을 제외한 나머지 부분)
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index+1:])

                # 정복에 해당(left와 right를 연산자를 가지고 계산)
                results.extend(compute(left, right, value))

        return results

    def diffWaysToCompute(self, input: str, memo = {}) -> List[int]:
        if input.isdigit():
            return [int(input)]
        if input in memo:
            return memo[input]

        res = []
        for i in range(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))

        memo[input] = res
        return res

    def helper(self, m, n, op):
        if op == '+':
            return m + n
        elif op == "-":
            return m - n
        else:
            return m * n
        
        
expression = "2-1-1"
# expression = "2*3-4*5"
solution = Solution()
print(solution.diffWaysToCompute(expression))