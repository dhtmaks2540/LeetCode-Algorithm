"""
해당 문제는 다이나믹 프로그래밍으로 풀이하였다.

그 이유는 우선 1 ~ 5번째까지의 값은 (1,1,1,2,2)에 해당하고 6번째 값부터는
현재 값의 n - 5의 값과 현재 값의 n - 1의 값이 더해지는 형태로 나오게 된다.

예를 들어서 A(9) -> 7 = A(8) -> 5 + A(4) -> 2에 해당하고
A(10) -> 9 = A(9) -> 7 + A(5) -> 2에 해당한다.
따라서 중복되는 값이 발생하므로 이를 기록하기 위해서 다이나믹 프로그래밍으로 풀이하며
점화식은 An = A(n-5) + A(n-1) (A >= 6)이다.

"""

import sys

# 테스트 케이스
T = int(input())
array = []
for _ in range(T):
    array.append(int(sys.stdin.readline()))
# 미리 기록된 값
nums = [1, 1, 1, 2, 2]
    
# 다이나믹 프로그래밍 풀이를 위한 테이블
dp = [0] * (101)
# 첫 번째 값부터 다섯 번째 값 넣기
for i in range(len(nums)):
    dp[i + 1] = nums[i]
    
# 그 이후의 점화식은 An = A(n-5) + A(n-1)에 해당
# 보텀업으로 접근
for i in range(6, 101):
    dp[i] = dp[i - 5] + dp[i - 1]
    
for num in array:
    print(dp[num])