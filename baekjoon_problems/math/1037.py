"""
약수가 주어지면 수를 구하라

약수는 1과 자기 자신을 제외한 숫자중에서 나누면 나머지가 0이 되는 수이다.
약수를 오름차순으로 정렬한 후, 약수의 개수가 1개라면 해당 수를 제곱한 수가 원래의 수가 되고
그렇지 않다면 가장 큰 수와 가장 작은 수 -> 그 다음으로 큰 수와 작은 수를 곱한 수가 원래의 수가 된다.
이러한 약수의 성질을 이용해 풀이할 수 있다.

"""

import sys

# 약수의 개수
N = int(sys.stdin.readline().strip())
# 약수
array = list(map(int, sys.stdin.readline().strip().split(" ")))

# 소수는 나오지 않으므로 약수의 개수가 1이라면 제곱한 값 출력
if N == 1:
    print(array[0]**2)
else:
    # 정렬 수행
    array.sort()
    print(array[0] * array[-1])