"""
우리 병사의 위력의 합과 적국 병사의 위력의 합을 출력

DFS를 활용하여 풀 수 있는 대표적인 문제이다.

해당 문제는 그래프에서 탐색을 요하는 문제로 깊이 우선 탐색을 사용해서 해당 위치에서
동서남북 방향으로 같은 색을 가진 값을 찾아나서며 방문처리를 통해 풀 수 있는 문제이다.
"""

# 전쟁터의 가로 크기, 세로크기(2차원 행열)
N, M = map(int, input().split())
# 2차원 그래프
graph = []

for _ in range(M):
    graph.append(list(input()))

def dfs(x, y, count, color):
    # 범위안에 있으며 해당 원소가 같은 색이라면
    if 0 <= x < M and 0 <= y < N and graph[x][y] == color:
        # 방문처리
        graph[x][y] = 'A'
        # 카운트 증가
        count += 1

        # 동서남북으로 DFS 호출
        count += dfs(x - 1, y, 0, color)
        count += dfs(x + 1, y, 0, color)
        count += dfs(x, y - 1, 0, color)
        count += dfs(x, y + 1, 0, color)

        return count
    else:
        return 0

white_number = 0
blue_number = 0

for i in range(M):
    for j in range(N):
        if graph[i][j] == 'W':
            number = dfs(i, j, 0, 'W')
            white_number += number**2
        elif graph[i][j] == 'B':
            number = dfs(i, j, 0, 'B')
            blue_number += number**2

print(white_number, blue_number)