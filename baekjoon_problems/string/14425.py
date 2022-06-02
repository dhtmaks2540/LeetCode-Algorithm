"""
집합 S가 주어지고, 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이
총 몇개인지 구하는 문제이다.

우선 주어지는 S를 딕셔너리를 이용해서 키로 지정하고 값은 0으로 지정한다. 그 후 나오는 M개의 문자열을
딕셔너리에 이미 선언되어 있다면 집합 S에 포함되는 것이므로 값을 1 증가시키도록 한다. 최종적으로
값들의 합을 출력하면 정답이 된다.
"""

import sys

# 집합에 포함된 문자열의 개수, 검사해야할 문자의 개수
N, M = map(int, sys.stdin.readline().strip().split(" "))
s_dict = dict()

for _ in range(N):
    value = sys.stdin.readline().strip()
    s_dict[value] = 0
    
for _ in range(M):
    value = sys.stdin.readline().strip()
    if value in s_dict:
        s_dict[value] += 1
        
print(sum(s_dict.values()))