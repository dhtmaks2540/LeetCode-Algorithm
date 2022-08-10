"""
대표적인 그래프에서 탐색을 요구하는 문제이다. 2차원 리스트가 주어지면서 현재 위치에서 해당 위치로 가는
최소한의 칸의 이동은 그래프 탐색을 통해서 현재 위치에서 이동할 수 있는 방향으로 탐색을 수행하면서
목적지가 도달하면 이동한 칸의 수를 출력하면 된다. 이때, 최소한의 칸으로 이동하는 방법 같은 것이 명확히
나와있지 않기에 그래프의 탐색을 통해서 이를 파악하는 것이다. DFS와 BFS 모두 가능한 코드로 아래는
BFS를 통해서 탐색을 수행하였다.

DFS 또는 BFS를 통해서 그래프에서 탐색을 할 수 있는지 묻는 문제로 DFS와 BFS 탐색을 수행하며 방문확인을
처리하여 무한루프에 빠지지 않도록 주의해야한다.

"""

import sys
import collections

# 테스트케이스
T = int(sys.stdin.readline().strip())

# 나이트가 이동할 수 있는 위치
dxy = [(-1, -2), (-2, -1), (1, -2), (2, -1), (-1, 2), (-2, 1), (1, 2), (2, 1)]

for _ in range(T):
    # 체스판의 한 변의 길이
    l = int(sys.stdin.readline().strip())
    # 현재 나이트의 위치
    now_row, now_col = map(int, sys.stdin.readline().strip().split(" "))
    # 이동하려고 하는 칸
    to_row, to_col = map(int, sys.stdin.readline().strip().split(" "))
    # 방문을 확인하기 위한 2차원 리스트
    visited = [[False] * l for _ in range(l)]
    
    queue = collections.deque()
    queue.append((now_row, now_col))
    visited[now_row][now_col] = True
    # 이동한 횟수를 체크하는 변수
    answer = -1
    check = False
    
    while queue:
        answer += 1
        # 현재 큐에 있는 목적지들을 이터레이션
        for _ in range(len(queue)):
            now_row, now_col = queue.popleft()

            # 목표로 한 위치에 도착했다면
            if now_row == to_row and now_col == to_col:
                check = True
                break
            
            for index in range(len(dxy)):
                next_row, next_col = now_row + dxy[index][0], now_col + dxy[index][1]
                # 현재 위치가 정상 범위이며 방문하지 않았다면
                if 0 <= next_row < l and 0 <= next_col < l and not visited[next_row][next_col]:
                    # 방문처리 및 큐에 삽입
                    visited[next_row][next_col] = True
                    queue.append((next_row, next_col))
                
        if check:
            print(answer)
            break