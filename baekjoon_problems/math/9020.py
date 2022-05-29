"""
짝수가 주어지면 두 소수의 합으로 나타내라

우선 에라토스테네스의 체를 사용하여 10,000까지의 소수를 모두 판별할 후
값이 주어지면 해당 값의 절반까지 탐색하면서 값에 현재 소수의 값을 뺀 값이 소수라면 정답에 저장한다.
이를 절반까지 탐색하게되면 가장 소수의 차이가 작은 값이 저장될테고, 이를 출력하였다.

"""

import sys
import math

# 에라토스테네스의 체를 사용하여 소수 판별
MAX_VALUE = 10000
prime_num = [True] * (MAX_VALUE + 1)

for i in range(2, int(math.sqrt(MAX_VALUE)) + 1):
    if prime_num[i]:
        j = 2
        while i * j <= MAX_VALUE:
            prime_num[i * j] = False
            j += 1
            
# 테스트 케이스
T = int(sys.stdin.readline().strip())
for _ in range(T):
    answer = (0, 0)
    target = int(sys.stdin.readline().strip())
    
    for i in range(2, target // 2 + 1):
        # 현재 값이 소수이고, 골드바흐 파티션이 된다면
        if prime_num[i] and prime_num[target - i]:
            answer = (i, target - i)
            
    print(f"{answer[0]} {answer[1]}")