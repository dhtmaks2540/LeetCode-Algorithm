"""
N이 주어졌을 때, N * N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 방법의 수

https://cryptosalamander.tistory.com/58
https://chanhuiseok.github.io/posts/baek-1/

백트래킹을 사용해 푸는 문제임은 파악했지만 백트래킹의 조건을 구현해내지 못함..
퀸을 놓았다면 퀸이 놓인 자리의 행, 열, 대각선은 못 놓는다는 조건을 구현을 못함
"""

N = int(input())
# 같은 행에는 못놓기에 1차원 리스트를 사용해서 풀이 가능
row = [0] * N
answer = 0

# 해당 위치에 퀸을 놓을 수 있는지
# 즉, 유망한지 판단하는 함수(백트래킹 조건 함수)
def is_promising(x):
    for i in range(x):
        # 같은 열이면 안되고, 대각선상에 있어서도 안 된다.
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i): # 행 - 행 == 열 - 열이라면 대각선상에 존재
            return False

    return True

# nqueen 알고리즘
def n_queens(x):
    global answer

    # x가 마지막 행까지 수행하여 여기까지 도달한다면 찾기 완료
    if x == N:
        answer += 1
        return

    for i in range(N):
        # [x, i]에 퀸을 놓는다
        # x번째 행, i번째 열에 queen을 놓는다.
        row[x] = i
        # 이후 그 행에 둔 것에 대한 유망성을 판단
        if is_promising(x): # 해당 자리에 두어도 괜찮다면
            n_queens(x + 1) # 그 다음 행에 대해 퀸을 놓기

n_queens(0)
print(answer)