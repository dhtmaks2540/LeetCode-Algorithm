"""
수가 주어지고 구간이 주어지면 해당 구간 수들의 합을 출력하는 문제이다.

해당 문제를 매번 구간이 주어질때마다 계산을 하게 되면 시간 복잡도는 O(수의 개수 * 구간의 개수)에
해당한다. 그 이유는 구간이 주어질 때마다 수의 최대 범위가 주어지면 위와 같은 시간 복잡도를 가지기 
때문이다. 현재 문제에서 수의 개수는 100,000이고, 구간의 개수는 100,000이므로 시간 제한 1초안에
절대 풀이할 수 없다. 따라서 구간 합을 미리 계산하는 방식으로 풀이하여 시간 복잡도를 줄여야한다.
구간 합을 미리 계산하는 방법은 접두사의 합이 있는데, 접두사 합은 리스트의 맨 앞부터 특정 위치
까지의 합을 구해 놓는 것을 의미한다. N개의 수에 대해서 접두사 합을 계산하여 배열에 저장해놓고
쿼리 정보 L, R이 주어지면, prefix_sum[R] - prefix_sum[L]을 출력해주면 된다. 이와 같이 문제를
풀이하면 N개의 데이터와 M개의 쿼리가 있을 경우, 전체 구간을 구하는데 걸리는 시간 N과 M개의 쿼리를
처리하는데 걸리는 시간 M이 더해져서 O(N + M)의 시간 복잡도를 가지게 된다.

"""

import sys

# 수의 개수, 합을 구해야 하는 횟수
N, M = map(int, sys.stdin.readline().strip().split(" "))
array = list(map(int, sys.stdin.readline().strip().split(" ")))
# 구간 합을 저장하는 리스트
prefix_sum = [0]
sum_value = 0

# 구간 합 계산
for i in range(N):
    # 접두사 합 누적
    sum_value += array[i]
    # 구간 합 리스트에 누적
    prefix_sum.append(sum_value)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split(" "))
    print(prefix_sum[j] - prefix_sum[i - 1])