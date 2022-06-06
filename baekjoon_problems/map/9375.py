"""
해빈이가 가진 의상들이 주어졌을때 해빈이가 알몸이 아닌 상태로 며칠동안 돌아다닐 수 있는가
 
https://st-lab.tistory.com/164
 
[headgear]
hat
turban

[eyewear]
sunglasses

위와 같이 두 종류의 옷과 세 개의 옷의 이름이 주어졌을 때, 알몸이 되지 않는 조합을 짜면 아래와 같다.

한 개만 입을 경우 : {hat}, {turban}, {sunglasses}
두 개씩 조합하여 입을 경우 : {hat, sunglasses}, {turban, sunglasses}

일단 중복해서 입을 수 없기에 옷의 종류별로 구분한 뒤 각각의 경우의 수를 구하면 된다.
이는 옷의 종류를 키로 하는 맵(딕셔너리)를 사용하여 저장하면 된다.

[headgear] : hat, turban
[eyewear] : sunglasses

이제 한 종류의 옷의 개수에서 1개를 선택하는 경우를 생각해보자.

headgear의 경우는 2개 있으니 2가 아닌 3이 되어야 한다. 그 이유는 headgear를 끼는 경우를
생각하면 hat과 turban이 있으므로 2지만, 옷을 안 입는 경우도 생각해야 하므로 총 3가지가 된다.
eyewear도 마찬가지로 안 입는 경우를 따져서 1이 아닌 2가 되어야 한다. 이를 다시 나타내면
아래와 같다.

[headgear] : hat, turban, NULL
[eyewear] : sunglasses, NULL

이제 각 종류별로 하나씩 고르는 조합을 계산하며 곱해주면 된다.
위 예시는 3C1 * 2C1 = 3 * 2 = 6의 결과가 나온다. 하지만 이때, 알몸이 아닌 상태는 포함하면
안되므로 headgear와 eyewear가 각각 NULL이 선택된 한 가지 경우의 수를 빼야하므로 최종적으로
6 - 1 = 5의 결과가 나온다.
"""

import sys

# 테스트 케이스
T = int(sys.stdin.readline().strip())

for _ in range(T):
    cloth_dict = dict()
    
    # 의상의 수
    N = int(sys.stdin.readline().strip())
    
    for _ in range(N):
        cloth_name, cloth_type = sys.stdin.readline().strip().split(" ")
        # 없는 종류라면 1로 초기화
        if cloth_type not in cloth_dict:
            cloth_dict[cloth_type] = 1
        # 이미 있는 종류라면 개수 1 증가
        else:
            cloth_dict[cloth_type] += 1
            
    answer = 1
    
    # 안 입는 경우를 고려하여 각 종류별 옷의 개수에 1 더해준 값을 곱한다.
    for value in cloth_dict.values():
        answer *= (value + 1)
    
    # 알몸인 상태를 제외해야하므로 최종값에 -1 반영
    print(answer - 1)