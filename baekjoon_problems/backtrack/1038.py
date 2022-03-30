"""
음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 가장 작은 자릿수까지 감소한다면 그 수를 감소하는
수라고 한다. 이때, N이 주어질 경우 N번째 감소하는 수를 출력하라.
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


N = int(input())
numbers = [0] * 10

# 예외처리
if N <= 9:
    print(N)
    exit()

N -= 9

def backtracking():
    pass