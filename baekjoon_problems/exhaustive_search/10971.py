"""
가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하라

시작점에서 모든 노드를 한번씩 방문하고 다시 시작점으로 돌아오기 위해서 재귀적으로 탐색하며 
조건을 사용해 재귀를 종료하는 방식으로 풀이하였다. 모든 노드를 시작점으로 탐색하기 위해서
노드를 iteration하면서 재귀함수로 완전 탐색을 수행한다. 그리고 재귀 함수 속에서
원하는 조건이 되었을 경우(임시 리스트에 저장된 노드의 개수가 모든 노드의 개수와 같다면)
마지막 노드에서 시작 노드로 가는 거리 추가(시작 노드로 다시 돌아와야하므로)한 후 최솟값을
갱신하는 방식으로 풀이했다. 다만 알고리즘의 시간복잡도가 좋지는 않은듯하다..

항상 DFS를 사용할 때 path와 in의 메서드를 사용하기보다는 visited를 사용해서 시간복잡도를
줄이는 방식으로 풀이하는게 좋다!
"""

def solution1():
    import sys

    # 도시의 수
    N = int(sys.stdin.readline().strip())
    # 비용
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().strip().split(" "))))
        
    min_price = sys.maxsize

    def recursive(price, path):
        global min_price
        
        # 모두 탐색했을 경우
        if len(path) == N:
            # 외판원 순회이므로 자기 자신으로 돌아가기
            # 다만 이동할 수 있을 경우에만 처리
            if graph[path[-1]][path[0]] != 0:
                price += graph[path[-1]][path[0]]
                min_price = min(min_price, price)
            return
        
        # 연결된 노드 확인
        for index in range(N):
            # 현재 노드와 다음 노드가 연결되어 있고, 아직 방문하지 않았다면
            if graph[path[-1]][index] != 0 and index not in path:
                # 다음 노드 추가하고 빼기
                price += graph[path[-1]][index]
                recursive(price, path + [index])
                price -= graph[path[-1]][index]
    
    # 모든 노드 시작점으로 하여 탐색      
    for i in range(N):
        recursive(0, [i])
    
    # 최솟값이 갱신되지 않았다면 방문하지 못하는 경우
    if min_price == sys.maxsize:
        print(0)
    else:
        print(min_price)
        
# 똑같은 DFS 방식이지만 최적화 진행
# https://blockdmask.tistory.com/229
def solution2():
    import sys

    # 도시의 수
    N = int(sys.stdin.readline().strip())
    # 비용
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().strip().split(" "))))

    visited = [False] * (N)
    min_price = sys.maxsize

    # 시작 도시, 현재 도시, 합, 방문한 도시 개수
    def dfs(start, y, sum_price, cnt):
        global min_price
        
        # 종료조건
        # 모든 도시를 방문했으며 현재 도시가 시작 도시와 같다면
        if cnt == N and start == y:
            min_price = min(min_price, sum_price)
            return
        
        for x in range(N):
            # 연결되지 않은 경우
            if graph[y][x] == 0: continue
            
            # 아직 방문하지 않은 경우
            if not visited[y]:
                # 방문처리
                visited[y] = True
                sum_price += graph[y][x]
                
                # 현재까지 더한 값이 min_price보다 작은 경우에만 탐색
                if sum_price <= min_price: 
                    # [1,2]이었다면 [2,-]로 보내줌
                    dfs(start, x, sum_price, cnt + 1)
                    
                # 방문한 기록과 합 초기화
                visited[y] = False
                sum_price -= graph[y][x]
                
    for i in range(N):
        # 각각의 도시에서 시작
        dfs(i, i, 0, 0)
        
    if min_price == sys.maxsize:
        print(0)
    else:
        print(min_price)
    
# solution2()