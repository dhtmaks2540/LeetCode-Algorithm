"""
배열의 수들의 순서를 변경한 후 문제에서 주어진 식을 사용한 값중 최댓값을 출력하라

원소의 개수가 최대 8개이므로 완전탐색을 통해 풀이할 수 있다고 생각했다. 풀이 방법은
재귀구조로 배열을 탐색하면서 배열의 순서를 변경하고 모두 변경이 
되었다면(임시 배열에 추가된 원소의 개수가 문제에서 주어진 수의 개수가 되었다면) 값을 계산하고
최댓값을 갱신하는 방식으로 풀이했다. 재귀를 사용하므로 조건이 무조건 필요하므로 임시 리스트의
개수를 원래 리스트의 개수와 비교해서 같다면 반환하는 코드를 추가했다.

파이썬의 permutaions 라이브러리를 사용해도되지만 DFS(재귀)를 통해 직접 구현하였다.
"""

def solution1():
    import sys

    # 수의 개수
    N = int(sys.stdin.readline().strip())
    array = list(map(int, sys.stdin.readline().strip().split(" ")))
    max_value = -sys.maxsize

    def recursive(path=[]):
        global max_value
        
        if len(path) == N:
            sum_value = 0
            for i in range(1, N):
                sum_value += abs(array[path[i - 1]] - array[path[i]])
            max_value = max(max_value, sum_value)
            return
            
        for i in range(N):
            if i not in path:
                path.append(i)
                recursive(path)
                path.pop()
            
    recursive()
    print(max_value)
    
import sys

# 수의 개수
N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split(" ")))
max_value = -sys.maxsize

def recursive(visited, path):
    global max_value

    if len(path) == N:
        sum_value = 0
        for i in range(1, N):
            sum_value += abs(path[i - 1] - path[i])
        max_value = max(max_value, sum_value)
        return
        
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            recursive(visited, path + [array[i]])
            visited[i] = False

visited = [False] * N
recursive(visited, [])
print(max_value)