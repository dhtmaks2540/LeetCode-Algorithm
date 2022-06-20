"""
도난당한 학생들에게 여분의 체육복이 있는 학생들이 빌려줘서 최대한 많은 학생들이 체육복을 가지게
하는 방벙을 찾아라.

현재 문제는 우선 여분을 가지고 있는 사람중에 도난당한 사람을 처리하여 빌려줄 수 있는 사람들을
추스린 후, 빌려줄 수 있는 경우 앞에 사람이 없다면 앞에 사람을 먼저 빌려주고 후에 뒤에 사람을 빌려주는
방식으로 풀이하면 된다. 다만 빌려줄 수 있는 사람들에 대한 정렬을 수행한 후 문제를 풀이해야 하는데,
그 이유는 아래의 테스트케이스를 확인하면 된다.

n = 5
lost = [2,4]
reserve = [3,1]
result = 5

아래의 테스트 케이스에서 3번과 1번이 여분의 체육복을 가지고 있고, 2번과 4번이 체육복이 없을 경우
reserve를 정렬을 수행하지 않으면 3번이 앞에 사람인 2번을 빌려주고, 1번은 빌려줄 사람이 없기에 
4번은 체육복이 없는 상태로 끝난다. 하지만 정렬을 수행한 후 1번이 2번을 빌려주고, 3번이 4번을 빌려주면
체육복이 없는 사람이 아무도 없게 된다. 이처럼 자신이 먼저 체육복을 빌려주는 방향으로 정렬을
수행한 후 풀이하면 그리디 알고리즘의 선택 조건에 부합하여 문제를 풀이할 수 있다.(뒤에서부터 빌려주면
내림차순 정렬, 앞에서부터 빌려주면 오름차순 정렬)

문제에서 조건을 만족하는 학생의 최댓값이 무엇인지 물었다. 따라서 최대가 되는 조건을 파악해야 하는데
여기서 최대가 되는 조건은 단지 체육복의 여분이 있는 학생을 앞에서 부터 순회하며 앞의 친구가 없으면
앞의 친구를 먼저 주고, 뒤의 친구가 없으면 뒤의 친구를 주는 방법을 선택할 수 있다. 즉, 앞의 친구를
먼저 주는 방식으로 풀이하는 것인데 해당 조건을 사용하여 문제를 풀이할 경우 정답을 만족하기에
그리디 알고리즘으로 분류가 되지만 최적 부분 구조인지는 잘 모르겠다.... 
"""

def solution(n, lost, reserve):        
    lost_check = [False] * (n + 1)
    reserve_check = [False] * (n + 1)
    
    # 도난당한 사람 체크
    for num in lost:
        lost_check[num] = True
    
    # 여분이 있는 사람 체크
    for num in reserve:
        reserve_check[num] = True
        
    # 여분을 가져온 사람중에 도난당한 사람 처리
    for num in lost:
        # 여분이 있는데 도난 당했다면
        if reserve_check[num] and lost_check[num]:
            reserve_check[num] = False
            lost_check[num] = False
    
    # 여분 순회
    for i in range(1, n + 1):
        # 현재 여분이 있을 경우
        if reserve_check[i]:
            # 자기 앞 사람이 도난당한 경우
            if 1 <= i - 1 <= n and lost_check[i - 1]:
                lost_check[i - 1] = False
            # 뒤에 사람이 도난당한 경우
            elif 1 <= i + 1 <= n and lost_check[i + 1]:
                lost_check[i + 1] = False
                
    answer = n
    
    # 체육복을 빌리지 못한 사람 체크
    for i in range(1, n + 1):
        if lost_check[i]:
            answer -= 1
            
    return answer

n = 5
lost = [3]
reserve = [1]
print(solution(n, lost, reserve))