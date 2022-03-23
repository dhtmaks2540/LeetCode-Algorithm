"""
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

DFS와 백트래킹을 사용하여 문제 풀이
재귀구조를 통해 numbers를 iterate하며 DFS를 호출하다가
현재 값들이 저장된 리스트의 길이가 문제의 목표와 같다면 리턴하는 방식으로 백트래킹 조건을 사용
"""

N, M = map(int, input().split())

numbers = [i for i in range(1, N + 1)]

result = []

def dfs(temp):
    # 문자열의 길이가 목표와 같다면
    if len(temp) == M:
        # 결과 변수에 추가
        result.append(temp[:])
        return
    
    # 숫자를 iterate하며
    for i in range(0, N):
        # 현재 숫자가 리스트에 없다면
        if numbers[i] not in temp:
            temp.append(numbers[i])
            dfs(temp)
            temp.pop()
        
dfs([])

for data in result:
    for value in data:
        print(value, end = " ")
    print()