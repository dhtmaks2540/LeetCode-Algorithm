"""
두 팀의 능력치 차이가 최소가 되도록 만들어라

https://st-lab.tistory.com/122

브루트 포스을 통해 투 팀의 능력치 차이를 계산하여 최솟값을 갱신하는 방식으로 풀이했다. 조합을
사용하는 방법으로 문제를 풀이하면 된다. 블로그와 같이 visited를 사용해서 조금 더 나은 
시간 복잡도를 가지도록 풀이할 수 있다. 다만 중요한 것은 DFS를 사용해서 조합을 구하며 브루트
포스를 하는 것이 문제의 핵심 포인트이다.
"""

# 브루트 포스
def solution1():
    import sys
    import itertools

    # 참가자 수
    N = int(sys.stdin.readline().strip())
    # 능력치 
    graph = []

    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().strip().split(" "))))
        
    min_diff = sys.maxsize

    # 스타트팀
    for start_team in list(itertools.combinations([i for i in range(1, N + 1)], N // 2)):
        link_team = []
        # 링크팀
        for i in range(1, N + 1):
            if i not in start_team:
                link_team.append(i)
        
        start_score = 0
        link_score = 0
        
        # 스타트팀 계산
        for x, y in list(itertools.combinations(start_team, 2)):
            start_score += graph[x - 1][y - 1]
            start_score += graph[y - 1][x - 1]
        
        # 링크팀 계산
        for x, y in list(itertools.combinations(link_team, 2)):
            link_score += graph[x - 1][y - 1]
            link_score += graph[y - 1][x - 1]
        
        # 두 팀의 능력치 차이 갱신
        min_diff = min(min_diff, abs(start_score - link_score))
        
    print(min_diff)