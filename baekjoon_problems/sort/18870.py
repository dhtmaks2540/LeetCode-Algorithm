"""
https://st-lab.tistory.com/279

좌표를 압축하는 문제로 현재 값은 현재 값보다 큰 값의 수로 출력하는 문제이다. 이를 살펴보면
중복을 제거하고 정렬을 수행한 후, 그 값의 인덱스를 계산하는 방법으로 풀이할 수 있다.
따라서 정렬을 수행한 후 순회하면서 현재 값이 딕셔너리에 없다면 추가하고 카운트를 증가하는 방식으로
풀이할 수 있다.
"""


import sys

# 좌표의 개수
N = int(sys.stdin.readline().strip())
# 좌표
array = list(map(int, sys.stdin.readline().strip().split(" ")))
# 중복제거 및 오름차순 정렬 수행
sorted_set_array = sorted(set(array))
# 결과를 저장할 딕셔너리
answer_dict = dict()

for index in range(len(sorted_set_array)):
    answer_dict[sorted_set_array[index]] = index
    
for num in array:
    print(answer_dict[num], end=" ")