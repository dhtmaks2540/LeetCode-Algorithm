"""
좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하라

"""

import sys

# 점의 개수
N = int(sys.stdin.readline())
points = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split(" "))
    points.append((x, y))
    
# 정렬 수행
points.sort(key = lambda point: (point[1], point[0]))
for x, y in points:
    print(x, y)