"""
https://st-lab.tistory.com/155

N개의 숫자가 주어졌을 경우 M으로 나누었을 때, 나머지가 모두 같게 되는 M을 모두 찾아라.

임의의 정수 A1과 A2는 아래와 같이 표현할 수 있다.(M : 나눈 수, r : 나머지)
A1 = M * a1 + r1
A2 = M * a2 + r2

이 때 나머지가 같아야 하기에 A1에서 A2를 빼면 아래와 같다
A1 - A2 = M * (a1 - a2) + (r1 - r2) -> r1 - r2 = 0이므로 A1 - A2 = M * (a1 - a2)
M은 (A1 - A2)의 약수이므로 A1과 A2의 공약수가 된다. 위의 방법을 사용해서 모든 숫자에 대한
최대 공약수를 뽑아내고, 그 최대 공약수를 이용해서 약수들을 구해 출력하면 문제의 정답이 된다.

이 문제는 브루트 포스로 풀이하면 절대로 풀이할 수 없다. 따라서 위와 같은 수학적 관점을 생각해서
풀이해야 하는데, 이것저것 수식을 적어보며 풀이해야 할 듯 하다..
"""

import sys
import math

# 숫자의 개수
N = int(sys.stdin.readline().strip())
array = list()
for _ in range(N):
    array.append(int(sys.stdin.readline().strip()))

# 유클리드 호제법을 사용하여 최대 공약수를 반환
def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
        
    return a

# 정렬 수행
array.sort()
# 첫 번째 최대 공약수
gcd_value = array[1] - array[0]
for i in range(2, N):
    # 직전의 최대 공약수와 다음 수의 최대 공약수를 갱신
    gcd_value = gcd(gcd_value, array[i] - array[i - 1])

answer = set()
    
# 최대공약수의 약수 찾기(제곱근 이용)
for i in range(2, int(math.sqrt(gcd_value)) + 1):
    # 현재 값으로 나누어 떨어진다면 -> 약수
    if gcd_value % i == 0:
        answer.add(i)
        answer.add(gcd_value // i)
        
answer.add(gcd_value)
# 작은 값부터 출력해야하므로 정렬 후 출력
print(*sorted(list(answer)))