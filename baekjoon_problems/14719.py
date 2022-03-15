import sys

sys.stdin = open("input.txt", "rt")

"""
투 포인터를 활용하여 문제 풀이

알고리즘 인터뷰 with 파이썬에서 봤던 문제로 LeetCode에서 풀었던 문제이다.

해당 문제는 접근하는 방법이 투 포인터와 스택 두 가지이다.
문제의 유형은 구현이자 시뮬레이션 문제로 시뮬레이션은 일련의 명령에 따라서 개체를 차례대로 이동시키는 문제이다.
해당 문제는 주어진 그래프에서 빗물의 총 합을 계산하는 것인데 내가 원하는 조건에 따라서
해당 위치에서의 빗물의 양을 계산하고 앞으로 나아가는 방식으로 코드를 구현해야 하기에
문제의 유형이 시뮬레이션인것 같다.

우선 문제를 투 포인터를 이용해서 풀이했는데 투 포인터는 대개 정렬된 리스트에서 사용할 수 있다.
하지만 이 문제에서 투 포인터를 이용할 수 있었던 이유는 조건에 따라서 포인터가 이동할 수 있으며
두 포인터가 어디까지 움직일 수 있는지 조건을 명확히 줄 수 있기에 투 포인터로 문제를 풀이했다.

문제의 핵심은 가장 높은 높이의 블록까지 왼쪽 포인터와 오른쪽 포인터를 이동시키며 해당 위치에서 빗물을
계산하도록 풀이하였다. 그러기 위한 세부 구현으로 먼저 왼쪽, 오른쪽 포인터를 배열의 시작과 끝 인덱스로 준 후
주고 해당 위치를 기록하였다. 그리고 왼쪽 포인터와 오른쪽 포인터 중 더 작은 값을 이동시키며 기록했던 위치
보다 더 작은 값이 나오면 빗물의 양을 계산하고 더 큰값이 나오면 기록했던 위치를 갱신함므로써 문제를 풀이하였다.

"""

# 높이와 넓이
H, W = map(int, input().split())
# 블록의 높이
array = list(map(int, input().split()))

answer = 0

# 투포인터를 이용하여 문제 풀이
# def sum_of_water():
left, right = 0, W - 1
prev_left, prev_right = array[left], array[right]

# left가 right보다 작은 동안
while left < right:
    # 왼쪽 포인터가 더 작다면
    if array[left] <= array[right]:
        # 두 개의 포인터가 정상 범위이며 기록한 위치보다 작은 동안에
        while left <= right and prev_left >= array[left]:
            # 값 기록 및 왼쪽 포인터 이동
            answer += (prev_left - array[left])
            left += 1
        # 더 높은 위치로 갱신
        prev_left = array[left]
    # 오른쪽 포인터가 더 작다면
    else:
        # 두 개의 포인터가 정상 범위이며 기록한 위치보다 작은 동안에
        while left <= right and prev_right >= array[right]:
            # 값 기록 및 오른쪽 포인터 이동
            answer += (prev_right - array[right])
            right -= 1
        # 더 높은 위치로 갱신
        prev_right = array[right]

print(answer)