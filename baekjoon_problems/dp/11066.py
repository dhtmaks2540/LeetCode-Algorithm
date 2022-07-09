"""
파일들을 하나로 파일로 합칠 때 필요한 최소비용을 계산하라

현재 문제는 우선 최적 부분 구조에 해당한다. 문제에서 예시로 준 40, 30, 30, 50 파일의 최종 합은
(40 + 30) + (30 + 50)으로 현재의 답이 부분 문제의 답으로 이루어지기 때문이다. 그리고 여기서 또한
중복이 발생하게 되는데 위의 4개가 아닌 여러 개의 답이 온다면 이전에 사용된 값이 새롭게 나오는
파일의 답으로 구성되기 때문에 하위 문제의 중복이 발생하게 되는 것이다. 따라서 DP를 풀이법으로 떠올릴
수 있는데 단지 최소의 값으로 만들기 위해서 어떤 규칙이 있나 찾아보기만하고 직접 구해볼 생각을
안했다... 이런 문제가 나오면 테스트 케이스는 우선 무시하고 직접 구해보는 방식으로 코드를 작성한 후,
시간 제한안에 풀이가 가능하면 그대로 가져가고 풀이가 불가능하다면 거기서부터 규칙을 찾아도 상관없을 듯 하다.

https://js1jj2sk3.tistory.com/3
https://cocoon1787.tistory.com/317
"""


import sys

# 테스트 케이스
T = int(sys.stdin.readline().strip())
MAX_NUM = 501

while T:
    # 소설을 구성하는 장의 수
    K = int(sys.stdin.readline().strip())
    sum_array = [0] * (K + 1)
    # i번째 장부터 j번째 장까지 합치는데 드는 최소 비용
    dp = [[0] * (K + 1) for _ in range(K + 1)]
    
    array = list(map(int, sys.stdin.readline().strip().split(" ")))
    
    # 구간합 계산
    for i in range(1, K + 1):
        sum_array[i] = sum_array[i - 1] + array[i - 1]
    
    # 구해야 하는 범위의 크기 
    for divide in range(1, K):
        # 합치는 범위의 시작 부분
        for tx in range(1, K - divide + 1):
            ty = tx + divide
            dp[tx][ty] = sys.maxsize
            # 구해야 하는 범위를 두 부분으로 나누는 기준점
            for mid in range(tx, ty):
                dp[tx][ty] = min(dp[tx][ty], dp[tx][mid] + dp[mid + 1][ty] + sum_array[ty] - sum_array[tx - 1])
        
    print(dp[1][-1])
    T -= 1