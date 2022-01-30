from tkinter import W
from typing import List
import collections

class Solution:
    """
    https://leetcode.com/problems/time-needed-to-inform-all-employees/discuss/532560/JavaC%2B%2BPython-DFS
    """

    """
    문제 어떻게 접근하려고 함?
    1. m-ary 트리를 생성하려고 함 -> 인접 리스트를 구성해서 풀이
    2. BFS로 접근 -> DFS, BFS 모두 접근 가능
    3. 그때 시간을 체크하여 총 걸린 시간을 반환하려고 함 -> 가장 깊은 리프노드에게 알리는 시간을 반환
    """

    # Top down DFS
    # dfs는 각 직원에게 필요한 시간을 찾는다.
    # manager를 위한 시간은 max(해당 manager의 직원들) + informTime[manager]
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # 인접 리스트
        children = [[] for _ in range(n)]

        for i, m in enumerate(manager):
            # head(루트노드)가 아니면
            # 해당 매니저에 자식 노드 추가
            if m >= 0: children[m].append(i)

        def dfs(i):
            # 현재 노드의 각 직원들 시간의 max값 + informTime[현재 노드]
            # max값을 리턴하는 이유는 가장 깊은 루트 노드에게 알리는 시간이 모든 정보를 보내는데 걸리는 시간이기에
            return max([dfs(j) for j in children[i]] or [0]) + informTime[i]

        return dfs(headID)


    # Bottom Up DFS
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(i):
            # 해당 노드가 head가 아니라면
            if manager[i] != -1:
                # informTime에 해당 노드의 매니저를 dfs한 값을 더하기
                informTime[i] += dfs(manager[i])
                manager[i] = -1
            return informTime[i]

        # n의 범위 만큼 dfs를 호출한 최대값 반환
        return max(map(dfs, range(n)))

    """
    https://leetcode.com/problems/time-needed-to-inform-all-employees/discuss/533109/JavaPython-BFSDFS-Solutions-Clean-code
    """
    # BFS
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # 인접 리스트
        graph = [[] for _ in range(n)]

        for i, m in enumerate(manager):
            # 헤드가 아니라면, 해당 매니저에게 자식 노드 넣기
            if m != -1: graph[m].append(i)

        # 큐 생성(루트 노드와 거리)
        queue = collections.deque([(headID, 0)])
        ans = 0
        
        while queue:
            # 현재 노드, 거리
            u, w = queue.popleft()
            # max값 갱신
            ans = max(ans, w)
            # 현재 노드에 연결된 노드 확인(부모 노드와 자식 노드)
            for v in graph[u]:
                # 연결된 노드, 거리 + informTime[현재 노드]
                queue.append((v, w + informTime[u]))
        
        return ans
        
n = 4
headID = 2
manager = [2,0,-1,1]
informTime = [1,1,1,0]
solution = Solution()
print(solution.numOfMinutes(n, headID, manager, informTime))