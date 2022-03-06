from typing import List

# top-left corner에서 bottom-right corner로 가는 값의 합 중 가장 작은 경로를 구하라
# 현재 위치에서 아래 또는 오른쪽으로만 이동 가능

"""
접근방법

최솟값으로 top-left corner에서 bottom-right corner로 이동해야 하기에 현재 위치에서 최소 path를 기록해야
한다고 생각함 -> DP 테이블을 사용해 현재 위치를 기록(DP로 풀이)

현재 위치로 이동할 수 있는 방법은 위에서 아래로 또는 왼쪽에서 오른쪽으로 이동하는 방법뿐이다.
이 중 최솟값을 구하는 방법은 현재 위치의 값에다가 위의 두 가지 방법 중 최솟값을 더해주면 되는 것이다.
따라서 점화식은 dp[i][j] = dp[i][j] + min(dp[i - 1][j], dp[i][j - 1])에 해당한다.

다만 첫 번째 행이나 첫 번째 열은 단지 왼쪽에서 오른쪽으로 또는 위에서 아래로 내려오는 방법 뿐이므로
미리 초기화를 시키고 점화식을 사용해 DP로 문제를 풀이한다.

"""
class Solution:
    # DP를 이용하여 문제 풀이(보텀업 방식)
    # 공간복잡도를 줄이기 위해 현재의 grid를 그대로 사용
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])

        # 첫 번째 행은 왼쪽에서 오른쪽으로 이동하는 방법만 존재
        for i in range(1, column):
            grid[0][i] += grid[0][i - 1]

        # 첫 번째 열은 위에서 아래로 이동하는 방법만 존재
        for i in range(1, row):
            grid[i][0] += grid[i - 1][0]

        # 남은 원소들은 위에서 아래로 이동하는 경로와 왼쪽에서 오른쪽으로 이동하는 경로 중 작은 값(min)값을
        # 현재 위치에 더해주면 된다.
        # 즉, 점화식은 dp[i][j] = dp[i][j](현재 위치의 값) + min(dp[i - 1][j], dp[i][j - 1])
        for i in range(1, row):
            for j in range(1, column):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[row - 1][column - 1]

    # DP를 이용하여 문제 풀이(보텀업 방식)
    # 최적화 1 : 위의 답에서 값을 업데이트할 때 필요한 것은 grid[i-1][j]와 grid[i][j - 1] 이므로
    # 전체의 m * n matrix를 유지할 필요가 없다.
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])

        pre = [grid[0][0]] * row
        cur = [0] * row

        # 첫 번째 행 초기화
        for i in range(1, row):
            pre[i] = pre[i - 1] + grid[i][0]
        
        for j in range(1, column):
            cur[0] = pre[0] + grid[0][j]
            for i in range(1, row):
                # cur에 두 번째 행을 기록
                cur[i] = min(cur[i - 1], pre[i]) + grid[i][j]

            # pre가 현재의 행을 가지도록 swap
            pre, cur = cur, pre

        return pre[row - 1]

    # DP를 이용하여 문제 풀이(보텀업 방식)
    # 최적화 2 : 위의 답에서 pre를 유지하는 것은 pre[i]의 복구를 위한 것인데, 이는 업데이트 하기 전 cur[i]이다.
    # 따라서 하나의 list로도 풀이 가능하다.
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        cur = [grid[0][0]] * row

        # 첫 번쨰 열 초기화
        for i in range(1, row):
            cur[i] = cur[i - 1] + grid[i][0]

        for j in range(1, column):
            cur[0] += grid[0][j]
            for i in range(1, row):
                cur[i] = min(cur[i - 1], cur[i]) + grid[i][j]

        return cur[row - 1]

grid = [[1,2,3],[4,5,6]]
solution = Solution()
print(solution.minPathSum(grid))