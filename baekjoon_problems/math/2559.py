"""
입력되는 온도의 수열에서 연속적인 K일의 온도의 합이 최대가 되는 값을 출력하라

해당 문제는 주어진 구간만큼 매번 계산을 수행하면 시간 복잡도가 O(수의 개수 * 구간의 개수)에 해당하여
시간 제한안에 풀이할 수 없는 문제이다. 따라서 접두사의 합이라는 구간 합을 계산하는 방법을 사용해서
풀이할 수 있는데, 어차피 수는 한번만 주어지고 구간만 변경되는 것이므로 미리 수의 합을 계산하고
주어진 구간에 따라서 미리 계산된 값을 사용해 정답을 출력해주는 방법으로 풀이할 수 있다.
따라서 미리 구간 합을 계산한 후 범위가 주어지면 pre[end] - pre[start - 1]을 출력해주면 된다.
"""

import sys

# 날짜의 수, 합을 구하기 위한 연속적인 날짜의 수
N, K = map(int, sys.stdin.readline().strip().split(" "))
array = list(map(int, sys.stdin.readline().strip().split(" ")))

# 구간 합을 저장할 리스트
prefix_sum = [0]
# 값을 누적할 변수
sum_value = 0
# 최대 구간 값을 출력할 변수
max_sum = -sys.maxsize

# 구간 합 계산
for i in range(N):
    sum_value += array[i]
    prefix_sum.append(sum_value)

# 주어진 구간을 탐색하며
for i in range(K, N + 1):
    # 최댓값 갱신
    max_sum = max(max_sum, prefix_sum[i] - prefix_sum[i - K])
    
print(max_sum)