"""
대칭 차집합을 출력하라

check_dict라는 딕셔너리를 선언한 후, 딕셔너리를 이용해서 우선 A의 원소들을 키로 지정하고 
값은 1로 지정해서 모두 입력해준다. 그 후 B의 원소들을 check_dict에 입력해주는데 이미 키가 있다면
둘의 공집합에 해당하므로 값을 1 더해주고, 그렇지 않다면 값을 1로 지정해서 넣어준다.
그 후 순회하면서 값이 1로 지정되어 있다면 A-B 또는 B-A의 집합이므로 이들의 수를 세면 대칭
차집합에 해당하므로 이를 출력해준다. 다만 문제에서 A와 B 집합에 중복되는 값이 나오지 않는다라는 말이
있으므로 각 단계에서(A 순회 -> B 순회) 중복되는 원소가 있다면 한 번씩만 입력되도록 처리해야한다.
"""

# 딕셔너리를 이용하여 문제 풀이
def solution1():
    import sys

    # A 원소의 개수, B 원소의 개수
    A, B = map(int, sys.stdin.readline().strip().split(" "))
    # set으로 설정하여 중복되는 원소는 제거
    A_array = set(list(map(int, sys.stdin.readline().strip().split(" "))))
    B_array = set(list(map(int, sys.stdin.readline().strip().split(" "))))

    check_dict = dict()

    for num in A_array:
        check_dict[num] = 1
            
    for num in B_array:
        if num not in check_dict:
            check_dict[num] = 1
        else:
            check_dict[num] += 1
            
    answer = 0

    for value in check_dict.values():
        if value == 1:
            answer += 1
            
    print(answer)

# 비트 연산자를 이용하여 문제 풀이
def solution2():
    import sys

    # A 원소의 개수, B 원소의 개수
    A, B = map(int, sys.stdin.readline().strip().split(" "))
    A_array = set(list(map(int, sys.stdin.readline().strip().split(" "))))
    B_array = set(list(map(int, sys.stdin.readline().strip().split(" "))))
    
    # A_array와 B_array의 합집합에서 둘의 공집합을 뺀 개수를 출력
    print(len(A_array | B_array) - len(A_array & B_array))
    
solution2()