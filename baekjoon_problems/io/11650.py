"""
N개의 줄에 점을 정렬한 결과를 출력하라
x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬
"""

import sys

# 점의 개수
N = int(sys.stdin.readline())
# 좌표
array = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split(" "))
    array.append((x, y))
    
# 정렬 수행
array.sort(key=lambda point: (point[0], point[1]))
for x, y in array:
    print(x, y)