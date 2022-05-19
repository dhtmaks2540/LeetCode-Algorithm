"""
자연수 N을 연속된 소수의 합으로 나타내라

에라토스테네스의 체를 사용하여 소수를 구한 후 투포인터를 사용해서 연속된 수열의 합이 목표값에
해당하는 값을 찾는다. 이 문제에서 투 포인터를 이용할 수 있는 이유는 소수 모두 양수이며
연속된 수열의 합을 찾기에 시작점과 끝점을 사용해서 끝점을 증가시키면 합이 늘어나고, 시작점을
증가시키면 합이 감소하기 때문이다. 이를 사용해서 문제를 풀이할 수 있다.
"""

import sys
import math

target = int(sys.stdin.readline().strip())

# 에라토스테네스의 체를 사용하여 소수 판별
prime_num = [True] * (target + 1)

for i in range(2, int(math.sqrt(target)) + 1):
    if prime_num[i] == True:
        j = 2
        while i * j <= target:
            prime_num[i * j] = False
            j += 1
            
numbers = []
for i in range(2, len(prime_num)):
    if prime_num[i] == True:
        numbers.append(i)
    
answer = 0
# 끝점
end = 0
# 합계
interval_sum = 0

# 시작점은 계속 증가
for start in range(len(numbers)):
    # 현재의 합이 목표값보다 작으며 아직 끝점에 도달하지 않은 동안
    while interval_sum < target and end < len(numbers):
        # 끝점을 증가시키며 합계를 증가
        interval_sum += numbers[end]
        end += 1
    
    # target과 같다면
    if interval_sum == target:
        answer += 1
    
    # 시작점은 계속 증가하므로 마지막에 시작점의 값 감소
    interval_sum -= numbers[start]
    
print(answer)