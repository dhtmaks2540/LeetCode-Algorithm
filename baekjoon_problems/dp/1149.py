"""
규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값

i번째 집은 i - 1번째 집과 i + 1번째 집과 다른 색으로 칠해야 한다. 이를 생각하면
현재의 집은 이전의 집에서 현재의 색과 다른 색중 더 작은 값으로 칠하면서 이를 빨,초,파
모두의 색에 계속해서 적용해가면 된다. 즉, 예를 들어 현재의 색을 빨간색으로 칠한다고 가정하면
이전의 초록색, 파랑색으로 칠해진 값중 더 작은 값을 가져와서 현재의 빨간색 값과 더해주는 방식이다.
이는 값을 기록하기 위해 새로운 리스트를 선언할 필요 없이 문제에서 주어진 빨,초,파 값의 리스트를
사용해서 풀이할 수 있다.
"""

import sys

# 집의 수
N = int(sys.stdin.readline().strip())
# 빨강, 초록, 파랑
price = []
for _ in range(N):
    price.append(list(map(int, sys.stdin.readline().strip().split(" "))))

# 두 번째 리스트부터
for i in range(1, N):
    # 빨, 초, 파 순회
    for j in range(3):
        # 가장 작은 값을 기록하기 위한 변수
        min_price = sys.maxsize
        # 빨, 초, 파 순회
        for k in range(3):
            # 현재의 색이 이전의 색과 다르며 현재 가장 작은 값이라면 갱신
            if j != k and min_price > price[i - 1][k]:
                min_price = price[i - 1][k]
        # 현재의 값에 이전의 가장 작은 값 더해주기
        price[i][j] += min_price
        
print(min(price[N - 1]))