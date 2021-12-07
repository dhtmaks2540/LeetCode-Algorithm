import collections

# BFS와 위상정렬을 이용한 풀이
def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]

    # 진입 차수
    indegree = [0] * numCourses

    # 코스 순서 쌍
    for a, b in prerequisites:
        graph[a].append(b)
        # 진입 차수 증가
        indegree[b] += 1

    q = collections.deque()

    # 진입 차수가 0인 노드(강의) 큐에 넣기
    for i in range(numCourses):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    # indegree가 0라는 것은 사이클이 발생하지 않았다는 뜻
    if sum(indegree) == 0:
        return True
    # 0가 아니라는 것은 사이클이 발생했다는 뜻
    else:
        return False

def canFinish(numCourses, prerequisites):
    graph = collections.defaultdict(list)
    # 그래프 구성
    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()

    def dfs(i):
        # 순환 구조이면 False
        if i in traced:
            return False

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)

        return True

    # 순환 구조 판별
    for x in list(graph):
        if not dfs(x):
            return False
    
    return True

def canFinish(numCourses, prerequisites):
    graph = collections.defaultdict(list)
    # 그래프 구성
    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()
    visited = set()

    def dfs(i):
        # 순환 구조이면 False
        if i in traced:
            return False
        # 이미 방문했던 노드이면 True
        if i in visited:
            return True
        
        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        
        # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)
        # 탐색 종료 후 방문 노드 추가
        visited.add(i)

        return True

    # 순환 구조 판별
    for x in list(graph):
        if not dfs(x):
            return False

    return True

numCourses = 5
prerequisites = [[1,0], [0,1]]

print(canFinish(numCourses, prerequisites))