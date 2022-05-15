"""
정리된 상태를 만드는 최소의 이동 횟수를 출력하라

BFS 탐색을 사용해서 비어 있는 칸에 주변의 값들을 모두 넣어보는 방식으로 완전 탐색을 수행해서
정렬이 완료된 경우의 횟수를 출력하는 방식으로 풀이했다. 다만 그래프를 사용해서 풀이하려고 했는데
정답이 나오지 않았다... 방향을 생각하고 코드로 구현하는 것이 중요하다.. 코드 구현을 높이자..

https://jaimemin.tistory.com/1081

핵심 포인트는 그래프를 그래프 그대로 사용하는 것이 아니라 숫자형태로 변경한 후 이 숫자를 가지고
방문 처리 및 빈 공간에 숫자를 넣는 방식으로 풀이하는 것이다.

1. 3*3칸에 존재하는 숫자들을 좌상단부터 우하단까지 이어지는 숫자로 표현하기 위해서 그래프의
비어있는 칸은 0을 9로 바꾼후 숫자로 표현한다.
2. BFS 탐색을 사용하여 큐에 숫자를 넣은 후 목표값(123456789)가 나오가나 큐가 빌 때까지
빈 칸을 동서남북으로 swap 하며 숫자를 확인한다.
3. target이 나온 경우 몇 번 했는지 출력하고 아니면 -1을 출력한다

항상 그래프만 생각하는 것이 아니라 여러가지 방법을 생각해서 최적화하는 것이 중요하다..!!
"""

import sys
import collections

graph = []
for _ in range(3):
    graph.append(list(map(int, sys.stdin.readline().strip().split(" "))))

# 동서남북 방향
dir = ((0, 1), (0, -1), (1, 0), (-1, 0))

# 목표
target = 123456789

# 시작값(숫자형식으로 변경)
start = 0
for i in range(3):
    for j in range(3):
        if graph[i][j] == 0:
            graph[i][j] = 9
        start = start * 10 + graph[i][j]

# BFS 탐색을 위한 큐 선언
queue = collections.deque()
queue.append(start)
# 방문을 확인하기 위한 딕셔너리
visited = dict()
# 시작값 방문처리
visited[start] = 0

while queue:
    cur = queue.popleft()
    lis_cur = str(cur)
    
    if cur == target:
        break
    
    # 비어있는 칸(9의 위치)
    zero_index = lis_cur.index('9')
    # 9의 좌표 저장(2차원 리스트에서의 좌표)
    y_index = zero_index // 3
    x_index = zero_index % 3
    
    # 동서남북 방향으로 확인하며
    for i in range(4):
        next_y = y_index + dir[i][1]
        next_x = x_index + dir[i][0]
        
        # 정상 좌표(정상 범위)
        if 0 <= next_y < 3 and 0 <= next_x < 3:
            temp = list(lis_cur)
            # 비어있는 칸과 주변 숫자 변경
            temp[y_index * 3 + x_index], temp[next_y * 3 + next_x] = temp[next_y * 3 + next_x], temp[y_index * 3 + x_index]
            
            next_cur = int("".join(temp))
            # 아직 방문하지 않았다면 방문 처리 및 큐에 삽입
            if next_cur not in visited:
                visited[next_cur] = visited[cur] + 1
                queue.append(next_cur)

# 결과값을 방문하지 못했다면 -1 출력               
if target not in visited:
    print(-1)
else:
    print(visited[target])
            