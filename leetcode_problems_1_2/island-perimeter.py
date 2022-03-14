from typing import List


class Solution:
    # 물과 맞닿은 땅의 면적을 구하라 -> 상하좌우로 물이라면 + 1, 아니라면 패스
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 결과 변수
        self.result = 0
        # 동서남북
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        len_x = len(grid)
        len_y = len(grid[0])

        def dfs(x, y):
            # 동서남북 확인하기
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 주변이 경계이거나 물이라면
                if nx < 0 or nx >= len_x or ny < 0 or ny >= len_y or \
                    grid[nx][ny] == 0:

                    self.result += 1

        for i in range(len_x):
            for j in range(len_y):
                # 육지라면
                if grid[i][j] == 1:
                    dfs(i, j)

        return self.result

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
solution = Solution()
print(solution.islandPerimeter(grid))