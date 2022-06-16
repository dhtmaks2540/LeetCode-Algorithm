"""
도로의 제일 왼쪽 도시에서 제일 오른쪽 도시로 이동하는 최소의 비용을 계산하라

우선 문제에서 예시로 주어진 예를 들어 설명하면 제일 왼쪽도시부터 1,2,3,4라고 한다면
1번에서 4번으로 가는 최소의 비용은 1번에서 2번으로 가는 비용과 2번에서 4번으로 가는 비용의 합이다.
즉, 최적 부분 구조에 해당하게 된다. 여기서 다이나믹 프로그래밍 또는 그리디 알고리즘을 생각할 수 있는데
이 문제에서는 피보나치 수열처럼 하위 문제의 정답이 중복되지 않는다. 따라서 그리디 알고리즘을 
사용하여 풀이해보자고 생각했다. 이제 현재 상황에서 최선의 선택을 하고 해당 선택이 정당한지 파악해야
하는데, 현재 주유소의 금액이 이후에 나오는 주요소보다 더 싸다면 현재 주유소의 금액으로 더 비싼
주유소에서 다음 주유소까지 가는 비용을 채워버리도록 풀이하면 문제를 풀이할 수 있다.

예를 들어, 5 - 2 - 3 - 4 - 1의 주유소 비용과 2, 3, 2, 4라는 거리가 주어진다고 가정해보자.
처음에 출발할 때 5는 2의 비용보다 비싸므로 다음 주유소로 가기 위한 비용만 채우고, 이후 2의 주유소는
그 다음에 나올 3, 4 주유소보다 금액이 싸기에 2 비용을 지불하고 끝까지 가는 기름을 채워버리면 된다.
이와 같은 방식으로 풀면 O(N)의 시간복잡도를 가지고 풀이할 수 있는데 주의할 점은 인덱스를 잘 생각해서
풀이해야 한다는 것이다. 그 이유는 주유소는 총 N개가 주어지고 거리는 총 N-1 이 주어지기 때문이다.

현재의 문제는 그리디 알고리즘으로 풀이할 수 있는 이유와 그 최적의 선택을 도출하는 방법을 알아갈 수
있는 것 같다.

"""


import sys

# 도시의 개수
N = int(sys.stdin.readline().strip())
# 도로의 길이
road_array = list(map(int, sys.stdin.readline().strip().split(" ")))
# 주유 비용
price_array = list(map(int, sys.stdin.readline().strip().split(" ")))

# 금액을 저장하기 위한 변수
price = 0
index = 0
# 현재의 주유소 인덱스
now_index = 0

while index <= N - 2:
    now_index = index
    
    # 현재 주유소 기름 채우기
    price += price_array[now_index] * road_array[index]
    index += 1
    # 만약 다음의 주유소보다 현재 주유소가 더 싸다면
    if price_array[now_index] <= price_array[index]:
        # 조건을 만족하는 동안
        while index <= N - 2 and price_array[now_index] <= price_array[index]:
            # 현재 주유소로 기름 넣기
            price += price_array[now_index] * road_array[index]
            index += 1
             
print(price)