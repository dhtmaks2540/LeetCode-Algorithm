"""
4가지의 명령어를 사용해서 최소한의 명령횟수로 A를 B로 변경하는 방법을 출력하라

4가지의 연산을 사용해서 a의 값을 b의 값으로 변경하는 최소한의 횟수를 출력하는 문제이다. 즉, 현재
숫자에서 4가지 연산을 모두 사용하며 직접 값을 비교하는 완전 탐색이 필요한데, 이 문제에서는
BFS를 사용하여 탐색을 수행하면 완전 탐색이 가능하다. 다만 이 문제는 숫자를 문자열로 변경하는 등의
연산을 사용하지 말고 숫자 그대로 연산을 수행시키는 최적화를 수행해야 풀이할 수 있다.

https://jaimemin.tistory.com/654
"""

import sys
import collections

# 테스트 케이스
T = int(sys.stdin.readline().strip())

def bfs(start, visited, target):
    queue = collections.deque()
    queue.append((start, []))
    visited[start] = True
    
    while queue:
        now, path = queue.popleft()
        
        if now == target:
            return path
        
        # D 연산
        d_result = (now * 2) % 10000
        # 방문하지 않았다면
        if not visited[d_result]:
            # 방문처리 및 큐에 삽입
            visited[d_result] = True
            queue.append((d_result, path + ['D']))
            
        # S 연산
        s_result = 9999 if now - 1 < 0 else now - 1
        # 방문하지 않았다면
        if not visited[s_result]:
            # 방문처리 및 큐에 삽입
            visited[s_result] = True
            queue.append((s_result, path + ['S']))
            
        # L 연산(1234 -> 2341)
        l_result = (now % 1000) * 10 + (now // 1000)
        # 방문하지 않았다면
        if not visited[l_result]:
            # 방문처리 및 큐에 삽입
            visited[l_result] = True
            queue.append((l_result, path + ['L']))
        
        # R 연산(1234 -> 4123)
        r_result = (now % 10) * 1000 + (now // 10)
        # 방문하지 않았다면
        if not visited[r_result]:
            # 방문처리 및 큐에 삽입
            visited[r_result] = True
            queue.append((r_result, path + ['R']))
        
for _ in range(T):
    start_num, end_num = map(int, sys.stdin.readline().strip().split(" "))
    visited = [False] * 10000
    path = bfs(start_num, visited, end_num)
    print("".join(path))