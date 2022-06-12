"""
모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 구하라

https://st-lab.tistory.com/138

없애야 하는 전깃줄의 최소 개수를 구하자면 하나하나 전깃줄의 교차 여부를 판단해야 하므로
코드가 지저분해지며 시간복잡도는 좋지 못할것이다. 따라서 다른 관점에서 문제를 바라보아야 하는데
없애야 하는 전깃줄의 최소 개수는 설치할 수 있는 전깃줄의 최대 개수를 파악해서 원래의 전깃줄에서
이 값을 빼면 없애야 하는 전깃줄의 최소 개수가 된다. 즉 (전체 전선 개수 - 설치 가능 개수) = 철거 개수
가 되는 것이다.

먼저 A 전봇대를 기준으로 i번째에 연결된 전깃줄을 잇고 이후 전선들을 탐색하면서 i번째가 연결된 B의 값보다
큰 경우들을 모두 탐색해 보는 것이다. 이는 결국 정렬된 A를 기준으로 B에 연결된 값들에서 LIS를 수행하면 되는
것이다. LIS는 다이나믹 프로그래밍 또는 이분 탐색을 통해서 풀이할 수 있는데, 이 문제에서 주어진
조건의 최댓값을 100이므로 O(N^2)에 해당하는 다이나믹 프로그래밍을 통해서 풀이할 수 있다.

DP를 통해서 LIS를 수행하는 방법은 간단하다. 우선 중복되는 값을 기록하기 위해서 리스트를 선언하고,
현재 값보다 이전 값들을 탐색하며 현재 값보다 이전 값이 더 작다면 현재까지의 길이의 값과 이전
값에서 1을 추가한 길이의 값 중 최댓값을 기록하는 방식으로 풀이하면 된다.
"""

# 보텀업 방식으로 풀이
def solution1():
    import sys

    # 전깃줄의 개수
    n = int(sys.stdin.readline().strip())
    # 연결되는 번호
    array = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().strip().split(" "))
        array.append((x, y))

    # 정렬 수행
    array.sort()

    # DP 테이블
    dp = [0] * n

    for i in range(n):
        dp[i] = 1
        # 현재 값 이전까지 확인하며
        for j in range(i):
            # 현재 값보다 더 짧은 값이 있다면 -> 증가하는 부분이라면
            if array[i][1] > array[j][1]:
                # 최댓값 갱신
                dp[i] = max(dp[i], dp[j] + 1)

    # 최대로 설치할 수 있는 개수를 파악했으므로 주어진 전선에서 이 값을 빼 최소로 철거하는 전선을 출력            
    print(n - max(dp))
    
# 탑다운 방식으로 풀이
def solution2():
    import sys

    # 전깃줄의 개수
    n = int(sys.stdin.readline().strip())
    # 연결되는 번호
    array = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().strip().split(" "))
        array.append((x, y))

    # 정렬 수행
    array.sort()
    
    # DP 테이블
    dp = [0] * n

    # 탑다운 함수
    def recursive(n):
        # 현재 탐색을 수행하지 않았다면
        if dp[n] == 0:
            # 자기 자신으로 초기화
            dp[n] = 1
            
            # N 번째 이후의 전봇대들 비교
            for i in range(n + 1, len(dp)):
                """
                A전봇대의 N번째 전선이 연결되어있는 B전봇대보다 A의 i번째
                전봇대의 전선이 이어진 B전봇대가 뒤에 있을 경우
                전선을 설치할 수 있음
                """
                if array[n][1] < array[i][1]:
                    # 연결 가능한 전선의 경우의 수 중 큰 값을 dp에 저장
                    dp[n] = max(dp[n], recursive(i) + 1)
                    
        return dp[n]
    
    max_value = -sys.maxsize
    
    for i in range(n):     
        max_value = max(max_value, recursive(i))
    
    print(n - max_value)
    
solution2()