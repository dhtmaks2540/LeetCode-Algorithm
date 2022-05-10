"""
회의의 시작시간과 끝나는 시간이 주어지고 회의가 겹치지 않게 회의실을 사용할 수 있는 회의의 최대 개수

데이터의 최대 개수는 100,000으로 만약 완전탐색으로 탐색을 수행한다면, n-1번씩 n번 탐색하므로 
시간복잡도가 O(N^2)이 나오므로 풀이할 수 없다. 따라서 O(NlogN)을 이용하는 풀이법이 필요하다.
우리에게 주어진 값은 시작시간과 끝나는 시간이 있다. 이를 사용해서 회의를 최대 개수로 출력해야 하므로
어떠한 값을 기준으로 사용하면 회의실을 최대로 사용할 수 있다고 생각했다. 즉, 그리디하게 접근하면
문제를 풀이할 수 있다고 판단했다. 끝나는 시간이 빠른 회의를 먼저 사용하게 되면 가장 많은 회의가
가능하기에 (끝나는 시간, 시작 시간)을 기준으로 정렬을 수행한 후에 현재 시간이 시작 시간보다 작다면
(회의가 가능하다면) 정답처리 후 현재 시간을 끝나는 시간으로 갱신하여 문제를 풀이하였다.
"""

import sys

# 회의의 수
N = int(sys.stdin.readline().strip())
# 회의 시작, 끝
array = list()
for _ in range(N):
    start, end = map(int, sys.stdin.readline().strip().split(" "))
    array.append((start, end))
    
# 끝나는 시간을 기준으로 정렬 수행
array.sort(key=lambda time: (time[1], time[0]))
time = 0
answer = 0

for start, end in array:
    if time <= start:
        time = end
        answer += 1
        
print(answer)