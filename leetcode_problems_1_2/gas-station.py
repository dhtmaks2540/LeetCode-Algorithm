from typing import List

"""
접근 방법

우선, 출발점에서 출발할 수 있는지를 판단하여 최적화를 진행
그 후 모든 경로는 다 확인해봐야 한다고 생각

"""

# 한 바퀴를 돌 수 있는 gas station의 인덱스를 반환, 불가능하면 -1
class Solution:
    # 브루드 포스 접근 -> Time Limited Exceed
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        # 출발점에 해당
        for i in range(n):
            fuel = 0
            # 출발점부터 출발점 + 길이까지
            for j in range(i, i + n):
                # 나머지 처리
                j %= n
                fuel += gas[j]
                fuel -= cost[j]

                if fuel < 0:
                    break

            if fuel >= 0:
                return i

        return -1

    """
    그리디 알고리즘

    한 번 이상은 반드시 성립되지 않는 지점이 존재한다. 그렇지 않다면 정답이 복수개가 되기 때문이다.
    성립되지 않는 지점이 있다면 그 앞은 전부 출발점이 될 수 없다.
    성립되지 않는 지점을 제외하면서 출발점을 찾는데, 이는 수학에서 귀류법으로 증명하는 것과 유사하다.
    모순을 이끌어낸 거짓인 경우를 제외하면, 가능한 지점은 제외하지 못한 지점, 자연스럽게 남은 곳이 정답이 된다.
    """
    
    # 한 번만 방문
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 전체 기름의 양이 전체 비용보다 클 경우 반드시 전체를 방문하는 출발점이 존재
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            # 출발점이 안되는 지점 판별
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]

        return start

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
gas = [2,3,4]
cost = [3,4,3]
solution = Solution()
print(solution.canCompleteCircuit(gas, cost))