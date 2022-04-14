"""
주어진 조건대로 학생의 성적을 정렬하라

"""

import sys

# 학생의 수
N = int(sys.stdin.readline())
array = []
for _ in range(N):
    # 이름, 국어, 영어, 수학
    name, kor, eng, mat = sys.stdin.readline().strip().split(" ")
    array.append((name, int(kor), int(eng), int(mat)))

# 정렬 수행
# 국어는 감소하는 순으로
# 영어는 증가하는 순으로
# 수학은 감소하는 순으로
# 이름은 사전 순으로 증가하는 순으로
array.sort(key=lambda student: (-student[1], student[2], -student[3], student[0]))

for name, _, _, _ in array:
    print(name) 