"""
소용돌이를 예쁘게 출력하라

https://kswims.tistory.com/138

구현 문제로 문제의 조건에 맞게 코드로 구현하면 된다...

우선 r2 - r1은 40보다 작거나 같고 c2-c1은 4보다 작거나 같기에 해당 크기 만큼만 배열을 만들어
공간을 낭비하지 않도록 한다. 

소용돌이치는 규칙을 살펴보면 동서남북 총 4방향으로 돌고 있는데 방향이 두번 바뀔 때마다 한 방향에서
전진해야하는 카운트가 증가한다. 이 규칙을 통해서 방향을 바꿔주며 좌표를 갱신해주면 된다.
그리고 해당 문제는 (0,0)에서 소용돌이를 시작해야하므로 x,y 값은 실제 소용돌이가 치는(음수를 포함하는)
좌표를 뜻하게 구현헀다. 그런데 출력을 위해 할당한 graph에 그리기 위해서는
음수를 포함하는 좌표를 사용할 수 없으므로 (x-r1, y-c1) 로 값을 계산해주어서 기록을 하는 범위인
(r1, c1) ~ (r2, c2)로 매칭한다.
"""
        
def solution2():
    import sys

    # (r1, c1) 가장 왼쪽 위, (r2, c2)는 가장 오른쪽 아래 = (행, 열)
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split(" "))
    # 0 <= r2 - r1 <= 49, 0 <= c2 - c1 <= 4
    graph = [[0] * 5 for _ in range(50)]
    # graph 원소의 개수
    number_of_graph = (c2 - c1 + 1) * (r2 - r1 + 1)
    # 동서남북 방향을 나타냄
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    x = y = 0
    dir = 3
    dcnt = num = 1
    cnt = 0
    
    # 가장 왼쪽 위, 아래와 가장 오른쪽 위, 아래의 좌표가 채워지지 않았다면
    # while not(graph[0][0] != 0 and graph[0][c2-c1] != 0 and graph[r2-r1][0] != 0 and graph[r2-r1][c2-c1] !=0):
    # 아직 graph의 원소의 개수만큼 채우지 않았다면
    while number_of_graph != 0:
        # 범위 안에 graph가 포함될경우
        if r1 <= x <= r2 and c1 <= y <= c2:
            graph[x - r1][y - c1] = num
            number_of_graph -= 1
        
        # 현재 숫자 및 전진 count 증가
        num += 1
        cnt += 1
        
        # 방향에 따라서 x, y 좌표 이동
        x = x + dx[dir]
        y = y + dy[dir]
        
        # 전진해야하는 카운트와 같다면
        if cnt == dcnt:
            cnt = 0
            # 방향 계산
            dir = (dir + 1) % 4
            # 동쪽 또는 서쪽으로 간다면 전진해야하는 카운트 증가
            if dir == 3 or dir == 1:
                dcnt += 1
    
    cnt = 0
    
    # num은 현재 최댓값 -> 자릿수 계산
    while num > 0:
        num //= 10
        cnt += 1 # 출력폭을 찾기 위해서
        
    for i in range(r2 - r1 + 1):
        for j in range(c2 - c1 + 1):
            print(str(graph[i][j]).rjust(cnt), end=" ")
        print()
        
solution2()