"""
A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하라

https://yeonstory.tistory.com/3
https://assaeunji.github.io/python/2020-05-06-bj11004/

시간 복잡도

파이썬은 대략 1초에 2천만번의 연산을 수행한다고 한다.
따라서 1초인 문제를 만났을 때, 일반적인 기준으로
* N의 범위가 500인 경우: 시간 복잡도가 O(N^3)인 알고리즘을 설계하면 풀 수 있다.
* N의 범위가 2,000인 경우: 시간 복잡도가 O(N^2)인 알고리즘을 설계하면 풀 수 있다.
* N의 범위가 100,000인 경우: 시간 복잡도가 O(NlogN)인 알고리즘을 설계하면 풀 수 있다.
* N의 버위가 10,000,000인 경우: 시간 복잡도가 O(N)인 알고리즘을 설계하면 풀 수 있다.

공간 복잡도

* 보통 코딩 테스트에서 128 ~ 512 MB로 제한
* int의 경우 약 리스트 길이가 100만개일때, 4MB
* 즉, 128MB일때 3200만개, 256MB일때 6400만개, 512MB일때 1억 2800만개 사용가능
"""

import sys

# 숫자의 개수, 몇 번째인지
N, K = map(int, sys.stdin.readline().split(" "))
array = list(map(int, sys.stdin.readline().split(" ")))
array.sort()
print(array[K - 1])