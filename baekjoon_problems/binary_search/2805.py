"""
적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값

1654번 문제와 비슷한 문제로 나무의 높이가 최대 1,000,000,000이다. 이를 완전 탐색으로
모두 찾는다고 하면 시간 제한안에 풀이할 수 없다. 따라서 이분 탐색을 사용해서 절단기의 높이를
min, max로 놓고 해당 절단기로 잘랐을 때의 나무의 길이를 target으로 잡아서 이를 비교하여 풀이한다.
다만 절단기에 설정할 수 있는 높이의 최댓값을 출력해야 하므로 Upper Bound를 찾아야 한다.

해당 문제는 target이 목표값보다 크거나 같을 경우 min을 늘리고,
target이 목표값보다 작으면 max를 줄여나간다. 그러다가 min_len이 max_len의 크기를 넘어서면
해당 그 값이 Upper Bound에 해당하기에 그 값에서 1을 뺀 값이 결과값이 된다.

"""

import sys

# 나무의 수, 목표 나무 길이
N, M = map(int, sys.stdin.readline().strip().split(" "))
# 나무의 높이
array = list(map(int, sys.stdin.readline().strip().split(" ")))

max_len = max(array)
min_len = 0

while min_len <= max_len:
    mid = min_len + (max_len - min_len) // 2
    
    target = 0
    for num in array:
        if num > mid:
            target += (num - mid)
            
    if target >= M:
        min_len = mid + 1
    else:
        max_len = mid - 1
        
    print(f"target : {target}, min_len : {min_len}, max_len : {max_len}")
    
print(min_len - 1)