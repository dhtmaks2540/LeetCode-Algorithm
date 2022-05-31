"""
나보다 키와 덩치가 모두 큰 사람의 수를 세고난 후, 그 사람이 K명이라면 자신은 K + 1등이 되도록
표시하는 문제이다. 따라서 정렬이나 이런걸 사용할 필요없이 자신의 키와 몸무게를 남들과 비교하며
현재 자신보다 그 두개가 모두 크다면 등수를 올리고, 최종적으로 나온 등수에 + 1을 해서 자신의 등수로
기록하는 방식으로 풀이하면 된다. 즉, 브루트포스 알고리즘을 사용하면 되는데, 인원이 최대 50명이기에
시간복잡도가 최대 49 * 50이므로 충분히 풀이할 수 있다.

이 문제를 정렬을 사용하지 않고 브루트포스를 사용한 이유는 몸무게나 키를 사용하여 정렬하더라도
정렬된 상태에서 현재 사람의 몸무게가 상대방보다 크다고 가정하더라도 키는 작을 수 있기에
모든 사람을 직접 한명씩 탐색해야 한다.
"""

import sys

# 사람의 수
N = int(sys.stdin.readline().strip())
array = []
for _ in range(N):
    wei, hei = map(int, sys.stdin.readline().strip().split(" "))
    array.append((wei, hei))
    
answer = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        # 현재 나와 다른 사람이고, 나의 키와 몸무게보다 모두 크다면
        if i != j and (array[i][0] < array[j][0] and array[i][1] < array[j][1]):
            # 등수 증가
            cnt += 1
    answer[i] = cnt + 1
    
for x in answer:
    print(x, end=" ")