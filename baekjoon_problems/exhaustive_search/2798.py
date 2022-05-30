"""
카드가 주어지면 3장을 뽑아서 최대한 주어진 값을 넘지 않으면서 최대한 가까운 수를 만들어라

문제의 답을 찾기 위해서는 모든 경우의 수를 확인하는 방법말고는 없다. 따라서 주어진 숫자들 중
세 카드를 뽑아서 그 합이 목표값과 가장 가까운 경우를 확인해야 하는데 이는 조합을 사용해서
확인할 수 있다.
"""

import sys
import itertools

# 카드의 개수, 목표 값
N, M = map(int, sys.stdin.readline().strip().split(" "))
array = list(map(int, sys.stdin.readline().strip().split(" ")))
# 목표값과 가장 작은 차이를 기록하는 변수
min_diff = sys.maxsize
answer = 0

# 주어진 배열에서 3개를 뽑는 조합을 순회하며
for numbers in list(itertools.combinations(array, 3)):
    sumValue = sum(numbers)
    # 그 값들의 합이 목표값보다 작거나 같으며 차이가 현재 기록된 값보다 작다면
    if sumValue <= M and M - sumValue < min_diff:
        min_diff = M - sumValue
        answer = sumValue
        
print(answer)