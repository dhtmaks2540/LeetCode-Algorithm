from typing import List


class Solution:
    # DFS로 접근
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 동서남북을 나타내는 값
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        def dfs(i, j, count = 0):
            # 범위를 벗어나거나 해당 아이템이 1이 아닌 경우는 return
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != 1:
                    return 0

            # 방문처리
            grid[i][j] = 0
            count += 1

            # 동서남북 탐색
            for index in range(4):
                count += dfs(i + dx[index], j + dy[index])

            return count

        # 결과 변수
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = max(count, dfs(i, j))

        return count

    # 깔끔한 코드
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i, j + 1) + dfs(i, j - 1) + dfs(i + 1, j) + dfs(i - 1, j)

            return 0
        
        areas = [dfs(i,j) for i in range(m) for j in range(n) if grid[i][j]]

        return max(areas) if areas else 0
        

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
solution = Solution()
print(solution.maxAreaOfIsland(grid))