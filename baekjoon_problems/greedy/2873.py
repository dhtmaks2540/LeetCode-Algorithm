"""
큰 기쁨을 주는 방향으로 롤러코스터를 이동해라

https://jaimemin.tistory.com/729

즉, 모든 경우의 수를 탐색하는 완전 탐색이 아닌 조건을 주고 현재 상황에서 점수를 최고로 얻을 수 있도록
나아가는 방식으로 문제를 풀이하는 그리디 알고리즘을 사용할 수 있다고 생각했다.

행이 홀수인 경우는 모두 방문할 수 있고 행이 짝수이고 열이 홀수인 경우도 모두 방문할 수 있다는 것을
파악해서 이를 코드로 구현하였다. 다만 행, 열이 모두 짝수인 경우는 답이 조금 복잡해지는데 
시작점과 도착점을 흰색이라고 표시하고 검은색, 흰색을 차례대로 동서남북에 표시한다. 그렇게 되면
흰색 -> 검은색 -> 흰색 -> ... 순서로 방문함을 알 수 있는데 
1. 만약 흰색 칸 하나를 방문하지 않기로 한다면 도착점까지 남은 칸을 모두 방문할 수 없다.
2. 검은 칸 하나를 방문하지 않기로 한다면 그 칸을 제외하고 도착점까지 남은 칸을 모두 방문할 수 있다.
3. 따라서, 검은 칸에 점수 중 최소인 지점을 찾아 해당 칸을 방문하지 않으면 된다.
"""

import sys

# 행, 열
R, C = map(int, sys.stdin.readline().strip().split(" "))
graph = []
for _ in range(R):
    graph.append(list(map(int, sys.stdin.readline().strip().split(" "))))

answer = ""

if R % 2:
    for y in range(R):
        for x in range(C - 1):
            if y % 2 == 0: # 짝수라면 오른쪽으로
                answer += 'R'
            else: # 홀수라면 왼쪽으로
                answer += 'L'
        # 아직 도착하지 못했다면
        if y != R - 1:
            answer += 'D'
elif R % 2 == 0 and C % 2 != 0: # 행 짝수, 열 홀수
    for x in range(C):
        for y in range(R - 1):
            if x % 2 == 0:
                answer += 'D'
            else:
                answer += 'U'
        if x != C - 1:
            answer += 'R'
elif R % 2 == 0 and C % 2 == 0:
    min_point = (0, 0)
    min_score = sys.maxsize
   
    for y in range(R):
        for x in range(C):
            # 검은칸이고 최소 점수라면
            if (y + x) % 2 and min_score > graph[y][x]:
                min_score = graph[y][x]
                min_point = (y, x)
                
    # 지나지 말아야 할 좌표의 최좌측으로 내려오고
    newR = min_point[0] - 1 if min_point[0] % 2 else min_point[0]
    for y in range(newR):
        for x in range(C - 1):
            if y % 2 == 0:
                answer += 'R'
            else:
                answer += 'L'
        answer += 'D'
    # 지나지 말아야 할 좌표의 대각선 아래까지 이동
    newC = min_point[1]
    for x in range(newC):
        if x % 2 == 0:
            answer += 'DR'
        else:
            answer += 'UR'
    # 지나지 말아야 할 좌표의 최우측으로 이동
    for x in range(newC, C - 1):
        if x % 2 == 0:
            answer += 'RD'
        else:
            answer += 'RU'
    # 목적지까지
    if min_point[0] % 2 == 0:
        newR = R - (min_point[0] + 2)
    else:
        newR = R - (min_point[0] + 1)
        
    for y in range(newR):
        answer += 'D'
        for x in range(C - 1):
            if y % 2 == 0:
                answer += 'L'
            else:
                answer += 'R'
            
print(answer)