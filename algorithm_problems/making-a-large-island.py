from typing import List
import collections

"""
https://leetcode.com/problems/making-a-large-island/discuss/1375992/C%2B%2BPython-DFS-paint-different-colors-Union-Find-Solutions-with-Picture-Clean-and-Concise

1. 그래프를 탐색하며 해당 위치가 1인 원소에서 DFS를 호출하여 육지의 크기 계산
-> 이 때 그 육지의 크기를 기록

2. 다시 그래프를 탐색하며 0인 위치에서 동서남북으로 연결된 땅을 확인하며
0인 위치를 땅으로 변경하고 난 크기 계산하고 그 값의 최댓값을 갱신하는 방식으로
"""

class Solution:
    # 하나의 0을 1로 바꾼 최대 땅 넓이를 구하라
    # DFS 사용(하나의 값을 변경 후 그 상황에서 최대 땅 넓이 구하기 위해)
    def largestIsland(self, grid: List[List[int]]) -> int:
        # 동서남북
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        # 리스트의 크기와 새로운 색을 넣기 위한 변수
        n, next_color = len(grid), 2
        component_size = collections.defaultdict(int)

        def paint(x, y, color):
            # 범위를 벗어나거나 1이 아니라면 return
            if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] != 1: return 
            grid[x][y] = color
            component_size[color] += 1
            # 동서남북으로 dfs 수행
            for i in range(4):
                paint(x + dx[i], y + dy[i], color)

        for x in range(n):
            for y in range(n):
                # 1이 아니라면 패스
                if grid[x][y] != 1: continue # Only paint when it's an island cell
                # DFS 호출
                paint(x, y, next_color)
                # 육지마다 다른 색을 칠하기 위해 증가
                next_color += 1

        ans = max(component_size.values() or [0])
        for x in range(n):
            for y in range(n):
                # 0이 아니라면 패스
                if grid[x][y] != 0: continue
                # 색을 획득하기 위한 변수
                nei_colors = set()
                # 동서남북(현재 위치에서 동서남북으로 연결된 땅 획득)
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    # 범위를 벗어나거나 0이라면 패스
                    if nx < 0 or nx >= n or ny < 0 or ny >= n or grid[nx][ny] == 0: continue
                    nei_colors.add(grid[nx][ny])
                
                size_formed = 1 # Start with 1, which is matrix[x][y] when turning from 0 into 1
                # 현재 위치에서 연결된 땅 확인하며
                for color in nei_colors:
                    size_formed += component_size[color]
                # 최댓값 갱신
                ans = max(ans, size_formed)

        return ans

"""
https://gmlwjd9405.github.io/2018/08/31/algorithm-union-find.html

Union-Find로 해결

* Union-Find는 연결된 구성 요소를 각가의 크기로 저장하는 데 매우 좋은 데이터 구조이다.
* 그래프를 탐색하며, 만약 현제의 셀이 1이라면 union-find로 셀과 인접한 셀을 연결한다.
* 다시 그래프를 탐색하며, 0의 위치를 1로 바꾼 새로운 크기를 계산한다.
  * 만약 matrix[r][c] == 0이라면
    * 인접한 셀의 부모의 index를 가져와 크기를 계산한다.(유일한 부모 index를 가져와 연결된 구성요소를 두 번 계산하지 않음)
    * 총 크기를 계산
    * 가장 큰 사이즈로 갱신
"""

class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.size = [0] * n
            
    def isExist(self, u):
        return self.parent[u] >= 0

    def add(self, u):
        if self.isExist(u): return # Only add if not existed yet!!
        self.parent[u] = u
        self.size[u] = 1

    def find(self, u):
        if self.parent[u] == u: return u
        self.parent[u] = self.find(self.parent[u]) # Path compression
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        if self.size[pu] <= self.size[pv]: # Merge the smaller component to the bigger component
            self.parent[pu] = pv # Merge u into v
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu # Merge v into u
            self.size[pu] += self.size[pv]
        return True

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # 동서남북
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        n, ans = len(grid), 0
        uf = UnionFind(n * n)

        def land_neighbors(x, y):
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                nei_id = nx * n + ny
                if nx < 0 or nx >= n or ny < 0 or ny >= n or not uf.isExist(nei_id): continue
                yield nei_id

        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0: continue
                cur_id = x * n + y
                uf.add(cur_id)
                for nei_id in land_neighbors(x, y):
                    uf.union(cur_id, nei_id)
                p = uf.find(cur_id)
                ans = max(ans, uf.size[p])

        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1: continue
                nei_parents = set()
                for nei_id in land_neighbors(x, y):
                    nei_parents.add(uf.find(nei_id))
                size_formed = 1 # Start with 1, which is matric[x][y] when turning from 0 into 1
                for p in nei_parents:
                    size_formed += uf.size[p]
                ans = max(ans, size_formed)

        return ans
                
grid = [[1,1],[1,1]]
solution = Solution()
print(solution.largestIsland(grid))