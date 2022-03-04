from typing import List
import collections


class Solution:
    # 위상 정렬을 활용
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 진입 차수
        indegree = [0] * numCourses

        graph = [[] for _ in range(numCourses)]

        # a강의를 듣기 위해 b 선 수강(b -> a)
        for a, b in prerequisites:
            graph[b].append(a)
            # 진입 차수 증가
            indegree[a] += 1

        # 결과변수
        result = []

        def topology_sort():
            q = collections.deque()

            # 진입 차수가 0인 노드 추가
            for i in range(numCourses):
                if indegree[i] == 0:
                    q.append(i)

            # 큐가 비어있지 않는 동안
            while q:
                now = q.popleft()
                result.append(now)

                # 연결된 노드 확인
                for i in graph[now]:
                    indegree[i] -= 1
                    # 새롭게 진입 차수가 0이된 노드 추가
                    if indegree[i] == 0:
                        q.append(i)

        # 위상 정렬 수행
        topology_sort()

        if len(result) == numCourses:
            return result
        else:
            return []

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
solution = Solution()
print(solution.findOrder(numCourses, prerequisites))