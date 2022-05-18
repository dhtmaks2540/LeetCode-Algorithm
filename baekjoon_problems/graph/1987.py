"""
좌측 상단에서 시작하여 말이 지날 수 있는 최대의 칸 수를 출력하라

처음 BFS 탐색을 수행하려고 하다가 그렇게 하면 문제가 복잡해져서 DFS를 사용하여 풀이했다.
다만 문제가 좀 까다로워서 시간 초과를 주의해야하는 문제인듯하다.. 우선 DFS와 BFS는 방문처리를 확인하지
않으면 무한 루프에 빠지기 때문에 이미 방문했는지 확인하기 위한 리스트가 필요하다. 이 문제에서는
그래프에 A ~ Z까지 쓰이므로 알파벳 변수를 저장하기 위한 26개의 원소로 이루어진 리스트를 선언한다.
그 후 현재 위치에서 상하좌우로 이동하며 이동한 위치가 정상범위이며 방문하지 않았다면 방문을 처리하고
DFS를 호출하는 방식으로 풀이한다. 그리고 방문이 모두 끝난다면 방문을 해제하여 다른 길로도 방문할 수 있도록
체크한다. 다만 이 문제는 종료 조건이 없기에 최댓값을 파악하기 위해서 cnt라는 변수를 dfs 함수가 호출될
때마다 +1씩 추가하며 이 값을 사용해서 최댓값을 기록하도록 했다.

https://mygumi.tistory.com/186
"""

import sys

R, C = map(int, sys.stdin.readline().strip().split(" "))
graph = []
for _ in range(R):
    graph.append(list(sys.stdin.readline().strip()))

# 동서남북
move_dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# 최대 칸을 기록하기 위한 변수
answer = -sys.maxsize
# 방문처리를 위한 리스트
visited = [False] * 26
# 시작점 방문 처리
visited[ord(graph[0][0]) - ord('A')] = True

def dfs(row, col, visited, cnt):
    global answer
    
    answer = max(answer, cnt)
    
    for i in range(4):
        next_row, next_col = move_dxy[i][0] + row, move_dxy[i][1] + col
        # 정상범위이며 방문하지 않았다면
        if 0 <= next_row < R and 0 <= next_col < C and not visited[ord(graph[next_row][next_col]) - ord('A')]:
            # 방문 처리 및 재귀 수행
            visited[ord(graph[next_row][next_col]) - ord('A')] = True
            dfs(next_row, next_col, visited, cnt + 1)
            # 다른 분기를 확인하기 위해서 방문 처리 해제
            visited[ord(graph[next_row][next_col]) - ord('A')] = False
               
dfs(0, 0, visited[:], 1)
print(answer)