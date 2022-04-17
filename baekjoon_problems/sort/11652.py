"""
-2^62 이상 2^62 이하의 값이 적힌 카드들이 주어질 때,
가장 많이 가지고 있는 값을 출력하라. 개수가 같으면 작은 값 먼저 출력하라

"""

import sys
import collections

# 숫자 카드의 개수
N = int(sys.stdin.readline())
# 카드의 정수
numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))
    
counts = collections.Counter(numbers)
items = counts.most_common()
# 정렬 수행
items.sort(key=lambda item: (-item[1], item[0]))
print(items[0][0])