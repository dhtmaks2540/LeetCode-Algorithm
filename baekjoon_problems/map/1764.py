"""
듣도 못한 사람과 보도 못한 사람이 주어졌을 때, 듣도 보도 못한 사람의 명단을 구하라

듣도 못한 사람을 키로 값은 1로 딕셔너리를 선언한다. 그리고 보도 못한
사람을 순회하면서 듣도 못한 사람의 딕셔너리에 현재 값이 있다면 +1을 해주고, 없다면 1을
선언한다. 그리고 딕셔너리를 순회하면서 현재 값이 2라면 듣도 보도 못한 사람이므로
이 사람들을 정답으로 출력하면 된다.
 
즉, 해시구조를 사용하여 문제를 풀이하는 것으로 듣도 못한 사람을 저장하는데 N의 시간이, 
보도 못한 사람을 검사하는데 N의 시간이 걸리므로 O(2N) -> O(N)의 시간복잡도로 문제를 풀이할 수 있다.
"""

import sys
import collections

# 듣도 못한 사람의 수, 보도 못한 사람의 수
N, M = map(int, sys.stdin.readline().strip().split(" "))
person_dict = collections.defaultdict(int)

# 듣도 못한 사람 기록
for _ in range(N):
    person = sys.stdin.readline().strip()
    person_dict[person] += 1

# 보도 못한 사람 기록  
for _ in range(M):
    person = sys.stdin.readline().strip()
    person_dict[person] += 1
    
answer = []
for key, value in person_dict.items():
    # 듣도 못했을 때 1을 더해주고, 보도 못했을 때 1을 더해주므로 2라면 듣도 보도 못한 사람이다.
    if value == 2:
        answer.append(key)

# 사전순으로 출력하기 위해서 정렬 수행
answer.sort()
print(len(answer))
for person in answer:
    print(person)