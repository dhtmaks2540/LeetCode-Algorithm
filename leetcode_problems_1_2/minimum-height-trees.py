import collections

class Solution:
    # n: 노드의 개수, edges: 간선
    def findMinHeightTrees(self, n, edges):
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
            # 방향이 없으므로 리프 노드는 자신을 연결한 부모 노드만
            # 가지고 있기에 1로 검사
            if len(graph[i]) == 1:
                leaves.append(i)

        # 루트 노드만 남을 때까지 반복 제거
        while n > 2:
            # 리프 노드의 개수를 빼기
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                # 리프노드에 연결된 노드
                neighbor = graph[leaf].pop()
                # 연결된 노드에서 리프노드 삭제
                graph[neighbor].remove(leaf)

                # 새롭게 리프 노드가 된 노드들을 추가
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves

n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
solution = Solution()
print(solution.findMinHeightTrees(n, edges))