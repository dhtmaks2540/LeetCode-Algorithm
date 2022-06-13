"""
id를 규칙에 맞지 않으면 변경한 후 출력하라

시간제한없이 규칙에 맞게 주어진 문자열을 변경하는 문제이다. 단지 규칙을 잘 준수하여 구현하여
풀이하면 되고, 파이썬이나 코틀린에서 많은 현재 글자가 알파벳인지, 영어인지 등의 많은 함수를
지원하니 이들을 사용하면 된다.
"""

import collections

def solution(new_id):
    correct_symbol = "-_."
    
    # 1단계
    new_id = new_id.lower()
    new_id = list(new_id)

    temp = []

    # 2단계
    for index in range(len(new_id)):
        # 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 문자 제거
        if new_id[index].isalnum() or new_id[index] in correct_symbol:
            temp.append(new_id[index])
    
    new_id = temp
            
    # 3단계
    temp = []
    for index in range(len(new_id)):
        if temp and temp[-1] == '.' and new_id[index] == '.':
            temp.pop()
        
        temp.append(new_id[index])
        
    new_id = collections.deque(temp)
    
    # 4단계
    index = 0
    while index < len(new_id):
        if  index == 0:
            if new_id[index] == '.':
                new_id.popleft()
        elif index == len(new_id) - 1:
            if new_id[index] == '.':
                new_id.pop()
                
        index += 1
    
    # 5단계
    if not new_id:
        new_id.append('a')
        
    # 6단계
    if len(new_id) >= 16:
        while len(new_id) > 15 or new_id[-1] == '.':
            new_id.pop()
            
    # 7단계
    if len(new_id) <= 2:
        while len(new_id) <= 2:
            new_id.append(new_id[-1])
        
    return "".join(new_id)

new_id = "abcdefghijklmn.p"
print(solution(new_id))