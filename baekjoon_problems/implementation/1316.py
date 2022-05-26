"""
이미 나온 글자가 다시 나오지 않는지 체크하는 문제이다. 
가장 첫 번째 글자를 우선 prev라는 변수에 저장해두고 해시 테이블(딕셔너리)를 사용해서
그 값을 기록한다. 그리고 그 이후의 값들을 확인하며 prev에 저장된 값과 다른 경우
방문했는지 체크하고 방문하지 않았다면 방문 처리 후 prev 변수를 갱신하고,
이미 방문했다면 글자가 다시 나온 경우이므로 무시하도록 처리했다. 

"""

import sys

# 단어의 개수
N = int(sys.stdin.readline().strip())
# 단어
array = []
for _ in range(N):
    array.append(sys.stdin.readline().strip())
answer = 0

for i in range(N):
    # 방문을 확인하기 위한 딕셔너리
    visited = {}
    # 첫 번째 글자
    prev = array[i][0]
    # 첫 번째 글자 방문 처리
    visited[prev] = True
    check = True
    for j in range(1, len(array[i])):
        # 새로운 글자가 온 경우
        if prev != array[i][j]:
            # 이미 방문했다면 그룹 단어 X
            if array[i][j] in visited:
                check = False
                break
            # 방문하지 않았다면 방문처리 및 이전 글자 변경
            else:
                visited[array[i][j]] = True
                prev = array[i][j]
                
    if check:
        answer += 1
        
print(answer)