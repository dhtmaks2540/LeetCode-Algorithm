from typing import List
import collections


class Solution:
    # 분할 정복을 활용
    def diffWaysToCompute(self, input: str) -> List[int]:
        # 계산하는 함수
        def compute(left, right, op):
            results = []
            # 왼쪽의 숫자 만큼
            for l in left:
                # 오른쪽의 숫자 만큼
                for r in right:
                    # eval 함수에 문자열 연산을 집어넣으면 알아서 계산
                    results.append(eval(str(l) + op + str(r)))
            return results
        
        # 값이 숫자라면 int로 바꾼 후 리스트로 반환
        if input.isdigit():
            return [int(input)]

        # 결과용 변수
        results = []
        # 이터레이터하며
        for index, value in enumerate(input):
            # 값이 연산이라면
            if value in '-+*':
                # 연산을 기준으로 왼쪽, 오른쪽 나누기
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index + 1:])

                # append가 아닌 extend를 사용하여 확장하는 형태로
                results.extend(compute(left, right, value))

        return results

expression = "2-1-1"
solution = Solution()
print(solution.diffWaysToCompute(expression))