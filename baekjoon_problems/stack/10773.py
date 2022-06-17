"""
모든 수를 적은 후 그 수의 합을 출력하라

잘못된 수를 알려줄 경우 0을 외쳐서 가장 최근의 수를 지우도록 한다고 문제에서 주어졌다. 따라서
가장 최근의 데이터를 제거하는데 연산이 O(1)의 시간복잡도가 걸리는 스택을 사용하면 문제를 
O(N)의 시간복잡도로 문제를 풀이할 수 있다. 그 이유는 스택은 후입선출이므로 가장 최근에 들어간
데이터가 먼저 나오기 때문이다.

해당 문제는 스택의 개념을 알고있는지 묻는 문제인듯하다. 
"""

import sys

# 수의 개수
K = int(sys.stdin.readline().strip())
# 스택의 역할을 수행하는 변수
stack = []

for _ in range(K):
    num = int(sys.stdin.readline().strip())
    # 잘못된 수라면 가장 최근의 수 제거
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
        
print(sum(stack))