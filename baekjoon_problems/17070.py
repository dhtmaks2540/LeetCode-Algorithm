"""
파이프가 (1,1), (2,2)를 차지하고 있고 방향은 가로이다. 파이프의 한쪽 끝을 (N,N)으로 이동시키는
방법의 개수를 구하라

"""

# 집의 크기
N = int(input())
# 집의 상태(빈 칸은 0, 벽은 1)
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

