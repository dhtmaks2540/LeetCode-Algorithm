"""
방법을 생각하다가 자릿수가 최대 4자릿수이기에 에라토스테네스의 체를
사용해서 4자릿수의 소수를 모두 구한 뒤 DFS를 통해 해당 인덱스의 값을
0 ~ 9(첫 인덱스는 1 ~ 9)로 변경한 후 해당 값이 소수이고 방문하지 않았다면
DFS를 또 호출하는 방식으로 풀이했다. 하지만 이 방법은 깊이 우선 탐색이므로
계속해서 탐색하다가 목표값을 만났을 경우 바로 기록해버린다. 따라서 이후에 더 나은 방법으로
접근하더라도 방문처리가 이미 되어있기에 이 문제는 DFS를 통해 풀이할 수 없다.

힌트를 보니 BFS를 사용하라고 나와있어서 이를 사용하면 풀이할 수 있을 것 같아지만 코드가 제대로
짜지지 않았다... 멘붕와도 계속해서 코딩하면서 생각하는 힘을 길러야겠다..

"""     
def solution2():
    import math
    import sys
    import collections
    
    # 에라토스테네스의 체
    n = 9999
    array = [True] * (n + 1)
    # 소수 판별
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    
    def bfs(start):
        queue = collections.deque()
        queue.append(start)
        visited[start] = 0
        
        while queue:
            now = queue.popleft()
            
            # 맨 앞자리 부터 4자리 검사
            for i in range(4):
                str_now = list(str(now))
                # 모든 자리를 0 ~ 9로 변환
                for j in range(10):
                    str_now[i] = str(j)
                    next = int("".join(str_now))
                    # 다음 이동하려는 숫자가 4자리 수이고 소수이며 방문하지 않았다면
                    if next >= 1000 and array[next] and visited[next] == -1:
                        # 방문 처리
                        visited[next] = visited[now] + 1
                        # 큐 삽입
                        queue.append(next)
                        
     # 테스트 케이스
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        # 방문확인용 리스트
        visited = [-1] * (n + 1)
        
        before_num, after_num = map(int, sys.stdin.readline().strip().split(" "))
        bfs(before_num)
        
        if visited[after_num] != -1:
            print(visited[after_num])
        else:
            print("Impossible")
            
solution2()