"""
규칙을 유추한 뒤에 별을 찍어라

규칙을 제대로 파악하지 못해서 재귀적이든 분할정복이든 코드로 녹여내지 못했다.. 이런 문제에서
핵심은 우선 규칙을 파악한 후 이를 재귀적이던 분할정복이던 코드로 구현해내는 것이 중요한것같다.
코드 구현도 포기하지말고 고민하고 또 고민해보자! 특히 초기 좌표와 어떻게 좌표를 설정할지를 잘
생각해보자

https://hongcoding.tistory.com/90

맨 처음 n=3 일때의 그래프를 양옆으로 계속해서 복사해 나가는 방식으로 풀이할 수 있다.
6인 경우는 3의 그래프가 양옆으로 복사되고 12인 경우는 6의 그래프가 양옆으로 복사되는 과정이
계속해서 반복된다. 따라서 n=3 일 때의 모양을 바탕으로(가장 작은 크기로 분할), 다음 모양부터는
좌표만을 계산하여 재귀적으로 풀이할 수 있다.
"""

def solution1():
    n = int(input())
    
    graph = [[" "] * (2 * n) for _ in range(n)]
    
    def recursive(x, y, N):
        # 정복(가장 작은 단위인 n = 3 까지 분할이 완료됨)
        if N == 3:
            graph[x][y] = '*'
            graph[x + 1][y - 1] = graph[x + 1][y + 1] = '*'
            for i in range(-2, 3):
                graph[x + 2][y + i] = '*'
            return
        
        # 분할
        nextN = N // 2
        # 위 중간
        recursive(x, y, nextN)
        # 왼쪽 아래
        recursive(x + nextN, y - nextN, nextN)
        # 오른쪽 아래
        recursive(x + nextN, y + nextN, nextN)
         
    recursive(0, n - 1, n)
    
    for x in graph:
        print("".join(x))
        
solution1()