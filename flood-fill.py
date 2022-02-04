from typing import List


class Solution:
    """
    왜 DFS로 접근?
    재귀적으로 해당 좌표가 범위 안에 들어가며, 해당 좌표의 값을 비교하기 위해서 DFS를 선택
    """

    # image[sr][sc] 위치의 값과 같은 인접한 원소들을 newColor로 칠해라
    # DFS로 접근
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        len_x = len(image)
        len_y = len(image[0])
        color = image[sr][sc]

        def dfs(x, y):
            # 유요한 범위이며 해당 좌표가 원하는 값일 때
            if 0 <= x < len_x and 0 <= y < len_y and image[x][y] == color:
                # 현재 값이 목표 값과 다를 경우에 변경
                if image[x][y] != newColor:
                    image[x][y] = newColor

                    # 동서남북 방향 이동
                    dfs(x - 1, y)
                    dfs(x + 1, y)
                    dfs(x, y - 1)
                    dfs(x, y + 1)

        dfs(sr,sc)

        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # 방문했는지를 확인하기 위한 리스트
        array = [[False] * len(image[0]) for _ in range(len(image))]
        len_x = len(image)
        len_y = len(image[0])
        color = image[sr][sc]
        
        def dfs(x, y):
            if 0 <= x < len_x and 0 <= y < len_y:
                if image[x][y] == color and not array[x][y]:
                    image[x][y] = newColor
                    array[x][y] = True

                    # 동서남북 방향 이동
                    dfs(x - 1, y)
                    dfs(x + 1, y)
                    dfs(x, y - 1)
                    dfs(x, y + 1)

        dfs(sr, sc)
        return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2

image = [[0,0,0],[0,1,1]]
sr = 1
sc = 1
newColor = 1

solution = Solution()
print(solution.floodFill(image, sr, sc, newColor))