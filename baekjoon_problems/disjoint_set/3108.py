"""
N개의 직사각형을 그리는데 필요한 PU 명령의 최솟값 -> 연결되어 있지 않은 직사각형이 몇개인가.
PU 명령은 거북이가 고개를 드는 명령인데, (0, 0)에서 시작하는 거북이의 PU 명령의 최솟값을 만들라는 것은
최대한 거북이가 고개를 들지 않고 연결된 직사각형들을 그리도록 하는 것이다. 따라서 따로 연결되어 있지
않은 직사각형의 개수를 파악하면 된다.

그림으로 그려보니 서로 떨어진 직사각형의 개수를 파악하는 것이 정답인것을 깨달았다. 다만 문제를 접근하지
못해서 힌트를 찾아봤는데 Disjoint-Set 기법이 나와있어서 이를 사용해 풀이하려고 했는데 2차원 배열을
Union-Find 하는 방법을 생각하지 못했다...

https://yabmoons.tistory.com/179

이 블로그는 DFS를 사용하여 풀이하였는데 우선 좌표가 -500 ~ 500이므로 이를 배열로 나타내기 위해서
값에 500을 더해 모두 양수로 만든다. 이렇게 되면 시작점이 (500, 500)이 되고 음수였던 좌표들도
모두 양수로 표현할 수 있다. 이제 DFS를 호출하면서 떨어져 있는 사각형의 위치를 확인해야 하는데 
예제 입력의 3번을 보면 (3, 3), (6, 6) - (4, 4), (5, 5)는 원래 떨어져 있는 사각형이다. 하지만
DFS를 호출하게 되면 이 둘은 붙어있는 상태가 되므로 좌표를 다시 * 2를 해줘서 떨어뜨린다. 이렇게 되면
원래의 좌표에 500을 더하고 * 2를 해주었기 때문에 시작점은 (1000, 1000)이 된다.

DFS를 호출할 때는 현재 위치에 사각형이 그러져 있다면(graph[i][j] == 1) DFS를 호출해 붙어 있는 사각형
들도 모두 방문처리하고 count를 1 증가시킨다. 다만 시작점 (1000, 1000)이 2라면 시작점에서 연결된
사각형이 하나 있는것이므로 count를 1 감소시키면 정답이 된다.
"""

# DFS를 사용하여 문제 풀이
def solution1():
    import sys
    sys.setrecursionlimit(10**5)

    # 직사각형의 개수
    N = int(sys.stdin.readline().strip())
    # 좌표
    graph = [[0] * 2001 for _ in range(2001)]

    for _ in range(N):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split(" "))
        
        # 원래의 좌표에서 모두 양수로 표현하기 위해 500을 더하고
        # 원래 떨어져 있는 사각형을 표현하기 위해서 * 2
        x1 = (x1 + 500) * 2
        y1 = (y1 + 500) * 2
        x2 = (x2 + 500) * 2
        y2 = (y2 + 500) * 2
        
        # 직사각형 그래프에 표현
        for i in range(x1, x2 + 1):
            graph[y1][i] = 1
            graph[y2][i] = 1
        
        for i in range(y1, y2 + 1):
            graph[i][x1] = 1
            graph[i][x2] = 1
            
    move_dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(x, y):
        # 이미 방문했다면 return
        if graph[x][y] == 2:
            return
        
        # 방문 처리
        graph[x][y] = 2
        
        # 동서남북 확인
        for i in range(4):
            next_x, next_y = x + move_dxy[i][0], y + move_dxy[i][1]
            
            # 정상 범위이면 재귀 호출
            if 0 <= next_x < 2001 and 0 <= next_y < 2001 and graph[next_x][next_y] == 1:
                dfs(next_x, next_y)
                
    answer = 0
                
    for i in range(2001):
        for j in range(2001):
            # 현재 위치가 1이라면 -> 직사각형이 있다는 뜻이므로 DFS 호출
            if graph[i][j] == 1:
                dfs(i, j)
                answer += 1
                
    # 시작점에서 그려진 직사각형이 있다면 정답 감소        
    if graph[1000][1000] == 2:
        answer -= 1
        
    print(answer)

"""
https://imnotabear.tistory.com/155

서로 사각형이 겹치게 되면 Union을 사용하여 Disjoint-Set을 만든 후 그 개수를 파악하여
문제를 풀이

"""    

def solution2():
    import sys
    
    class Point:
        def __init__(self, x1, y1, x2, y2):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
    
    # 부모 노드를 찾는 메서드
    def find_parent(parent, x):
        if parent[x] == x:
            return x
        
        parent[x] = find_parent(parent, parent[x])
        
        return parent[x]
    
    # 두 노드를 합치는 메서드
    def union(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        
        if a > b:
            parent[a] = b
        else:
            parent[b] = a
    
    # 두 노드가 만나는지 확인
    def meet(i, j):
        a = points[i]
        b = points[j]
        
        # 큰 B 사각형안에 작은 A 사각형이 있는 경우
        if b.y2 > a.y2 and a.x2 < b.x2 and a.y1 > b.y1 and b.x1 < a.x1:
            return False
        
        # 큰 A 사각형안에 작은 B 사각형이 있는 경우
        if a.y2 > b.y2 and b.x2 < a.x2 and b.y1 > a.y1 and b.x1 > a.x1:
            return False
        
        # 사각형 A의 상하좌우로 B 사각형이 위치하여 A와 겹치지 않는 경우
        if b.y1 > a.y2 or b.x1 > a.x2 or a.y1 > b.y2 or b.x2 < a.x1:
            return False
        
        return True
        
        
    # 직사각형의 개수
    N = int(sys.stdin.readline().strip())
    
    parent = [0] * (N + 1)
    # 부모노드 초기화
    for i in range(1, N + 1):
        parent[i] = i
        
    points = []
    
    # 시작점 추가
    zero_point = Point(0, 0, 0, 0)
    points.append(zero_point)
    
    for i in range(N):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split(" "))
        point = Point(x1, y1, x2, y2)
        points.append(point)
    
    for i in range(N):
        for j in range(i + 1, N + 1):
            # 만약 현재 사각형과 다른 사각형이 만난다면
            if meet(i, j):
                # 두 노드의 합치기
                union(parent, i, j)
                
    answer = set()
    for i in range(N + 1):
        answer.add(find_parent(parent, parent[i]))
    
    # 시작점(0, 0)이 추가되어 있으므로 1 감소
    print(len(answer) - 1)
    
solution2()