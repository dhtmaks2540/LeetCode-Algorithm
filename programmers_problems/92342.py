"""
어피지가 쏜 화살의 점수가 주어졌을 때, 라이언이 어피치를 이기는 점수의 최댓값을 구하라.
다만 점수가 같을 경우에는 낮은 점수를 더 많이 쏜 경우를 반환하라.

문제를 잘못봐서 라이언이 어피치를 이기는 경우 점수의 최댓값을 사용하였는데 알고보니
라이언과 어피치 점수차가 가장 큰 경우를 출력하도록 하는 문제였다. 이를 조건으로 사용해서
DFS로 문제를 풀이하였다. 우선 DFS를 사용하므로 종료 조건이 필요하기에 종료 조건은 현재 
주어진 화살을 다 쏜 경우로 잡았다. 화살을 다 쏘면 깊이 우선 탐색이
완료된 경우이며, 이제 라이언과 어피치의 점수를 계산한 후
라이언의 점수에서 어피치의 점수를 뺀 경우가 현재 최댓값보다 큰 경우 갱신하면 이 값을
리스트에 저장하도록 하였다. 또한 현재 최댓값보다 같으면 계속해서 리스트에 추가하도록 하였다.
그 이유는 점수가 같은 경우에는 가장 낮은 점수를 많이 쏜 경우를 출력해야하기 때문이다.

조건의 아래는 10점부터 0점까지 순회하며 1발부터 현재 주어진 화살까지 순회하면서
현재 주어진 화살로 그 점수를 쏘고 DFS를 호출하도록 하였다.

깔끔한 풀이

https://programmers.co.kr/learn/courses/30/lessons/92342/solution_groups?language=python3
"""

max_lion_score = 0

def solution(n, info):
    answer = []
    
    # DFS를 통해 깊이 우선 탐색
    def dfs(index, cnt, path):
        global max_lion_score
        
        # 화살을 다 쏘았다면(종료 조건)
        if cnt == 0:
            lion_score = 0
            apeach_score = 0
            # 라이언의 점수와 어피치의 점수 확인
            for i in range(11):
                if path[i] > info[i]:
                    lion_score += 10 - i
                elif info[i] and path[i] <= info[i]:
                    apeach_score += 10 - i
            
            # 라이언의 점수가 더 높을 때
            if apeach_score < lion_score:
            # 그 차이가 최고 점수라면
                if max_lion_score < lion_score - apeach_score:
                    answer.clear()
                    answer.append(path[:])
                    max_lion_score = lion_score - apeach_score
                elif max_lion_score == lion_score - apeach_score: # 최고 점수가 같은 경우라면
                    answer.append(path[:])
                
            return
        
        # 10점부터 0점까지 순회        
        for i in range(index, 11):
            # 현재 주어진 화살을 사용해서 쏘기
            for j in range(1, cnt + 1):
                # 쏜 후 다시 제거
                path[i] = j
                dfs(i + 1, cnt - j, path)
                path[i] = 0
            
    dfs(0, n, [0] * 11)
    
    # 어피치를 이길 수 없다면
    if max_lion_score == 0:
        return [-1]
    # 이길 수 있다면 더 낮은 점수를 많이 쏜 값을 출력하도록 정렬
    else:
        answer.sort(key=lambda x : (x[10], x[9], x[8], x[7], x[6], x[5], x[4], x[3], x[2], x[1], x[0]))
        return answer[-1]

n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]
result = solution(n, info)
print(result)
print(max_lion_score)