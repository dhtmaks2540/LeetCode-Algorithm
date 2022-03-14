from typing import List


class Solution:
    # 재귀를 사용하는 DFS로 접근
    def numIslands(self, grid: List[List[str]]) -> int:
        len_x = len(grid)
        len_y = len(grid[0])
        
        # 동,서,남,북을 나타내기 위한 값
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        # dfs 함수
        def dfs(x, y):
            grid[x][y] = "2"

            # 4방향 탐색
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # nx, ny의 값이 범위안에 있고
                if 0 <= nx < len_x and 0 <= ny < len_y:
                    # 그 값이 1이라면
                    if grid[nx][ny] == "1":
                        # 재귀 호출
                        dfs(nx, ny)
                    else:
                        continue

        count = 0

        for i in range(len_x):
            for j in range(len_y):
                # 현재의 값이 1이면 dfs함수 호출
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count

    # 책 정답 - DFS로 접근
    def numIslands(self, grid: List[List[str]]) -> int:
        # 예외처리
        if not grid:
            return 0
        
        def dfs(i, j):
            # 더 이상 땅이 아닌 경우 종료
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                    return

            grid[i][j] = 0

            # 동서남북 탐색
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1

        return count
    

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

solution = Solution()
print(solution.numIslands(grid))