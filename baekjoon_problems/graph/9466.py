"""
사이클이 존재하는 경우 한 팀이 된다. 어느 팀에도 속하지 않은 학생들의 수를 계산하라

해당 문제는 답은 도출하였지만 시간초과를 해결하지 못했다.. 시간 복잡도를 정확히 계산하는 방법과
코드를 정리하며 최적화를 항상 고민해자.. 
"""

# 시간 초과 케이스
def solution():
    import sys
    
    # 테스트 케이스
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        # 학생의 수
        N = int(sys.stdin.readline().strip())
        edges = [[] for _ in range(N + 1)]
        array = list(map(int, sys.stdin.readline().strip().split(" ")))
        for i in range(len(array)):
            edges[i + 1].append(array[i])
        
        # 팀을 이루지 못한 학생의 수
        student = 0
        visited = [False] * (N + 1)
        
        def dfs(start, path):
            if not visited[i]:
                path.append(start)
                
                for next_node in edges[start]:
                    if next_node not in path:
                        path = dfs(next_node, path)
                    # 사이클 존재
                    if next_node == path[0]:
                        for x in path:
                            visited[x] = True
                            return path
                return path
        
        # 정점 iteration
        for i in range(1, N + 1):
            dfs(i, [])
            
        for i in range(1, N + 1):
            if not visited[i]:
                student += 1
        
        print(student)
        
"""
https://claude-u.tistory.com/435

코드를 잘 정리하여 최적화를 
"""        

import sys
sys.setrecursionlimit(111111) # 재귀 오류 예방

def dfs(x):
    global result
    # 노드 방문 처리
    visited[x] = True
    cycle.append(x) # 사이클을 이루는 팀을 확인하기 위함
    number = numbers[x]
    
    if visited[number]: # 방문가능한 곳이 끝났는지
        if number in cycle: # 사이클 가능 여부
            result += cycle[cycle.index(number):] # 사이클 되는 구간부터만 팀을 이룸
        return
    else: # 방문이 끝나지 않았다면 dfs
        dfs(number)

for _ in range(int(sys.stdin.readline().strip())):
    N = int(sys.stdin.readline().strip())
    numbers = [0] + list(map(int, sys.stdin.readline().strip().split())) # 간선
    visited = [True] + [False] * N # 방문 여부
    result = []
    
    # 모든 노드 iteration
    for i in range(1, N + 1):
        # 방문하지 않았다면
        if not visited[i]:
            cycle = []
            dfs(i) # DFS 함수 호출
            
    print(N - len(result)) # 팀에 없는 사람 수