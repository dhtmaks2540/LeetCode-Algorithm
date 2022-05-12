"""
1,2,3을 가지고 정수 n을 만드는 방법의 수를 구하라

재귀함수를 사용해서 리스트에 저장된 값인 [1,2,3]을 가지고 target을 만드는 방식으로
문제를 풀이하였다. 인덱스를 통해서 현재 값을 더하고 재귀를 호출하고 다시 빼는 방식을 사용하면
순열을 만들 수 있으므로 이를 통해서 target이 만들어지는 경우의 수를 체크하면 된다. 다만
재귀함수이므로 종료 조건이 필수이기에 목표값을 넘어가면 반환, 목표값에 도달하면 경우의 수를 
1 추가하고 반환하는 방식으로 풀이했다.

다이나믹 프로그래밍으로도 풀이할 수 있다. 수를 1,2,3만 가지고 만드는 방법의 수를 출력하는 것이다.
우선 1, 2, 3을 만드는 방법은 각각 
dp[1] = 1, dp[2] = 2(1 + 1, 2), dp[3] = 4(1+1+1, 1+2, 2+1, 3)이 있다.
여기서 4를 만드는 방법은 
1에다가 3을 더하는 경우의 수 -> 즉, dp[3]
2에다가 2를 더하는 경우의 수 -> dp[2]
3에다가 1을 더하는 경우의 수 -> dp[1]을 합친 7이 된다.

이 점화식을 사용해서 5를 만드는 방법은
1에다가 4를 더하는 경우의 수 -> dp[4]
2에다가 3을 더하는 경우의 수 -> dp[3]
3에다가 1을 더하는 경우의 수 -> dp[2]를 합친 13이 된다.

따라서 계속해서 중복이 발생하며 문제의 최적의 해답이 부분 문제의 최적의 해답으로 구성되므로 다이나믹
프로그래밍을 통해 중복되는 하위 문제의 답을 기록하는 방식으로 풀이할 수 있다.
"""

def solution1():
    import sys

    # 테스트케이스
    T = int(sys.stdin.readline().strip())
    numbers = [1,2,3]

    def check(sum_value, target):
        global answer
        
        if sum_value > target:
            return
        
        if sum_value == target:
            answer += 1
            return
        
        for i in range(3):
            sum_value += numbers[i]
            check(sum_value, target)
            sum_value -= numbers[i]
            
    for _ in range(T):
        answer = 0
        target = int(sys.stdin.readline().strip())
        check(0, target)
        print(answer)
        
def solution2():
    import sys

    # 테스트케이스
    T = int(sys.stdin.readline().strip())
    # 다이나믹 테이블
    dp = [0] * (11)
    # 1을 만드는 경우의 수
    dp[1] = 1
    # 2를 만드는 경우의 수
    dp[2] = 2
    # 3을 만드는 경우의 수
    dp[3] = 4
    
    for i in range(4, 11):
        # 점화식
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    for _ in range(T):
        number = int(sys.stdin.readline().strip())
        print(dp[number])
        
solution2()