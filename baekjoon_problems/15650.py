"""
백트래킹을 사용하여 문제 풀이
"""

N, M = map(int, input().split())

numbers = [i for i in range(1, N + 1)]
result = []

def dfs(index, temp=[]):
    if len(temp) == M:
        result.append(temp[:])
        return
    
    for i in range(index, N):
        if numbers[i] not in temp:
            temp.append(numbers[i])
            dfs(i + 1, temp)
            temp.pop()
        
dfs(0)

for x in result:
    for value in x:
        print(value, end = " ")
    print()  