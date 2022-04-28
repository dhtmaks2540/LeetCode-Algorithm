"""
N개를 만들 수 있는 랜선의 최대 길이

https://st-lab.tistory.com/269

랜선의 길이를 정한 후 가지고 있는 랜선의 길이를 모두 잘라보며 일일히 확인하기에는 랜선의 길이가
2^31 - 1로 완전 탐색은 불가능하다고 판단했다. 따라서 랜선의 길이는 어차피 1 ~ 2^31-1 이라는 범위
에 포함되므로 정렬되어 있다고 가정하고 이분 탐색으로 문제를 풀이했다.

해당 문제에서는 이분 탐색으로 사용되는 min과 max가 index가 아니라 랜선의 길이로 지정한다. 
즉, min은 1(0으로는 못자르므로), max는 주어진 랜선의 길이 중 최대값을 지정한다. 그 후 target과 비교해야
하는데 이 문제에서 target은 랜선의 개수에 해당한다. 따라서 이분 탐색을 통한 랜선의 길이로 
랜선들을 모두 자른 후 나온 개수들을 target과 비교한다. 다만, 해당문제는 랜선의 길이가
최대인 값을 정답으로 도출해야 하기에 원하는 값을 찾았다고 바로 정답으로 출력하면 안된다.

예를 들어서
4 11
802
743
457
539

이런 값이 주어졌을 때, 199로 자르면 11개, 200으로 자르면 11개, 201로 자르면 10개 이므로
최대 길이인 200이 도출되어야 한다. 

이를 위해 Lower bound와 Upper bound를 사용할 수 있는데
Upper Bound(상한)은 찾고자 하는 특정 값을 초과하는 '첫 위치'를 반환하고,
Lower Bound(하한)은 찾고자 하는 특정 값 이상인 '첫 위치'를 반환한다.
예를 들어서, arr = {1, 2, 2, 2, 3}이라고 할 때, target 값은 2이고, Upper Bound로 찾는다면
2를 초과되는 처음 위치인 arr[4] = 3인 index 4가 반환된다.
반대로, Lower Bound로 찾게 된다면 2 이상 위치 중 처음 위치인 arr[1] = 2인 index 1이 반환될것이다.

이를 사용해서 중복 원소에서 가장 끝 값(가장 오른쪽 값)을 찾고자 한다면 Upper Bound - 1을 하면 되고,
중복 원소 중 가장 왼쪽 끝 값(가장 왼쪽 값)을 찾고자 한다면 Lower Bound를 통해 반환 된 값 그대로가 
된다. 이 문제에서는 개수가 중복될 때 최대 길이를 찾아야 한다. 즉, Upper Bound를 통해 얻어진 값에서
-1을 해주면 최대 길이가 출력된다.
"""

import sys

# 가지고 있는 랜선의 개수, 필요한 랜선의 개수
K, N = map(int, sys.stdin.readline().strip().split(" "))
# 랜선
array = []
for _ in range(K):
    array.append(int(sys.stdin.readline().strip()))
    
# 랜선의 최대 길이
max_len = max(array)
min_len = 1
answer = 0

# 이분탐색
while min_len <= max_len:
    # 중간 값
    mid_len = min_len + (max_len - min_len) // 2
    target = 0
    # 현재 중간 값으로 랜선 잘라보기
    for num in array:
        target += num // mid_len
        
    # Upper Bound 형식
    # mid 길이로 잘랐을 때의 개수가 만들고자 하는 랜선의 개수보다 작다면
    # 자르고자 하는 길이를 줄이기 위해 최대 길이 줄인다.
    # 그 외에는 자르고자 하는 길이를 늘려야 하므로 최소 길이를 늘린다.
    if target < N:
        max_len = mid_len - 1
    else:
        min_len = mid_len + 1

# Upper Bound로 얻어진 값(min)에 -1이 최대 길이가 된다.
print(min_len - 1)