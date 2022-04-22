"""
주어진 수 N개 중에서 소수가 몇 개인지 출력하라

하나하나 제곱근까지 확인하는 방식으로 풀면 수의 최대 개수 * 최대 값의 제곱근으로
O(N * (1000)의 제곱근)의 시간 복잡도로 풀 수 있다. 따라서 2초안에 풀 수 있지만
에라토스테네스의 체를 사용하면 더 빠르게 풀이할 수 있다.

에라토스테네스의 체는 주어진 최대 수 까지 iteration하면서 현재 가장 작은
값들의 배수를 제거해나가는 방식으로 문제를 풀이할 수 있다.
즉, 2부터 순회하면서 2를 제외한 2의 배수들은 모두 소수가 아니므로 False로 처리하고,
그 다음 작은수인 3을 제외한 3의 배수들은 모두 소수가 아니므로 False로 처리한다.
이와 같은 방식을 N까지 하면 되는데 여기서 소수는 제곱근까지만 확인해도 계산할 수 있으므로
제곱까지만 iteration하면 된다.
"""

import math
import sys

# 수의 개수
N = int(sys.stdin.readline())
# 숫자
nums = list(map(int, sys.stdin.readline().split(" ")))
# 소수를 판별할 array
array = [True for i in range(1001)]

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(1000)) + 1): # 2부터 n의 제곱근까지 iterate
    if array[i] == True: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수 지우기
        j = 2
        while i * j <= 1000:
            array[i * j] = False
            j += 1
            
answer = 0    
# nums 확인
for num in nums:
    if num != 1 and array[num]:
        answer += 1
        
print(answer)