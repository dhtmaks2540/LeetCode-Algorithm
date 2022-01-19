from typing import List


class Solution:
    # DFS로 접근
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n, m = len(land), len(land[0])

        # 결과용 변수
        result = []
        
        def dfs(i, j):
            if 0 <= i < n and 0 <= j < m and land[i][j]:
                land[i][j] = 0
                # 동서남북 탐색(i와 j의 max값 가져오기)
                i, j = max((i, j), dfs(i, j + 1), dfs(i, j - 1), dfs(i + 1, j), dfs(i - 1, j))
                return i, j
            return 0, 0

        for i in range(n):
            for j in range(m):
                if land[i][j] == 1:
                    x, y = dfs(i, j)
                    result.append([i, j, x, y])

        return result

    """
    https://leetcode.com/problems/find-all-groups-of-farmland/discuss/1640116/Python3-DFS-(easy-to-understand)
    """

    # 개선된 코드
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        group = []
        m, n = len(land), len(land[0])
        
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or land[row][col] == 0:
                return (0, 0)
            
            land[row][col] = 0
            # 남쪽
            h_r1, h_c1 = dfs(row + 1, col)
            # 동쪽
            h_r2, h_c2 = dfs(row, col + 1)
            
            # 최댓값 갱신
            h_r = max(h_r1, h_r2, row)
            h_c = max(h_c1, h_c2, col)
            
            return (h_r, h_c)
        
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    x, y = dfs(i, j)
                    group.append([i, j, x, y])
                    
        return group

land = [[1,0,0],[0,1,1],[0,1,1]]
solution = Solution()
print(solution.findFarmland(land))