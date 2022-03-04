from typing import List


class Solution:
    """
    https://leetcode.com/problems/count-sub-islands/discuss/1284319/JavaC%2B%2BPython-DFS-Solution
    """
    # DFS로 접근
    # 두 개의 2차원 행렬의 연관관계를 맺어서 개수를 파악해라
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n, m = len(grid1), len(grid1[0])

        def dfs(i, j):
            # 범위안에 들어가지 않거나 grid2의 값이 1이 아니라면 1 반환
            if not (0 <= i < n and 0 <= j < m and grid2[i][j] == 1): return 1
            grid2[i][j] = 0
            # grid1의 값 획득(grid1의 값이 0이면 sub-island가 아니므로 패스됨)
            res = grid1[i][j]
            # 동서남북 탐색
            for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                # &비트 연산
                res &= dfs(i + di, j + dj)

            return res

        # 합 계산
        return sum(dfs(i, j) for i in range(n) for j in range(m) if grid2[i][j])

    """
    https://leetcode.com/problems/count-sub-islands/discuss/1284306/98-faster-oror-Simple-approach-oror-well-explained
    """
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m=len(grid1)
        n=len(grid1[0])
        
        def dfs(i,j):
            # 범위를 벗어나거나 값이 0이라면 넘기기
            if i<0 or i>=m or j<0 or j>=n or grid2[i][j]==0:
                return
            
            grid2[i][j]=0
            # 동서남북 탐색
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i-1,j)
            
        # grid2는 1이고 grid1은 0인 섬
        # 즉, sub-island가 아닌 곳 지우기
        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1 and grid1[i][j]==0:
                    dfs(i,j)
        
        c=0
        # sub-island 계산
        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1:
                    dfs(i,j)
                    c+=1
        return c

        
            

grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
solution = Solution()
print(solution.countSubIslands(grid1, grid2))