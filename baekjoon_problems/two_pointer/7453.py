"""
A, B, C, D 배열이 주어졌을 때 각 배열마다 원소를 한개씩 뽑아서 합이 0이 되는 쌍의 개수를 구하라

1208번 문제와 비슷하게 4개의 배열을 두개의 배열(left 배열, right 배열)로 나눈 후
left 배열을 우선 계산하고 map에 해당 값을 키로 넣은 후, right 배열을 계산하며 현재 값에 -1을 곱한 값이 
존재한다면 4개 배열의 원소의 합이 0이 된다는 의미이므로 그 때의 값을 결과 변수에 더해주는 방식으로
풀이했다. 즉, map을 사용하였는데 이 풀이법은 시간초과가 발생했다.. ㅠㅠ

https://velog.io/@ckstn0778/%EB%B0%B1%EC%A4%80-7453%EB%B2%88-%ED%95%A9%EC%9D%B4-0%EC%9D%B8-%EB%84%A4-%EC%A0%95%EC%88%98-X-1

정렬과 투 포인터를 사용하여 문제를 풀이할 수 있다. 우선 4개의 배열을 두 개의 배열끼리 나누는 것은
동일하게 처리한다. 그 후 첫 번째, 두 번째 배열을 leftArray, 세 번째, 네 번째 배열을 rightArray라고
칭하고 이 둘을 각각 오름차순으로 정렬한다. 그 후 투 포인터를 사용하는데 시작점은 0, 끝 점은 rightArray의
마지막 인덱스를 가리키도록 한다. 이제 이 둘의 합을 분기하는데 

1. 만약 그 합이 0이라고 한다면 문제의 조건에 해당하는 것이므로 이 값을 계산하는데 
단지 한 번만 더해주는 것이 아니라 leftArray와 rightArray에서 현재 0이 나오는 값과 같은 값을 
모두 더해서 최적화를 진행해준다.

2. 합이 0보다 크다고 하다면 끝 점을 줄여서 합이 더 작아지도록 한다.

3. 합이 0보다 작다고 하다면 시작점을 늘려서 합이 더 커지도록 한다.

이 세개의 분기점을 시작점이 배열의 길이보다 작거나 끝 점이 0보다 큰 동안에 수행하게 되면
문제에서 원하는 답을 출력할 수 있다.

이 문제를 만약 완전탐색을 수행했으면 최대 4000^3으로 문제를 풀이할 수 없었을 것이다. 따라서 최적화를
진행해야하는데 이와 같이 두 개의 배열로 나누고 투 포인터를 사용하는 방법 또는 이분 탐색을 사용하는 방법을
생각해봐야겠다.  
"""

# 시간 초과
def solution1():
    import sys
    import collections

    # 배열의 크기
    n = int(sys.stdin.readline().strip())
    A = [0] * n
    B = [0] * n
    C = [0] * n
    D = [0] * n

    for i in range(n):
        data = list(map(int, sys.stdin.readline().strip().split(" ")))
        A[i] = data[0]
        B[i] = data[1]
        C[i] = data[2]
        D[i] = data[3]
        
    subSum = collections.defaultdict(int)
    cnt = 0

    for i in range(n):
        for j in range(n):
            temp = A[i] + B[j]
            subSum[temp] += 1
            
    for i in range(n):
        for j in range(n):
            temp = C[i] + D[j]
            cnt += subSum[-temp]
            
    print(cnt)
    
# solution1()
    
def solution2():
    import sys
    
    n = int(sys.stdin.readline().strip())
    array = [list(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(n)]
    
    left_array = []
    right_array = []
    
    for i in range(n):
        for j in range(n):
            # 첫 번째와 두 번째 배열의 수열의 합
            left_array.append(array[i][0] + array[j][1])
            # 세 번째와 네 번째 배열의 수열의 합
            right_array.append(array[i][2] + array[j][3])
            
    # 정렬 수행(오름차순)
    left_array.sort()
    right_array.sort()
    
    # 시작점과 끝점
    i, j = 0, len(right_array) - 1
    answer = 0
    
    while i < len(left_array) and j >= 0:
        # 왼쪽 배열의 값과 오른쪽 배열의 값이 0이라면
        if left_array[i] + right_array[j] == 0:
            next_i, next_j = i + 1, j - 1
            # 왼쪽 배열의 값이 같은게 여러개라면
            while next_i < len(left_array) and left_array[i] == left_array[next_i]:
                next_i += 1
                
            # 오른쪽 배열의 값이 같은게 여러개라면
            while next_j >= 0 and right_array[j] == right_array[next_j]:
                next_j -= 1
                
            # 결과값에 개수 추가
            answer += (next_i - i) * (j - next_j)
            i, j = next_i, next_j
        # 오른쪽 배열의 값이 왼쪽 배열의 값보다 더 절대값이 큰 경우 -> 오른쪽 배열의 값을 줄이기
        elif left_array[i] + right_array[j] > 0:
            j -= 1
        # 왼쪽 배열의 값이 오른쪽 배열의 값보다 더 절대값이 큰 경우 -> 왼쪽 배열의 값을 늘리기
        else:
            i += 1
            
    print(answer)
    
solution2()