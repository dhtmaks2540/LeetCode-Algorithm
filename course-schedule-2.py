from typing import List
import collections

class Solution:
    # 위상 정렬 활용
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 모든 노드에 대한 진입차수는 0으로 초기화
        indegree = [0] * numCourses
        # 각 노드에 연결된 간선의 정보를 담기 위한 연결 리스트 초기화
        graph = [[] for _ in range(numCourses)]

        # 모든 간선의 정보 입력 받기
        # a를 완료하기 위해서 b를 선 수강해야함
        for a, b in prerequisites:
            # 정점 b에서 a로 이동 가능
            graph[b].append(a)
            # 진입차수 증가
            indegree[a] += 1

        # 위상 정렬 함수
        def topology_sort():
            q = collections.deque()

            # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
            for i in range(numCourses):
                if indegree[i] == 0:
                    q.append(i)

            # 큐가 빌 때까지 반복
            while q:
                # 큐에서 원소 꺼내기
                now = q.popleft()
                # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
                for i in graph[now]:
                    indegree[i] -= 1
                    # 진입차수가 0이 되면 큐에 추가
                    if indegree[i] == 0:
                        q.append(i)

        topology_sort()
        # 진입 차수가 0 -> 모두 수행
        if sum(indegree) == 0:
            return True
        # 진입 차수가 남아있다 -> 사이클이 발생한 경우
        else:
            return False

    # DFS를 이용하여 접근
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)

        # 중복 여부를 판별하기 위한 집합 자료
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

    # DFS 및 가지치기
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
    
numCourses = 2
prerequisites = [[1,0],[0,1]]
solution = Solution()
print(solution.canFinish(numCourses, prerequisites))