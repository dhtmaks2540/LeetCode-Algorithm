"""
스타트가 링크를 만나는데 필요한 에너지 양의 최솟값을 구하라

해당 문제는 현재 위치까지 순서에 맞춰서 최소의 에너지로 오는 값을 구하는 문제로
따라서 점화식은 dp[N] = 현재 위치로 이동할 수 있는 위치의 값 + 이동 에너지의 최솟값에 해당한다.
이 점화식은 최장 증가 부분 수열을 구하는 문제와 점화식이 비슷하다. 그 이유는
현재 위치로 이동할 수 있는지를 판단하기 위해서 현재 위치가 i라고 한다면 i-1 까지 순회하면서
현재 위치의 이전에 올 수 있는 값만을 가지고 점화식을 사용하여 dp 테이블을 갱신하기 때문이다.
"""

import sys

# 링크의 집
N = int(sys.stdin.readline())
# 보도블럭 글자
array = list(sys.stdin.readline())
# 현재 위치에서 에너지를 기록하기 위한 DP 테이블
dp = [sys.maxsize] * (N + 1)
dp[1] = 0

dic = {
    'B':'J',
    'O':'B',
    'J':'O'
}

# 집 iterate
for i in range(1, N + 1):
    # 현재 위치에서 이전의 위치에서 순서가 맞는 값이 있는지
    for j in range(i):
        # B <- O <- J <- B ....
        if dic[array[i - 1]] == array[j - 1]:
            # 현재 위치의 값 또는 이전의 위치에서 움직이는 비용을 더한 값중 최솟값
            dp[i] = min(dp[i], dp[j] + (j - i) * (j - i))

# 이동할 수 없다면
if dp[N] == sys.maxsize:
    print(-1)
else:
    print(dp[N])