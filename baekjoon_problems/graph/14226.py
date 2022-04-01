"""
영선이가 S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값을 구하라

BFS를 사용하여 문제 풀이

https://jdselectron.tistory.com/57

* 초기 화면에는 하나의 이모티콘이 존재 (즉, display = 1, clipboard = 0, time = 0 상태에서 탐색 시작)
* 1. display에 있는 모든 이모티콘을 clipboard에 저장 -> clipboard = display, time += 1
* 2. clipboard에 있는 모든 이모티콘을 display에 붙여넣기 -> display += clipboard, time += 1
* 3. display의 이모티콘에서 하나를 제거 -> display -= 1, time += 1
* display에 s개의 이모티콘이 존재할 때 탐색 종료

필요한 세 개의 변수를 사용해서 큐에 저장하고 이를 조건에 잘 맞게 구현하는 것이 핵심..!!
"""
import collections

MAX_SIZE = 5
S = int(input())
# 방문처리를 확인할 리스트(display, clipboard)
visited = [[False] * MAX_SIZE for _ in range(MAX_SIZE)]
print(visited)
# BFS 탐색을 위한 큐 선언 및 현재 위치 방문 처리
queue = collections.deque()
queue.append((1, 0, 0))

# 큐에 값이 있는 동안
while queue:
    display, clipboard, time = queue.popleft()
    
    # 현재 값이 목표값과 같다면
    if display == S:
        print(time)
        exit()
        
    if 0 <= display < MAX_SIZE:
        # 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장
        if not visited[display][display]:
            visited[display][display] = True
            queue.append((display, display, time + 1))
        
        # 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
        if clipboard > 0 and display + clipboard < MAX_SIZE:
            if not visited[display + clipboard][clipboard]:
                visited[display + clipboard][clipboard] = True
                queue.append((display + clipboard, clipboard, time + 1))
                
        # 화면에 있는 이모티콘 중 하나를 삭제
        if not visited[display - 1][clipboard]:
            visited[display - 1][clipboard] = True
            queue.append((display - 1, clipboard, time + 1))