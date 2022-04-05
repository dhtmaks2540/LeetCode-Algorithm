"""
백준이가 얻을 수 있는 최대 수익을 구하라

해당 날짜에서 상담을 통해 얻을 수 있는 최대 수익은 현재 날짜를 상담한 후 그 이후에
상담 가능한 날짜들 중 최댓값을 얻어오는 방식으로 풀이하면 된다. 따라서 하위값을 기록하기 위해서
다이나믹 프로그래밍으로 접근할 수 있다.

해당 문제는 뒤쪽부터 순회하며 접근하는데 매 상담에 대하여 '현재 상담 일자의 이윤(p[i]) + 현재 상담을 마친 
일자부터의 최대 이윤(dp[t[i] + i]')을 계산하면 된다. 이후에 계산된 각각의 값 중에서 최댓값을 출력하면 된다.
따라서 dp[i] = i 번째 날부터 마지막 날까지 낼 수 있는 최대 이익이라고 하면 점화식은
dp[i] = max(p[i] + dp[t[i] + i], max_value)가 된다. 이때 max_value는 뒤에서부터 계산해오면서 
현재까지의 최대 상담 금액에 해당하는 변수이다.
"""

import sys

# 시간복잡도는 O(2N..?)
def solution():
    # 전체 상담 개수
    N = int(input())
    # 상담을 완료하는데 걸리는 기간
    t = []
    # 상담을 완료했을 때 받을 수 있는 금액
    p = []
    for _ in range(N):
        # 상담에 걸리는 시간, 금액
        x, y = map(int, sys.stdin.readline().split())
        t.append(x)
        p.append(y)
    # 최대 금액을 기록하기 위한 변수
    max_value = 0
        
    # DP 테이블
    dp = [0] * (N + 1)

    # 뒤에서부터 순회하며
    for i in range(N - 1, -1, -1):
        # 날짜 계산(현재 날짜 + 상담에 걸리는 시간)
        time = i + t[i]
        
        # 상담이 기간 안에 끝나는 경우
        if time <= N:
            # 점화식에 맞게, 현재까지의 최고 이익 계산
            dp[i] = max(p[i] + dp[time], max_value)
            # 최댓값 갱신
            max_value = dp[i]
        # 상담이 범위를 벗어나는 경우
        else:
            dp[i] = max_value
            
    print(max_value) 
        
solution()

"""
앞에서부터 접근하는 풀이

https://yabmoons.tistory.com/337
"""