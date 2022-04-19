"""
모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하라

해당 문제는 시간제한이 굉장히 작으므로 시간 복잡도를 유의해서 코드를 작성해야 한다.

"""

import sys
import collections

# 문자열
array = list(sys.stdin.readline().strip())
# 명령어의 개수
M = int(sys.stdin.readline().strip())
# 명령어
orders = []
lst = collections.deque()

for _ in range(M):
    order = list(sys.stdin.readline().strip().split())
    # 왼쪽으로 이동한다면 array의 마지막 원소 다른 리스트로 삽입
    if order[0] == "L" and array:
        lst.insert(0, array.pop())
    # 오른쪽으로 이동한다면 다른 리스트의 첫 번째 원소 array에 삽입
    if order[0] == "D" and lst:
        array.append(lst.popleft())
    # 원소 삭제
    if order[0] == "B" and array:
        array.pop()
    # 원소 삽입
    if order[0] == "P":
        array.append(order[1])
        
answer = array + list(lst)
print("".join(answer))