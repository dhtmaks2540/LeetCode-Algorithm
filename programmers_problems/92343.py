"""
처음에는 DFS를 사용해 풀이하려고 했는데 이미 방문한 노드를 다시 방문해야 한다는 생각이 떠올라서
visited 처리를 어떻게 해야할지 고민하다가, 방문처리를 처리하지 못할것 같아서 다른 방법을
고안하던 중 우선순위큐를 사용하면 풀릴 것 같아서 코드를 짜다가 풀이하지 못했다 ㅠ...
현재 문제에서 노드는 최대 17개로 완전 탐색을 수행해서 풀이할 수 있다. 따라서 DFS를 사용하여서 
탐색하는데 방문처리부분을 유심히 살펴보아야 할듯하다.

가장 중요한 것은 부모 노드에 연결된 다른 길로 어떻게 다시 돌아갈지를 생각해야 하는 것이다.
이를 현재 문제에서는 can_go 라는 변수를 사용해서 부모 노드에서 현재 노드와 연결된 자식 노드를 
추가하고, can_go를 순회하면서 현재 노드를 제외한 다른 노드들을 다시 방문하도록 처리하는 것이다.
이는 can_go.extend()와 can_go를 순회하는 부분의 아래코드에 해당한다.

https://kimjingo.tistory.com/154
"""

from copy import deepcopy

max_sheep = 0

def solution(info, edges):
    global max_sheep
    graph = [[] for _ in range(len(info))]
    # 방문처리를 확인하기 위한 리스트
    visited = [False] * len(info)
    # 간선 연결
    for from_node, to_node in edges:
        graph[from_node].append(to_node)
    
    # DFS 코드
    def find_max_recursive(current_node, visited, cnt_sheep, cnt_wolf, can_go):
        global max_sheep
        
        # 이미 방문했다면 return
        if visited[current_node]: return
        # 방문 처리
        visited[current_node] = True
        
        # 늑대인 경우
        if info[current_node]:
            cnt_wolf += 1
        # 양인 경우
        else:
            # 양의 수 증가 후, 최댓값 갱신
            cnt_sheep += 1
            max_sheep = max(max_sheep, cnt_sheep)
            
        # 늑대 수가 양의 수와 같거나 많은 경우 return
        if cnt_wolf >= cnt_sheep: return
        
        # 현재 노드와 연결된 노드를 추가
        # print(f"Current_node : {current_node}, Before : {can_go}, Sheep : {cnt_sheep}, Wolf : {cnt_wolf}", end=" -> ")
        can_go.extend(graph[current_node])
        # print(f"After : {can_go}")
        
        for next_node in can_go:
            # 큐에 저장된 노드에서 하나를 가져와 재귀함수 요청
            # 이 때 다음 큐에는 현재 노드를 제외한 리스트로 재구성하여 재귀함수 요청
            find_max_recursive(next_node, deepcopy(visited), cnt_sheep, cnt_wolf, \
                can_go = [loc for loc in can_go if loc != next_node and not visited[next_node]])
            
    find_max_recursive(0, visited, 0, 0, [])
    
    return max_sheep

"""
https://kimjingo.tistory.com/154

"""

info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
result = solution(info, edges)
print(result)