"""
단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력

DFS를 활용하여 문제 풀이

해당 문제는 그래프에서 탐색을 요구하는 문제로 완전 탐색보다는 DFS를 사용해서 해당 위치에서
탐색이 가능할 경우 DFS를 사용해 방문을 처리하며 탐색하면 풀 수 있다. 즉, 그래프 탐색에 대한 문제로
DFS를 사용하면 풀기가 좋다. 우선 집의 개수를 확인해야 하므로 그래프에서 집에 해당하는 1의 값일 때
DFS를 시도한다. DFS는 재귀구조 이므로 종료 조건으로 범위를 벗어나거나 해당 위치가 집이 아닌 경우로
주었고, 정상 조건일 경우 개수를 체크하기 위해 count를 증가, 방문처리, 그리고 동서남북으로 탐색하기
위해 또다시 DFS 함수를 호출한다.
"""

# 지도의 크기
N = int(input())
# 지도(0 또는 1로 이루어져 있다)
graph = []
# 지도 입력
for _ in range(N):
    graph.append(list(map(int, input())))

result = []

def dfs(x, y, count):
    # 범위안에 들어가고 해당 위치를 방문할 수 있다면
    if 0 <= x < N and 0 <= y < N and graph[x][y] == 1:
        count += 1
        # 방문처리
        graph[x][y] = 2

        # 동서남북 방문
        count += dfs(x - 1, y, 0)
        count += dfs(x + 1, y, 0)
        count += dfs(x, y - 1, 0)
        count += dfs(x, y + 1, 0)

        # 결과 반환
        return count
    # 범위안에 안들어가거나 방문하지 못한다면
    else:
        return 0

# 그래프를 순회하며
for i in range(N):
    for j in range(N):
        # 현재 위치가 집이라면
        if graph[i][j] == 1:
            # DFS 탐색
            houses = dfs(i, j, 0)
            result.append(houses)

# 정렬 수행
result.sort()

# 집의 수
print(len(result))
for house in result:
    print(house)