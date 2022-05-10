"""
수열이 주어졌을 때, 각 수를 적절히 묶어서 그 합이 최대가 되도록 하라.

예시로 준 부분을 보다보니 양수는 큰 양수끼리 묶는 것이 더 큰값이 되고 음수 또는 0과는 묶으면 안되며,
1의 경우는 그냥 더하는 것이 더 합을 크게 만드는 것을 파악했다.
음수는 더 작은 음수끼리 묶는 것이 더 큰값이 되고 양수와는 묶으면 안되며,
만약 묶지 못한 음수가 남아 있고 0이 있다면 이 둘을 곱해서 없애는 방법이 더 합을 크게 만드는 것을 
파악했다. 즉, 현재 상황에서 최적의 선택을 해서 정답을 도출하는 그리디 알고리즘으로 풀이했다.
"""

import sys

# 수열의 크기
N = int(sys.stdin.readline().strip())
pos_num = []
neg_num = []

# 양수와 음수 나누기
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    if num <= 0:
        neg_num.append(num)
    else:
        pos_num.append(num)
        
answer = 0

# 양수는 내림차순, 음수는 오름차순으로 정렬
pos_num.sort(reverse=True)
neg_num.sort()

temp_stack = []

for num in pos_num:
    # 1이라면 그냥 더하기
    if num == 1:
        answer += 1
    # 스택에 값이 없다면 넣기
    elif not temp_stack:
        temp_stack.append(num)
    # 스택에 값이 있다면 빼서 두 수를 묶은 후 더하기
    else:
        answer += num * temp_stack.pop()

# 남은 수 처리     
if temp_stack:
    answer += temp_stack.pop()
    
temp_stack = []
    
for num in neg_num:
    # 스택에 값이 없다면 넣기
    if not temp_stack:
        temp_stack.append(num)
    # 스택에 값이 있다면 빼서 두 수를 묶은 후 더하기
    else:
        answer += num * temp_stack.pop()

# 남은 수 처리
if temp_stack:
    answer += temp_stack.pop()
    
print(answer)