import sys

"""
접근방법

투 포인터를 사용하여 왼쪽,오른쪽 포인터 사이의 숫자들의 합을 계산하였다. 
이 계산된 값을 이용하여 목표값보다 크거나 같으면 왼쪽 포인터를 움직여 더 줄여도 조건을 만족하는지
파악하고, 목표값보다 작으면 오른쪽 포인터를 움직여서 값을 키워주는 방식으로 풀이하였다.
다만, 투 포인터 범위의 조건을 잘못사용하여 오답이 계속 도출됐는데 
조건을 잘 파악하도록 하자.. 


https://paris-in-the-rain.tistory.com/127
"""

# 투 포인터를 사용하여 풀이
def use_two_pointer():
    sys.stdin = open("input.txt", "rt")

    # 길이, 목표값
    N, S = map(int, input().split())
    # 수열
    array = list(map(int, input().split()))
    # 왼쪽, 오른쪽 포인터, 중간계산 
    left, right, cur = 0, 0, 0
    # 정답
    answer = sys.maxsize

    while True:
        # 현재 합이 목표값보다 크거나 같으면
        # 왼쪽 포인터를 이동하여 더 줄일 수 있는지 파악
        if cur >= S:
            # 개수를 최소로 하기위한 갱신
            answer = min(answer, right - left)
            cur -= array[left]
            left += 1
        # 오른쪽 포인터가 리스트의 범위를 벗어나면
        elif right == N:
            break
        # 현재 합이 목표값보다 작다면
        # 오른쪽 포인터를 이동하여 값 늘리기
        else:
            cur += array[right]
            right += 1

    if answer == sys.maxsize:
        print(0)
    else:
        print(answer)

"""
풀이방법

구간합을 미리 계산해놓으면 i부터 j까지의 숫자의 합을 빠르게 계산할 수 있기에 구간합을 사용해서 풀이할 수
있다. 구간합을 계산하는 방법은 여러가지 방법이 있지만 기본적인 접근은 현재 배열의 길이보다 1 더 큰 구간합 
리스트를 선언한다. 그 후 배열의 첫 번쨰 원소부터 누적으로 더해나가면서 구간합 리스트에 추가하면 된다.
그리고 만약 i번째부터 j번째까지 구간합을 계산하라는 문제가 나온다면 prefix[j] - prefix[i-1]를 계산하면
된다. 따라서 구간합 문제의 시간복잡도는 원소의 개수가 M, 쿼리의 개수가 N 이라고 한다면 O(N+M)이
되는 것이다.

현재 문제의 경우 위의 방법을 사용하여 구간합을 계산한 후 구간합이 목표값보다 크면 개수를 갱신한 후
왼쪽 포인터를 이동해서 구간을 줄이고 목표값보다 작다면 오른쪽 포인터를 이동해서 구간을 늘리는 방식으로
풀이하면 된다.
"""

def use_pre_fix():
    N, S = map(int, input().split())
    array = list(map(int, input().split()))
    prefix = [0] * (N + 1)
    start, end = 0, 1

    # 구간합계산
    for i in range(1, N + 1):
        prefix[i] = prefix[i - 1] + array[i - 1]

    answer = sys.maxsize

    while start < N:
        # 목표값보다 크거나 같다면
        if prefix[end] - prefix[start] >= S:
            answer = min(answer, end - start)
            start += 1
        # 목표값보다 작다면
        else:
            # end가 범위안에 포함될 경우
            if end < N:
                end += 1
            # end가 범위안에 포함되지 않을 경우
            else:
                start += 1

    if answer == sys.maxsize:
        answer = 0

    print(answer)