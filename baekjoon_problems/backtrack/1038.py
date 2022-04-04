"""
음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 가장 작은 자릿수까지 감소한다면 그 수를 감소하는
수라고 한다. 이때, N이 주어질 경우 N번째 감소하는 수를 출력하라.

https://khsung0.tistory.com/22
"""

# 시간초과
def brute_force():
    # 브루트 포스로 풀이
    # N 번째
    N = int(input())

    if N <= 9:
        print(N)
        exit()

    # 결과변수
    N -= 9
    prev = 0

    for i in range(10, 9876543210 + 1):
        value = str(i)
        flag = True
        for j in range(1, len(value)):
            if value[j] >= value[j - 1]:
                flag = False
                break

        if flag:
            N -= 1

        if N == 0:
            print(i)
            exit()


# backtracking을 사용하여 문제 풀이
def solution():
    def add_digit(digit, num): # 자릿수에 따라 증가
        # 탈출 조건
        if digit == 1:
            decreasing.append(num)
        else:
            for i in range(num % 10):
                # digit 감소 후 재귀 호출
                add_digit(digit - 1, num * 10 + i)
                
    def backtracking(digit): # 백트래킹 시작
        for i in range(digit - 1, 10):
            add_digit(digit, i)
            
    decreasing = [] # 감소하는 숫자 리스트
    for i in range(1, 11):
        backtracking(i)
        
    n = int(input())
    if n >= len(decreasing): # 감소하는 숫자가 없을 때
        print(-1)
    else:
        print(decreasing[n])
        
solution()