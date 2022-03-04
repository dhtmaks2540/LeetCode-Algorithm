from typing import List


class Solution:
    # 브루드 포스로 접근 -> 타임아웃
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            if gas[i] - cost[i] >= 0:
                car = 0
                for j in range(i, i + len(gas)):
                    j %= len(gas)

                    car += gas[j]
                    car -= cost[j]

                    if car < 0:
                        break
                
                if car >= 0:
                    return i
        return -1

    # 책에 있는 브루드 포스
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for start in range(len(gas)):
            fuel = 0
            for i in range(start, start + len(gas)):
                index = i % len(gas)

                can_travel = True
                if gas[index] + fuel < cost[index]:
                    can_travel = False
                    break
                else: fuel += gas[index] - cost[index]

            if can_travel:
                return start

        return -1

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 모든 주유소 방문 가능 여부 판별
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            # 출발점이 안되는 지점 판별
            if gas[i] + fuel < cost[i]:
                # 안되면 한 칸 뒤로 밀어내기
                # 성립되지 않는 지점이 있다면 그 앞은 전부 출발점이 될 수 없음
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]

        return start

gas = [5,1,2,3,4]
cost = [4,4,1,5,1]

solution = Solution()
print(solution.canCompleteCircuit(gas, cost))