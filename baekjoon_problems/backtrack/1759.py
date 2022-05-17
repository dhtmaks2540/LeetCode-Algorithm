"""
사전식으로 가능성 있는 암호를 모두 출력하라

주어진 문자열을 정렬한 후 백트래킹(DFS 탐색)을 수행하면 기본적으로 만들어지는 문자열은 정렬된 순서로
배열이 될 것 이다. 다만 DFS 탐색이므로 종료 조건이 필요한데 종료 조건으로 현재 만들어진
암호가 L 글자이면서 모음 1개, 자음 2개 이상으로 이루어져있는지를 주어서 무한 루프에 빠지지 않도록
만든다.
"""

import sys

# 암호의 개수, 문자의 종류
L, C = map(int, sys.stdin.readline().strip().split(" "))
# 문자 암호
array = sorted(sys.stdin.readline().strip().split(" "))
# 배열의 길이
len_n = len(array)
# 자음
vowel_list = ['a', 'e', 'i', 'o', 'u']
answer = []

# 모음 1개, 자음 2개 이상으로 이루어졌는지 확인
def check_can_password(password):
    consonant_cnt = 0
    vowel_cnt = 0
    for x in password:
        if x in vowel_list:
            vowel_cnt += 1
        else:
            consonant_cnt += 1
            
        if consonant_cnt >= 2 and vowel_cnt >= 1:
            return True
        
    return False

def dfs(index, password):
    # 종료 조건(길이가 L이며 최소 모음 1개, 자음 2개로 이루어졌다면)
    if len(password) == L and check_can_password(password):
        # 결과변수에 추가 및 return
        answer.append(password)
        return
    
    for i in range(index, len_n):
        dfs(i + 1, password + array[i])
        
dfs(0, "")

for x in answer:
    print(x)