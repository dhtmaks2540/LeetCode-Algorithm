"""
첫째 줄에 김지민이 K개의 글자를 가르칠 때, 학생들이 읽을 수 있는 단어 개수의 최댓값을 출력한다.

문제풀이

해당 문제는 백트래킹을 이용하여 푸는 문제이다. 백트래킹(DFS)라고 하여 무조건 예시 리스트만 순환하며
조건을 검사하는 것이 아닌 하나의 방문처리 리스트를 만들고 해당 리스트를 사용해서 재귀적으로
함수를 호출할 수도 있다. 유연하게 완전 탐색을 생각해야 한다.

이 문제 같은 경우는 알파벳 글자의 리스트 변수를 만들고
해당 글자를 방문했다고 가정한 후, 백트래킹을 호출하며 현재 글자가 주어진 조건의 배울 수 있는
글자의 수와 같다면(백트래킹의 조건) 현재 상황에서 배울 수 있는 단어의 최댓값을 계산하고 반환하는
방식으로 문제를 풀 수 있다.

완전 탐색에 대해서 유연하게 생각하며 백트래킹의 조건도 잘 생각해야 하는게 이 문제의 포인트같다..
"""

# 단어의 개수, 배울 수 있는 글자의 수
N, K = map(int, input().split())
# 단어 기록
words = []
# 알파벳 리스트(방문처리 리스트와 같다)
visited = [False] * 27
# 결과변수
answer = 0

def backtracking(alpha, cnt):
    global answer

    # k개를 다 배운 경우
    if cnt == K:
        # 배울 수 있는 단어의 개수
        temp = 0
        # 단어 iterate
        for i in range(N):
            flag = True
            # 익히지 않은 알파벳이 있는 경우 배울 수 없는 단어
            for j in range(len(words[i])):
                if not visited[ord(words[i][j]) - ord('a')]:
                    flag = False
                    break

            # 배운 단어라면
            if flag:
                temp += 1
        
        # 현재 글자를 배운 경우 최댓값 갱신
        answer = max(answer, temp)
        return
    
    # 아직 K개를 배우지 않은 경우 : 브루트 포스(알파벳을 순환)
    for c in range(alpha, 27):
        # 현재 단어를 배우지 않았다면
        if not visited[c]:
            # 배웠다고 처리
            visited[c] = True
            # backtracking 함수 호출
            backtracking(c, cnt + 1)
            # 배운거 다시 제거
            visited[c] = False

# 예외처리
if K < 5: # 하나도 못 배울 경우
    print(0)
    exit()
elif K == 26: # 전부 배울 경우
    print(N)
    exit()

# 'a', 'n', 't', 'i', 'c'는 접두사, 접미사이므로 당연히 배워야 하는 단어이기에 제거
K -= 5
for _ in range(N):
    data = input().replace("anta", "").replace("tica", "")
    words.append(data)

# a, c, i, n, t 무조건 포함(방문처리)
visited[ord('a') - ord('a')] = True
visited[ord('c') - ord('a')] = True
visited[ord('i') - ord('a')] = True
visited[ord('n') - ord('a')] = True
visited[ord('t') - ord('a')] = True

backtracking(0, 0)
print(answer)