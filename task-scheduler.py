from typing import List


import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 결과용 변수
        result = 0
        # Counter
        counter = collections.Counter(tasks)

        while True:
            sub_count = 0

            # 개수 순 추출
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1
                # 1개씩 개수 줄이기
                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()

            # counter에 원소가 없다면 -> 즉 업무가 다 끝났다면
            if not counter:
                break
            
            # idle 처리
            result += n - sub_count + 1

        return result

tasks = ["A","A","A","B","B","B"]
n = 2

solution = Solution()
print(solution.leastInterval(tasks, n))