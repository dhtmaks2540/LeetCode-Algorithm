"""
M이상 N이하의 소수를 모두 출력하라

에라토스테네스의 체를 사용하여 문제를 풀이하면 O(NloglogN)으로 풀이할 수 있다. 이때, N이
1,000,000이라고 하더라도 4,000,000 정도에 해당한다.

해당 문제는 총 시간 복잡도가 O((N - M) * 1000000loglog1000000) 이다.
"""

import math

# M과 N
M, N = map(int, input().split(" "))
# 소수를 나타낼 배열
array = [True] * (N + 1)
# 1은 소수 X
array[1] = False

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(N)) + 1):
    if array[i]:
        # 배수
        j = 2
        while i * j <= N:
            array[i * j] = False
            j += 1
            
for i in range(M, N + 1):
    if array[i]:
        print(i)