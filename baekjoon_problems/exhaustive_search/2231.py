"""
가장 작은 생성자를 찾아라

가장 작은 생성자를 찾기 위해서는 1부터 주어진 값까지 순회하면서 현재 값의 분해합을 만든 후
목표값과 같은지 비교하는 방식으로 풀이했다. 즉, 브루트 포스를 사용해 모든 경우의 수를 탐색하는
방법으로 풀이하였다.

"""

N = int(input())

for value in range(1, N):
    sum_value = value
    for chr in str(value):
        sum_value += int(chr)
    
    if sum_value == N:
        print(value)
        exit()
        
print(0)