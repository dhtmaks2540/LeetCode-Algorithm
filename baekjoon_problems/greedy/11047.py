"""
K원을 만드는데 필요한 동전 개수의 최솟값을 출력하라

그리디 알고리즘으로 풀이할 수 있는 대표적인 문제이다. 가치의 합을 K원을 만드는데 동전 개수를 최솟값
으로 만들기 위해서는 가장 큰 동전부터 차례대로 최대한 사용하는 방식으로 풀이하면 동전 개수를
최솟값으로 만들 수 있다. 다만 이 문제를 그리디 알고리즘으로 풀이할 수 있는 이유는 동전의 가치가
배수로 존재하기 때문이다. 동전의 가치가 배수로 존재하지 않는다면 이 방법을 사용해서 문제를 
풀이할 수 없고 다이나믹 프로그래밍을 사용해서 풀이해야 한다.

그리디 알고리즘은 현재 상황에서 뒤의 상황은 생각하지 않고 최적의 조건을 고르는 방식으로 문제를 풀이
할 수 있다.
"""

import sys

# 동전의 종류, 목표 가치
N, K = map(int, sys.stdin.readline().strip().split(" "))
# 동전의 종류
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline().strip()))

answer = 0

for i in range(-1, -len(array) - 1, -1):
    answer += K // array[i]
    K %= array[i]
        
print(answer)