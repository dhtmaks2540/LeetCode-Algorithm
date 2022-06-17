"""
1~n까지의 숫자와 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 출력하라

처음에 문제를 잘못이해해 방향을 잡지 못했지만 문제를 이해하고 쉽게 풀이했다. 우선 1~n까지의
숫자는 계속해서 순회해야하기 때문에 for문을 사용해서 순회하도록 했다. 이때 순회하면서
현재의 값을 스택에 넣은 후, 수열의 현재 인덱스 값과 가장 최근에 넣은 데이터를 비교하는데 값이 같으면
stack에서 pop하도록 했다. 다만 이때 값이 같은 동안 모두 pop 하기 위해서 while문으로 처리했다.

위와 같이 풀이한 후 스택에 값이 남아있으면 정상적으로 주어진 수열을 만들지 못하는 경우이므로
NO를 출력하고, 스택이 비어있다면 정상적으로 수열은 만든 경우이므로 push, pop 연산의 순서를 출력해주면
된다.

현재 문제는 스택을 사용해서 원하는 값을 만들 수 있는지 묻는 문제로, 스택의 개념과 이를 응용하는
구조를 판단할 수 있는 문제인듯하다.
"""

import sys

# 1부터 n까지의 수
n = int(sys.stdin.readline().strip())
# 수열
correct_array = []
for _ in range(n):
    correct_array.append(int(sys.stdin.readline().strip()))
    
# 스택의 역할을 수행하는 변수
stack = []
# 결과값을 저장하기 위한 변수
answer = []
# 1 ~ n
array = [i for i in range(1, n + 1)]
# 수열을 가리키는 인덱스
index = 0

# 1 ~ n까지 순회
for num in array:
    # 스택에 현재 값 추가
    stack.append(num)
    answer.append('+')
    
    # 가장 최근에 저장된 데이터가 수열의 현재 인덱스의 값과 같다면
    if stack[-1] == correct_array[index]:
        # 인덱스가 범위를 벗어나지 않았으며 스택에 값이 있고 값이 같은 동안에
        while index < n and stack and stack[-1] == correct_array[index]:
            # 정답 변수에 값 추가 및 인덱스 증가
            stack.pop()
            answer.append('-')
            index += 1
            
# 스택에 값이 남아있지 않다면 정상적으로 수열이 출력된 상황
if not stack:
    for x in answer:
        print(x)
else:
    print("NO")