"""
A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력하라. 만들 수 없는 경우에는 -1을 출력

문제의 조건에 맞게 그리디 알고리즘으로 풀이

A를 B로 바꾸는게 가능하냐는 뜻은 B를 A로 바꾸는게 가능하냐는 뜻이므로
더 큰 수 B를 A로 조건에 맞게 바꾸다가 바꿀 수 없으면 -1을 출력하고 바꿀 수 있으면 최솟값에 + 1을 추가하여
반환한다.

https://covenant.tistory.com/147

BFS 탐색으로도 풀이가 가능하다. BFS는 현재 원소의 인접한 값들을 탐색하는 방식으로 풀이하는데
해당 문제는 A를 B로 변경하는데, 2를 곱하거나 마지막 자릿수에 1을 더하는 규칙으로만 바꿔야한다.
따라서 현재 값에서 2를 곱한 값과 마지막 자릿수에 1을 더한 값이 목표값보다 작다면 계속해서
큐에 넣고 빼면서 목표값과 같은지 비교하는 방식으로 풀이하면 된다.
"""

def greedy():
    a, b = input().split()
    answer = 0

    # b의 값이 a보다 큰 동안에
    while int(b) > int(a):
        # b의 마지막 값이 1이라면
        if b[-1] == '1':
            # 1 제거
            b = b[:len(b) - 1]
            answer += 1
        # 2로 나누어 떨어진다면
        elif int(b) % 2 == 0:
            # 2로 나누기
            b = str(int(b) // 2)
            answer += 1
        # 그 밖의 경우는 만들 수 없는 경우이므로 -1 출력
        else:
            print(-1)
            exit()

    # 최종적으로 같은 값이라면
    if a == b:   
        print(answer + 1)
    # 아니라면
    else:
        print(-1)

def bfs():
    import collections

    A, B = map(int, input().split())

    # BFS 탐색을 위한 큐 선언 및 결과변수
    q = collections.deque()
    q.append((A, 1))

    while q:
        # 현재 값, 결과변수
        x, t = q.popleft()
        # 목표값과 같다면 결과 출력 후 exit
        if x == B:
            print(t)
            exit()
            
        
        # 2를 곱한 값과 마지막 자릿수에 1을 더한 값이 목표값보다 작다면 큐에 계속해서 삽입해주면서
        # 그 값을 목표값과 비교하는 방식으로 문제 풀이
        
        # 만약 현재 값에 2를 곱한 값이 목표값보다 작거나 같다면
        if x * 2 <= B:
            q.append((x * 2, t + 1))
        # 현재 값의 마지막 자리에 1 추가
        x = int(str(x) + "1")
        # 만약 현재 값의 마지막 자리에 1 추가한 값이 B보다 작다면 
        if x <= B:
            q.append((x, t + 1))
        
    print(-1)