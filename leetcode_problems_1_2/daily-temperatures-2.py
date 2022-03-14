from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 스택 변수
        stack = []
        # 결과 변수
        result = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):
            # 스택에 저장된 값이 현재 온도보다 낮으면
            while stack and stack[-1][0] < temperature:
                # 뽑아낸 후 차이 계산
                temp, i = stack.pop()
                result[i] = index - i
            
            stack.append((temperature, index))

        return result

    # 정답 코드(인덱스만을 저장하여 더 깔끔한 코드)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):
            # 현재 온도보다 스택 값이 높다면 정답 처리
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last

            stack.append(i)

        return answer
            
temperatures = [30,60,90]
solution = Solution()
print(solution.dailyTemperatures(temperatures))