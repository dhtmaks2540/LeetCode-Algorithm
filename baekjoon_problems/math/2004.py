"""
끝자리 0의 개수를 출력하라

순열과 소인수 분해를 사용하여 문제 풀이

https://st-lab.tistory.com/166

순열과 소인수 분해를 통해 푸는 방법은 생각했으나 조금만 더 생각하지 않고 풀이를 포기했다...
해당 문제는 1676번의 문제와 똑같이 10의 승수를 생각해서 문제를 풀이하면 된다.
다만 1676번은 5의 개수가 당연히 적다고 판단하고 5만을 생각했지만 해당 문제는 조합을
풀이하는 것이므로 nCm 이라고 한다면 (n)! / (n - m)! * (m!)을 풀이하는 문제이다. 따라서
5가 적을 수도 있고 2가 적을 수도 있으므로 이 둘을 모두 판단하는 방식으로 풀이하면 된다.
"""

import sys

n, m = map(int, sys.stdin.readline().strip().split(" "))

# 5의 승수
def five_power_n(num):
    count = 0
    
    while num >= 5:
        count += num // 5
        num //= 5
        
    return count

# 2의 승수
def two_power_n(num):
    count = 0
    
    while num >= 2:
        count += num // 2
        num //= 2
        
    return count

# 순열 계산
count_5 = five_power_n(n) - five_power_n(m) - five_power_n(n - m)
count_2 = two_power_n(n) - two_power_n(m) - two_power_n(n - m)

# 2 또는 5의 승수 중 더 작은 값을 정답으로 출력
print(min(count_5, count_2))