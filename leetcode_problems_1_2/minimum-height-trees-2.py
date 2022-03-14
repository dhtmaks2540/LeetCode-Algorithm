from typing import List
import collections

class Solution:
    """
    최소 높이를 구성하려면 가장 가운데에 있는 값이 루트여야 한다
    -> 리프 노드를 하나씩 제거해 나가면서 남아 있는 값을 찾으면 이 값이 가장 가운데에 있는 값
    -> 이 값을 투르토 했을 때 최소 높이를 구성할 수 있다는 뜻.
    """

    """
    https://leetcode.com/problems/minimum-height-trees/discuss/76055/Share-some-thoughts
    """
    
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        # 양방향 그래프 구성
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 첫 번째 리프 노드 추가
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)

        # 루트 노드만 남을 때까지 반복 제거
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                # 리프 노드와 연결된 노드
                neighbor = graph[leaf].pop()
                # 연결된 노드에서 리프 노드 제거
                graph[neighbor].remove(leaf)

                # 새롭게 리프 노드가 된 노드 추가
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            
            leaves = new_leaves
        
        return leaves

    

n = 4
edges = [[1,0],[1,2],[1,3]]

n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
solution = Solution()
print(solution.findMinHeightTrees(n, edges))