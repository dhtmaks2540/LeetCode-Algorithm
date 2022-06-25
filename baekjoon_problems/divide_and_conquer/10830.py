"""
크기가 M * N인 행렬 A가 주어지면 A의 B제곱을 구하는 프로그램을 구하라

행렬 A의 최대 크기는 5이고 제곱근은 최대 100,000,000,000 이다. 따라서 이를 직접 제곱하여서는 문제를
절대 풀이할 수 없다. 이를 풀이하기 위해서는 행렬의 거듭제곱을 사용할 수 있다. 행렬의 거듭제곱은
A * A = A^2으로 이 공식이 성립하기 위해서는 앞에 있는 행렬의 열의 개수와 뒤에 있는 행렬의 
행의 개수가 같아야 한다. 즉, 정사각 행렬에서만 이를 사용할 수 있다는 뜻인데, 현재 문제는 정사각행렬
이므로 행렬의 거듭제곱을 사용할 수 있는 것이다.

이제 이를 사용해서 문제를 풀이해보자. 예를 들어, A^10 이 나온다고 치면 이는 A^5 * A^5이 되고
이는 (A^5)^2이 되므로 A^5 한번만 구하면 된다. 또한 A^5은 홀 수 이기에 A^2 * A^2 * A가 되고 여기서는
(A^2)^2 * A가 되므로 A^2 한번만 구하면 된다. 이렇게 되면 O(logB)가 되므로 문제를 시간 제한안에
풀이할 수 있게 되는 것이다.

해당 문제는 분할 정복을 사용할 수 있는지 묻는 문제이다. 우선 위에서 말했듯이 범위가 굉장히 크기에
직접 계산을 하려고 하면 절대 시간안에 풀이할 수 없다. 따라서 새로운 접근방법을 떠올려야 하는데
수학적인 방법으로 접근을 하면 거듭제곱을 사용하여 나눌 수 있기에 이를 사용하여 가장 작은 크기까지
분할한 후 거듭제곱을 계산해주면서 정복해나가서 풀이할 수 있다. 큰 범위의 값이 주어지고
수학적인 접근법을 떠올려야 하는 경우 분할 정복을 생각하면 좋을 듯 하다.
"""

import sys

# 행렬의 크기
N, B = map(int, sys.stdin.readline().strip().split(" "))
# 행렬
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split(" "))))
    
def pow(now_graph, exponent):
    # 지수가 1일 경우 나머지 처리 후 그래프 그대로 반환(최소 크기)
    if exponent == 1:
        for i in range(N):
            for j in range(N):
                graph[i][j] %= 1000
                
        return graph
    
    # 분할(지수 법칙 사용)
    temp_graph = pow(now_graph, exponent // 2)
    even_new_graph = [[0] * N for _ in range(N)]
    
    # 행렬의 제곱 계산 -> 정복 및 병합
    for i in range(N):
        for j in range(N):
            now_value = 0
            for k in range(N):
                now_value += temp_graph[i][k] * temp_graph[k][j]
            even_new_graph[i][j] = now_value % 1000
    
    # 홀수라면 graph를 한번 더 곱해주기 -> 정복 및 병합
    # Ex) A^3 -> A^2 * A
    if exponent % 2 == 1:
        ord_new_graph = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                now_value = 0
                for k in range(N):
                    now_value += even_new_graph[i][k] * graph[k][j]
                ord_new_graph[i][j] = now_value % 1000
                
        return ord_new_graph
    
    # 그 외의 경우는 짝수이므로 그대로 리턴
    return even_new_graph

result_graph = pow(graph, B)
for values in result_graph:
    for value in values:
        print(value, end=" ")
    print()