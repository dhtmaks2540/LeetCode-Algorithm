"""
문자열 T와 P가 주어졌을 때, 문자열 T에서 P는 몇 번 나오며 나타나는 위치를 출력하라

KMP 알고리즘을 사용하여 문제 풀이
KMP 알고리즘은 문자열 검색 알고리즘으로 단순히 브루드포스로 푸는 방법(O(NM))에 비해
시간 복잡도가 문자열 S의 길이가 N, 패턴 p의 길이가 M이라고 한다면 O(N + M)으로 줄어든다.

KMP 알고리즘을 이해하기위해 먼저 해당 인덱스에서 접두사, 접미사가 같은 최대를 구하는 PI 테이블을 
구해야 한다. 해당 테이블을 구한 후 PI 테이블을 사용해 중복되는 부분을 획기적으로 줄이는 방식이다.
"""

T = input()
P = input()
answer = []

# 패턴의 해당 인덱스에서 접두사와 접미사가 같은 최대 개수 테이블
def get_pi(p):
    # pi 테이블
    pi = [0] * len(p)
    j = 0
    
    # 1부터 확인(i는 계속해서 증가)
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]: # j가 0이거나, i와 j의 문자열이 같을 때까지 반복
            j = pi[j - 1]

        if p[i] == p[j]: # i와 j가 같은 겨웅 j 증가
            j += 1
            pi[i] = j # i 번째의 값으로 j 저장

    return pi

def kmp(s, p):
    global answer

    # pi 획득
    pi = get_pi(p)
    
    # 패턴을 탐색할 인덱스
    j = 0
    
    # 문자열을 순회하는 인덱스 i
    for i in range(len(s)):
        # j가 0이거나 문자열에서 i 인덱스가 가리키는 값과 패턴에서 j 인덱스가 가리키는
        # 문자가 같을 때까지 반복
        while j > 0 and s[i] != p[j]:
            j = pi[j - 1]

        # 만약 해당 문자가 같을 때
        if s[i] == p[j]:
            # j와 패턴 문자열의 길이 - 1이 같다면 매칭에 성공
            if j == len(p) - 1:
                # 결과 변수에 해당 인덱스 넣기
                answer.append(i - len(p) + 2)
                # j 테이블 갱신
                j = pi[j]
            # 매칭에 성공하지 않았다면 j 값 증가
            else:
                j += 1

kmp(T, P)

print(len(answer))
for idx in answer:
    print(idx, end = " ")