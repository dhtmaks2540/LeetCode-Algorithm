from typing import List
import collections

class Solution:
    """
    DP로 문제를 풀이, 이전 위치까지의 경로를 저장하고 이전 위치까지의 값을 가지고 현재의 위치를 갱신하기 때문에
    즉, 값을 기록해두고 이후에 사용하기 위해서 DP로 접근하였다.

    DP로 접근 후, 현재 위치의 경로합을 어떻게 더해줄지 분기하여 문제를 풀이
    """
    # DP로 풀이
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 예외처리
        if obstacleGrid[0][0] == 1:
            return 0
        
        row, column = len(obstacleGrid), len(obstacleGrid[0])
        # init dp table
        dp = [[0] * column for _ in range(row)]
        # init start position
        dp[0][0] = 1

        # init first row
        for i in range(1, column):
            # if position is not obstacle, dp[row][column] = dp[row][column - 1]
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i - 1]

        # iterate graph
        for x in range(row):
            for y in range(column):
                # 현재 위치가 장애물이 아니며 x > 0, y > 0이라면 현재 열 - 1의 위치 값 + 현재 행 - 1의 위치값
                if x > 0 and y > 0 and obstacleGrid[x][y] != 1:
                    dp[x][y] = dp[x][y - 1] + dp[x - 1][y]
                # 현재 위치가 장애물이 아니며 x > 0라면 현재 행 - 1의 위치값
                elif x > 0 and obstacleGrid[x][y] != 1:
                    dp[x][y] = dp[x - 1][y]

        # return finish
        return dp[row - 1][column - 1]

    """
    https://leetcode.com/problems/unique-paths-ii/discuss/23250/Short-JAVA-solution
    
    원본을 변경하지 않는 방법
    """
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        column = len(obstacleGrid[0])
        # init dp table
        dp = [0] * column
        dp[0] = 1

        for row in obstacleGrid:
            for j in range(column):
                if row[j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] = dp[j] + dp[j - 1]

            print(dp)

        return dp[column - 1]
    

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
solution = Solution()
print(solution.uniquePathsWithObstacles(obstacleGrid))