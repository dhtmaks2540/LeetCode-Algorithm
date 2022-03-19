"""
문자열 S와 P가 주어졌을 때, P가 S의 부분 문자열인지 아닌지 파악

KMP 알고리즘을 이용하여 푸는 문제로 KMP 알고리즘은 문자열 검색에 많이 사용되는
알고리즘이다. 이 알고리즘의 핵심은 접두사와 접미사를 사용하여 똑같은 문자열의 길이를 저장하는 테이블을
만든 후 해당 테이블을 사용하여 문제를 푸는것이다.

KMP 알고리즘에 유형에 대한 개념과 예시 문제 여러개 풀어보도록 하자.
"""

s = input()
p = input()

# 패턴의 길이만큼 접두사 접미사가 같은 최대수를 반환
def get_pi(p):
    pi = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]: # j가 0이거나, i와 j의 문자열이 같을때까지 반복
            j = pi[j - 1]

        if p[i] == p[j]: # i와 j가 같은 경우 j 증가
            j += 1
            pi[i] = j # i 번째의 값으로 j 저장

    return pi

def kmp(s, p):
    pi = get_pi(p)
    
    j = 0

    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = pi[j - 1]
        
        if s[i] == p[j]:
            if j == len(p) - 1:
                return 1
            else:
                j += 1

    return 0

print(kmp(s, p))