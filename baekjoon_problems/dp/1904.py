"""
N이 주어졌을 때 만들 수 있는 모든 가짓수

N이 4로 주어졌을 때 만들 수 있는 가짓수는 
(0011, 0000, 1001, 1100, 1111)로 총 5가지인데 이는
N이 3으로 주어졌을 때 만들 수 있는 가짓수인
(111, 100, 001)에 1을 더한 가짓수와
N이 2로 주어졌을 때 만들 수 있는 가짓수인
(11, 00)에 00을 더한 가짓수의 합으로 이루어져있다. 

즉, 문제의 최적의 답이 부분 문제의 최적의 답으로
구성되므로 다이나믹 프로그래밍, 그리디 알고리즘, 분할 정복으로 문제를 접근할 수 있다.

추가로 또한 부분 문제(하위 문제)가 중복되서 나오기에 이를 기록하여 메모리의 사용량은 늘리지만
시간 복잡도는 줄이는 다이나믹 프로그래밍을 활용해서 문제를 풀 수 있다.

위에서 언급했듯이 N이 4로 주어졌을 때의 답은
N이 3으로 주어졌을 때 만들 수 있는 가짓수와 N이 2로 주어졌을 때 만들 수 있는 가짓수의 합이므로
점화식 dp[n] = dp[n - 1] + dp[n - 2]에 해당한다.

-----
참고!!

이 문제와 같이 "~로 나눈 나머지를 출력한다"는 문제는 거의 대부분 전체 답을 먼저 구하고 
마지막에 나머지 연산을 한 번 하라는 것이 아니라, 연산 과정에서 모듈로의 성질을 이용하여 수를 
계속 작게 유지할 수 있도록 배려를 해주는 것입니다. 
안 그러면 수가 너무 커져서 계산 시간도 오래 걸릴 뿐만 아니라 파이썬처럼 
bigint를 지원하지 않는 언어에서는 구현하는 것 자체가 매우 까다롭기 때문입니다.
"""

n = int(input())

# 3보다 작은 값은 똑같은 값의 경우의 수가 나오므로
if n <= 3:
    print(n)
    exit()

# 중복되는 하위 값을 기록하기 위한 테이블  
dp = [0] * (n + 1)
# N = 1일 경우 만들 수 있는 가짓수는 1(1)
dp[1] = 1
# N = 2일 경우 만들 수 있는 가짓수는 2(11,00)
dp[2] = 2
# N = 3일 경우 만들 수 있는 가짓수는 3(111, 100, 001)
dp[3] = 3

for i in range(4, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
    
print(dp[n])