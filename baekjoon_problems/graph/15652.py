"""
DFS를 사용하여 문제 풀이

"""

N, M = map(int, input().split())
# 숫자를 나타내는 리스트
numbers = [i for i in range(1, N + 1)]

answer = []

def dfs(temp):
    # 현재 리스트에 저장된 값들의 길이가 목표값과 같다면
    if len(temp) == M:
        answer.append(temp[:])
        return

    for i in range(N):
        # 리스트에 값이 있을 경우
        if temp:
            # 마지막에 저장된 값보다 현재의 값이 크거나 같다면
            if temp[-1] <= numbers[i]:
                # DFS
                temp.append(numbers[i])
                dfs(temp)
                temp.pop()
        # 없을 경우 추가 후 DFS
        else:
            temp.append(numbers[i])
            dfs(temp)
            temp.pop()

dfs([])
for x in answer:
    for value in x:
        print(value, end=" ")
    print()