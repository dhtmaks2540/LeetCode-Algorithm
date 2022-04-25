"""
수열이 주어질 때, 반복되는 부분을 제외하고 남게 되는 수들의 개수를 출력하라

반복수열은 반복되는 숫자가 나온다면 그때부터 반복되는 부분이 될것이다.
따라서 하나의 리스트에 계속해서 수열을 기록하면서 현재 값이 리스트에 있다면 반복되는 부분으로 판별한다.
그리고 그 값의 인덱스를 제외한 나머지의 개수를 출력하도록 풀이했다.
"""

import sys

# 완전 탐색(브루트포스)
def solution():
    A, P = map(int, sys.stdin.readline().split(" "))
    path = [A]
    repeat_num = 0

    while True:
        num = 0
        while A:
            num += (A % 10)**P
            A //= 10
        if num not in path:
            path.append(num)
            A = num
        else:
            repeat_num = num
            break
    
    repeat_index = path.index(repeat_num)
    print(len(path[:repeat_index]))
    
# solution()

"""
DFS를 사용하여 문제 풀이

"언젠가 이와 같은 반복수열이 된다"가 포인트 -> DFS나 BFS는 visited가 되어있으면 탐색을 종료하기에
for 문처럼 무한루프에 빠질수 있는 것보다 시간적으로도 풀기 좋다. 따라서 이렇게 언제 끝날지
모르는 탐색문제는 BFS나 DFS가 보통 정해라 본다.

https://jaimemin.tistory.com/946

A=9999, P=5일 때 연산 결과가 최대가 되는데 이 때 값이 30만보다 작으므로 visited 배열 크기 30만
A부터 DFS가 시작하는데 해당 숫자가 방문될 때마다 visited 배열의 해당 인덱스를 1 증가
visited 배열의 해당 인덱스 값이 3이 된다면 반복 수열이 두번째 반복하는 시점이므로 재귀 함수를 탈출
이후 visited 배열을 전부 방문하면서 한번만 등장한 숫자들의 갯수를 파악하고 출력

"""

def solution2():
    MAX = 300000 + 1
    visited = [0] * MAX
    
    def dfs(num):
        visited[num] += 1
        # 반복구간이 한번 반복되었다는 것을 의미
        if visited[num] == 3:
            return
        # 각 자리수 계산
        sum_num = 0
        while num:
            sum_num += ((num) % 10)**P
            num //= 10
            
        dfs(sum_num)
        
    A, P = map(int, sys.stdin.readline().strip().split(" "))
    
    dfs(A)
    answer = 0
    # 한번만 등장한 숫자들이 반복구간에 속하지 않는 숫자들
    for i in range(1, MAX):
        if visited[i] == 1:
            answer += 1
    
    print(answer)
    
solution2()