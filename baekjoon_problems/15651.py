"""
DFS를 활용하여 문제 풀이

조건에 맞게 주어진 숫자들을 순열로 구성해야하는데 파이썬의 itertools의 permutation을 사용해도
되지만 DFS를 활용하여 리스트를 탐색하면서 조건으로 현재 값을 저장하고 있는 리스트의 길이가 목표값과
같은지를 비교하며 맞으면 돌아가는 방식으로 문제를 풀이한다.

"""

N, M = map(int, input().split())
# 1부터 N까지의 리스트
numbers = [i for i in range(1, N + 1)]

answer = []

def dfs(temp):
    # 리스트에 저장된 값의 길이가 목표값과 같다면
    if len(temp) == M:
        answer.append(temp[:])
        return

    # 숫자들을 iterate하며
    for i in range(N):
        # DFS 활용
        temp.append(numbers[i])
        dfs(temp)
        temp.pop()

dfs([])
for i in answer:
    for j in i:
        print(j, end=" ")
    print()