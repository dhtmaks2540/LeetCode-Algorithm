"""
회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오도록 정렬
"""

import sys

# 회원의 수
N = int(sys.stdin.readline())
# 나이와 이름
array = []
for i in range(N):
    age, name = sys.stdin.readline().strip().split(" ")
    # 가입한 순을 기록하기 위해 index 추가
    array.append((i, int(age), name))

# 정렬 수행
array.sort(key=lambda user: (user[1], user[0]))
for index, age, name in array:
    print(age, name)