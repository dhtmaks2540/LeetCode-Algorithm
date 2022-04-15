"""
두 변을 공유하지 않는 스티커 점수의 최댓값을 출력하라

그래프에서 점수의 최댓값을 획득하는 문제로 2차원 모양의 광산의 그래프를 주면서 최대 금값을 계산하라는
문제와 비슷하며, 이전의 최댓값이 중복되며 사용되기에 DP로 문제를 풀고자함.

현재 행, 열, 현재 행열을 방문했는지 안했는지에 따른 최댓값을 기록하기 위한 3차원 테이블을 정의한 후
현재 위치를 방문했을 경우에 가능한 왼쪽의 값들의 최댓값과 현재 위치를 방문하지 않았을 경우 가능한
왼쪽의 값들의 최댓값을 기록하는 방식으로 풀이했다. 다만 시간이 굉장히 오래걸린것으로 보아 좋지 않은
풀이 방법인듯하다.

핵심은 가로는 N으로 변경되지만 세로는 2로 고정되어 있으니 고정된 2를 활용할 수 있다는 것이다. 따라서
첫째 줄의 첫째 칸에서 시작하여 얻을 수 있는 최대 점수와, 둘째 줄의 첫째 칸에서 시작하여 얻을 
수 있을 수 있는 최대 점수, 이렇게 2가지의 경우로 나누어서 접근할 수 있다.

문제를 보며 완전탐색이 힘든 경우와 중복되는 하위 문제가 발생하면 다이나믹 프로그래밍을 떠올리고,
어떻게 값을 저장할 지 여러가지 방면으로 생각하며 주어진 값을 잘 활용하도록 하자..
"""

import sys

def solution1():
    # 테스트 케이스
    T = int(input())

    for _ in range(T):
        # 열
        n = int(sys.stdin.readline())
        # 2차원 행렬
        array = []
        for _ in range(2):
            array.append(list(map(int, sys.stdin.readline().split(" "))))
        
        # 중복되는 값을 기록하기 위한 테이블
        dp = [[[0] * 2 for _ in range(n)] for _ in range(2)]
        dp[0][0][0] = array[0][0]
        dp[0][0][1] = array[1][0]
        dp[1][0][0] = array[1][0]
        dp[1][0][1] = array[0][0]
        
        # array 순회
        for i in range(1, n):
            for j in range(2):
                # 0은 현재 탐색
                # 1은 현재 탐색 X
                if j == 0:
                    dp[j][i][0] = array[j][i] + max(dp[j][i - 1][1], dp[j + 1][i - 1][0])
                    dp[j][i][1] = max(dp[j][i - 1][0], dp[j + 1][i - 1][1], dp[j + 1][i - 1][0])
                elif j == 1:
                    dp[j][i][0] = array[j][i] + max(dp[j][i - 1][1], dp[j - 1][i - 1][0], dp[j - 1][i - 1][0])
                    dp[j][i][1] = max(dp[j][i - 1][0], dp[j - 1][i - 1][1], dp[j - 1][i - 1][0])
                    
        max_value = 0

        for i in range(2):
            for j in range(2):
                max_value = max(max_value, dp[i][n - 1][j])
                
        print(max_value)
        
"""
https://m.blog.naver.com/occidere/220786307316

스티커 선택시 선택한 스티커의 상, 하, 좌, 우 에 위치한 스티커를 고르지 않으면서 얻을 수 있는
최대 점수를 구하는 것이 문제에서 요구하는 사항이다. 따라서 어떤 스티커를 시작점으로 할것인지를
먼저 선택해야 하고, 세로가 2로 고정되어 있기에 2를 활용한다. 따라서 첫째 줄의 첫째 칸에서
시작하여 얻을 수 있는 최대 점수와, 둘째 줄의 첫째 칸에서 시작하여 얻을 수 있는 최대 점수 2가지의
경우로 나누어서 접근한다.

따라서 DP로 활용할 최대값을 담아놓는 2차원 배열을 선언한다.
dp[2][100001]
"""
def solution():
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        n = int(sys.stdin.readline())
        array = []
        for _ in range(2):
            array.append(list(map(int, sys.stdin.readline().split(" "))))
        dp = [[0] * 100001 for _ in range(2)]
        # 0은 첫째 줄에서 시작하는 경우
        dp[0][1] = array[0][0]
        dp[1][1] = array[1][0]
        for i in range(2, n + 1):
            # 1칸 뒤 대각선과 2칸 뒤 대각선 중 최대값 판별
            dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + array[0][i - 1]
            dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + array[1][i - 1]
            
        print(max(dp[0][n], dp[1][n]))

solution()