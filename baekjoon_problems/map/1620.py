"""
도감에 포켓몬을 입력하고 숫자가 주어지면 포켓몬의 이름을, 포켓몬의 이름이 주어지면 숫자를 출력하는
문제이다.

포켓몬의 이름은 딕셔너리를 이용하여 포켓몬의 이름을 키, 현재 포켓몬의 인덱스를 값으로 기록한다. 이를
사용하면 포켓몬의 이름이 주어졌을 경우, 원하는 숫자를 출력할 수 있다. 그리고 포켓몬의 이름을
리스트에 입력하여 인덱스를 활용해 숫자가 주어졌을 경우 포켓몬의 이름을 출력하도록 풀이하였다.

또는 두 개의 딕셔너리를 사용해 하나는 포켓몬이름-숫자, 하나는 숫자-포켓몬이름을 기록해서 풀이할 수도 있다.
중요한 점은 포켓몬이름으로 데이터를 저장하기 위해서 해시 구조를 사용한다는 점이다.

"""

import sys

# 도감으로 주어질 숫자, 문제로 주어질 숫자
N, M = map(int, sys.stdin.readline().strip().split(" "))
# 포켓몬 이름, 숫자를 입력할 딕셔너리
string_dict = dict()
# 인덱스에 따라서 포켓몬 이름을 추가할 리스트
num_dict = []

for i in range(N):
    value = sys.stdin.readline().strip()
    # 딕셔너리에 키, 숫자 입력
    string_dict[value] = i + 1
    # 리스트에 이름 입력
    num_dict.append(value)
    
for i in range(M):
    value = sys.stdin.readline().strip()
    # 주어진 값이 알파벳이라면 -> 딕셔너리 활용하여 숫자 출력
    if value.isalpha():
        print(string_dict[value])
    # 주어진 값이 숫자라면 -> 리스트 활용하여 포켓몬 이름 출력
    else:
        print(num_dict[int(value) - 1])