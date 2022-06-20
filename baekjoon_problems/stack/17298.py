"""
각 원소에 대해서 오큰수를 구하라. 여기서 오큰수는 현재 원소의 오른쪽에 있으면서 현재 수보다 큰 수
중에서 가장 왼쪽에 있는 수를 의미한다.

https://st-lab.tistory.com/196

우선 이 문제를 브루트 포스를 사용해서 완전 탐색을 수행한다면 이중 for문을 통해
수행하기에 수열의 크기가 최대 1,000,000이므로 시간 복잡도가 O(1,000,000 * 1,000,000)으로 
시간 제한안에 절대 풀이할 수 없다. 따라서 다른 방법을 수행해야 하는데 스택의 후입선출을 사용해서
풀이할 수 있다. 문제를 풀이하는 방법은 다음과 같다. 원소를 순회하면서 현재 원소가 스택의 최상단
값보다 작다면 스택에 현재 인덱스를 삽입하고, 현재 원소가 스택의 최상단보다 값이 크다면 
스택의 최상단의 값이 큰 동안에 스택에서 원소를 pop 해준 후 그 인덱스의 값을 현재 원소의 인덱스로
바꿔준다. 그리고 마지막에 스택에 원소가 남아 있다면 자신의 이후로 큰 값이 없는 경우로 -1로 변경하면
문제의 정답을 출력해줄 수 있다.

예시를 들어보자. {9, 5, 4, 8}이라는 수열이 주어졌다고 가정하겠다.
우선 첫 번째 원소 9는 현재 스택에 값이 없으므로 비교하지 못하기에 단지 현재 인덱스를 push한다.
두 번째 원소 5는 현재 스택의 최상단에 저장된 값 9보다 작으므로 단지 현재 인덱스를 push 한다.
세 번째 원소 4는 현재 스택의 최상단에 저장된 값 5보다 작으므로 단지 현재 인덱스를 push 한다.
네 번째 원소 8은 현재 스택의 최상단에 저장된 값 4보다 크므로 스택의 최상단 값을 pop하고 
최상단 인덱스를 현재 값인 8로 변경해준다. 그리고 최상단을 비교하면 값이 5이므로 이 값 또한
pop하고 현재 값인 8로 변경해준다. 그리고 나오는 스택의 최상단 값 9는 현재 원소 크기에 무시하고
현재 원소 8의 인덱스를 넣어준다. 이와 같은 방식을 수행하면 자신의 이후에 큰 값이 나오면 
문제에서 원하는 대로 자신의 오른쪽에서 더 큰 값으로 변경할 수 있게 된다.
순회가 끝났는데 스택에 9와 8의 인덱스가 남았으므로 이 둘은 오른쪽에 자신보다 큰 수가 없다는 의미이기에
-1로 변경해준 후 출력하면 정답이 되는 것이다.

현재 문제에서는 스택을 응용하는 방법을 물어보는 문제인듯하다. 단지 모든 수를 넣거나 하는 것이 아니라
후입선출의 특징을 사용해서 현재 원소와 이후에 나오는 수들의 대소비교를 하기 때문이다. 스택의 특징과
이를 응용하는 방법을 여러 방면으로 생각해봐야 하는 문제인것같다.
"""

import sys

# 수의 개수
N = int(sys.stdin.readline().strip())
# 수
array = list(map(int, sys.stdin.readline().strip().split(" ")))
# 스택의 역할을 수행하는 변수
stack = []

for i in range(N):
    # 현재 스택에 원소가 없거나 스택의 최상단의 원소가 더 크다면 push
    if not stack or array[stack[-1]] > array[i]:
        stack.append(i)
    # 현재 스택에 값이 있고 스택의 최상단의 원소가 더 작다면
    else:
        while stack and array[stack[-1]] < array[i]:
            index = stack.pop()
            array[index] = array[i]
        
        stack.append(i)
            
# 남아있는 원소는 모두 -1로 처리
while stack:
    array[stack.pop()] = -1
    
for num in array:
    print(num, end=" ")