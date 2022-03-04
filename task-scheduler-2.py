from typing import List
import collections

"""
접근 방법

모든 tasks를 끝내는 최소한의 시간은 가장 많은 tasks를 먼저 끝내는 것이 목표라고 생각함
따라서 Counter를 통해 tasks의 개수를 파악한 후 most_common() 메소드를 통해 n + 1의 tasks를 뽑아냄
그리고 반복문을 돌면서 task를 처리하고 task가 0이 되면 제거

그리고 마지막에 if문을 통해서 n + 1 만큼 task를 처리하지 못했다면(같은 값이 못나오는 휴식시간(n)을 가져야 한다면)
조건을 통해 휴식시간을 갖도록 풀이
"""

# 모든 tasks를 끝내는 최소한의 시간, 다만 n 값동안 같은 업무를 수행할 수 없음
class Solution:
    # 그리디 포인트는 가장 많은 개수를 가진 작업을 최대한 빠르게 끝내는 것이 목표라고 생각
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        result = 0

        # freq에 값이 있는 동안에
        while freq:
            sub_count = 0
            temp = freq.most_common(n + 1)
            
            for value in temp:
                freq[value[0]] -= 1
                sub_count += 1
                result += 1
                # 현재 값이 0이라면 현재 요소 제거
                if freq[value[0]] == 0:
                    del freq[value[0]]
            
            # 더 이상 요소가 없을 경우
            if not freq:
                break

            result += n - sub_count + 1

        return result

    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0

            # 개수 순 추출
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1

                # 현재 요소 -1 처리
                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()

            # exit condition(counter의 요소가 없을 경우)
            if not counter:
                break

            result += n - sub_count + 1

        return result

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
solution = Solution()
print(solution.leastInterval(tasks, n))
print(collections.Counter(tasks))