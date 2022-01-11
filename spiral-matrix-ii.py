from typing import List


class Solution:
    # DFS로 접근
    def generateMatrix(self, n: int) -> List[List[int]]:
        array = [[0] * n for _ in range(n)]
        isVisited = [[False] * n for _ in range(n)]

        # 동, 남, 서, 북
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        def dfs(x, y, count, direction):
            # 범위가 넘거나 이미 방문했다면 리턴
            if x < 0 or x >= n or y < 0 or y >= n or isVisited[x][y]:
                return

            # count 처리
            array[x][y] = count
            # 방문 처리
            isVisited[x][y] = True

            nx = x + dx[direction]
            ny = y + dy[direction]

            # 범위를 넘어섰거나 이미 방문한 곳이라면
            if nx < 0 or nx >= n or ny < 0 or ny >= n or isVisited[nx][ny]:
                # 방향 바꾸기
                direction = (direction + 1) % 4
                nx = x + dx[direction]
                ny = y + dy[direction]

            dfs(nx, ny, count + 1, direction)

        dfs(0, 0, 1, 0)

        return array

    """
    https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions
    """

    def generateMatrix(self, n):
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            A[i][j] = k + 1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A

    """
    https://leetcode.com/problems/spiral-matrix-ii/discuss/963128/Python-rotate-when-need-explained
    """

    # 시간 복잡도는 O(n^2), 공간 복잡도도 O(n^2)
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        # x좌표, y좌표, 방향좌표
        x, y, dx, dy = 0, 0, 1, 0
        for i in range(n*n):
            # 1 ~ n^2까지
            matrix[y][x] = i + 1
            # 범위 안에 없거나 또는 방문한적이 있다면(숫자가 0 - 초기값이 아니라면)
            if not 0 <= x + dx < n or not 0 <= y + dy < n or matrix[y+dy][x+dx] != 0:
                # 방향 바꾸기
                dx, dy = -dy, dx
            x, y = x + dx, y + dy
        return matrix

n = 4
solution = Solution()
print(solution.generateMatrix(n))