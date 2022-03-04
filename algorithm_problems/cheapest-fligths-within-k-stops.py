import collections
import heapq

# 사이클이 존재하여 이 방법으로는 풀이 불가능
def findCheapestPrice(n, flights, src, dst, K):
    graph = collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    for u, v, w in flights:
        graph[u].append((v, w))

    # 큐 변수: [(가격, 정점, 남은 가능 경유지의 수)]
    Q = [(0, src, K)]

    # 우선순위 큐 최솟값을 기준으로 도착점까지 최소 비용 판별
    while Q:
        price, node, k = heapq.heappop(Q)
        # 현재 나온 노드가 목적지와 같으면 리턴
        if node == dst:
            return price
        # k >= 0보다 크다면 heapq에 넣기
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k - 1))

    return -1

def findCheapestPrice(n, flights, src, dst, K):
    graph = collections.defaultdict(list)
    # 그래프의 인접 리스트 구성
    for u, v, w in flights:
        graph[u].append([v, w])
    k = 0
    # 방문처리 확인
    visit = {}
    # 큐 변수: [(가격, 정점, 남은 가능 경유지의 수)]
    Q = [(0, src, 0)]

    # 우선순위 큐 최솟값을 기준으로 도착점까지 최소 비용 판별
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        # 노드를 아직 방문하지 않았거나
        # 해당 노드를 방문하기 이전에 경유지가 더 적다면
        if node not in visit or visit[node] > k:
            # 방문처리
            visit[node] = k
            for v, w in graph[node]:
                if k <= K:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k + 1))
    return -1


n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1

# n = 13
# flights = [[11,12,74],[1,8,91],[4,6,13],[7,6,39],[5,12,8],[0,12,54],[8,4,32],[0,11,4],[4,0,91],[11,7,64],[6,3,88],[8,5,80],[11,10,91],[10,0,60],[8,7,92],[12,6,78],[6,2,8],[4,3,54],[3,11,76],[3,12,23],[11,6,79],[6,12,36],[2,11,100],[2,5,49],[7,0,17],[5,8,95],[3,9,98],[8,10,61],[2,12,38],[5,7,58],[9,4,37],[8,6,79],[9,0,1],[2,3,12],[7,10,7],[12,10,52],[7,2,68],[12,2,100],[6,9,53],[7,4,90],[0,5,43],[11,2,52],[11,8,50],[12,4,38],[7,9,94],[2,7,38],[3,7,88],[9,12,20],[12,0,26],[10,5,38],[12,8,50],[0,2,77],[11,0,13],[9,10,76],[2,6,67],[5,6,34],[9,7,62],[5,3,67]]
# src = 10
# dst = 1
# k = 10
print(findCheapestPrice(n, flights, src, dst, k))

