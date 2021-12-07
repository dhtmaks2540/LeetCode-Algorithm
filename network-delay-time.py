import heapq
import sys
import collections

def networkDelayTime(times, n, k):
    graph = [[] for _ in range(n + 1)]

    for time in times:
        # 출발지, 도착지,소요 시간
        x, y, z = time
        # 우선순위 큐에 사용하기 위해서 소요시간을 먼저 넣기
        graph[x].append((z, y))

    # 거리
    INF = sys.maxsize

    distance = [INF] * (n + 1)

    # 다익스트라 최단 거리 알고리즘
    def dijkstra(start):
        q = []

        # 시작지점 넣기
        heapq.heappush(q, start)
        # 시작지점 거리 초기화(자기 자신까지의 거리이므로 0)
        distance[start] = 0

        # 큐가 비어있지 않는 동안에
        while q:
            now = heapq.heappop(q)
            cost = distance[now]
            
            # 연결된 노드 확인
            for i in graph[now]:
                # 거리가 더 작다면
                if distance[i[1]] > cost + i[0]:
                    # 갱신하기
                    distance[i[1]] = cost + i[0]
                    heapq.heappush(q, i[1])

    dijkstra(k)

    if INF in distance[1:]:
        return -1
    else:
        return max(distance[1:])


def networkDelayTime(times, n, k):
    graph = collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    for u, v, w in times:
        graph[u].append((v,w))

    # 큐 변수: [(소요 시간, 정점)]
    Q = [(0, k)]
    dist = collections.defaultdict(int)

    # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))
    
    # 모든 노드의 최단 경로 존재 여부 판별
    if len(dist) == n:
        return max(dist.values())
    return -1

times = [[1,2,1]]
n = 2
k = 2

print(networkDelayTime(times, n, k))