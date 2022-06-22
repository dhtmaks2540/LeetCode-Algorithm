"""
배열의 초깃값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하라

주어진 조건을 구현하는 문제로 문제 자체는 간단하나 시간 복잡도를 중시해야 하는 문제이다. 우선
배열의 최대 길이가 100,000이고 연산의 최대 길이도 100,000이기에 매번 P연산에 대해서 배열의 수를
뒤집어 버리면 O(100,000 * 100,000)의 시간복잡도가 걸리고 이렇게 되면 문제를 절대 시간 제한안에 풀이할 
수 없다. 따라서 다른 방법을 떠올려야 하는데 D의 연산은 배열의 앞에서 부터 값을 추출한다고 나와있다.
앞에서 부터 값을 추출하기에 Deque를 떠올릴 수 있고, Deque를 사용하면 pollFirst()를 통해 O(1)의 시간복잡도를
가지고 값을 추출할 수 있다. 따라서 기본적인 자료구조는 Deque로 잡고, P의 연산이 나왔을 경우는
D의 연산을 앞에서 부터 추출하지 않고 뒤에서 부터 추출하도록 변경시켜주면 매번 reverse를 할 필요없이
Deque이기에 O(1)의 시간 복잡도를 가지고 P의 연산도 수행할 수 있게 된다. 그리고 마지막에 출력할 때는
거꾸로 연산이 수행되어 있다면 단지 뒤집어서 결과를 출력하면 되기 때문이다. 이렇게 되면 시간 제한안에
문제를 풀이할 수 있게 된다.

현재 문제는 Deque의 개념과 문자열 파싱 그리고 원하는 조건을 구현할 수 있는지를 물어보는 문제인듯하다.
시간 제한안에 풀기 위해 Deque의 개념을 잘 사용하여 양쪽에서 pop을 수행하도록 해야한다. 또한 시간 복잡도
를 최대한 줄이는 것이 이러한 문제의 특징이기에 연산을 복잡하게 수행하지 말고 더 간단한 방법을
생각하는 것이 좋을 듯 하다.
"""

import sys
from collections import deque

# 테스트 케이스
T = int(sys.stdin.readline().strip())
for _ in range(T):
    # 수행할 함수
    func_array = list(sys.stdin.readline().strip())
    # 수의 개수
    n = int(sys.stdin.readline().strip())
    # 배열 입력
    num_array = sys.stdin.readline().strip()
    # 대괄호 제거하고 숫자만 가져오기
    num_array = num_array[1:len(num_array) - 1].split(",")
    # Deque
    queue = deque()
    # Deque에 숫자만 삽입
    for value in num_array:
        if value.isdigit():
            queue.append(value)
            
    error_check = False
    reverse_check = False
            
    for func in func_array:
        if func == 'R':
            # 현재 함수가 R이라면 거꾸로 체크 
            reverse_check = not reverse_check
        else:
            # 큐에 값이 없다면 -> Error
            if not queue:
                error_check = True
                break
            # 큐에 값이 있는 경우
            else:
                # 거꾸로 체크가 되어 있다면 앞이 아닌 뒤에서 값을 뽑기
                if reverse_check:
                    queue.pop()
                # 그렇지 않다면 정상적으로 앞에서 값을 뽑기
                else:
                    queue.popleft()
    
    # 에러가 발생했다면        
    if error_check:
        print("error")
    # 큐에 값이 비어있다면
    elif not queue:
        print("[]")
    else:
        # 거꾸로 체크가 되어있다면 뒤집어서 출력
        if reverse_check:
            queue.reverse()
            
        print("[", end="")
        for i in range(len(queue) - 1):
            print(queue[i], end=",")
        print(f"{queue[-1]}]")