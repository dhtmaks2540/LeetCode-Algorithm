"""
https://programmers.co.kr/learn/courses/30/lessons/42888

접근방법

우선, 유저 아이디와 닉네임을 저장하기 위해서 해시 테이블을 사용했다.
Key는 유저 아이디, Value는 닉네임으로 지정한 후 O(1)의 시간복잡도를 가지고 접근한다.

그리고 기록된 결과를 저장하기 위해 리스트를 사용해서 문제의 조건에 맞도록
Enter와 Leave의 경우를 리스트에 저장(스택 또는 큐를 사용해도 무방)
이때, 리스트에는 어떤 유저가 해당 상태를 통해 기록을 남겼는지 확인하기 위해서 유저 아이디, 상태와 같이
튜플 형태로 데이터를 기록했다.

그 후 리스트를 순회하며 해당 상태에서의 닉네임을 가져와 이를 결과 리스트에 넣는 방식으로 문제를 풀이
"""

# 시간 복잡도 O(n)
def solution(record):
    answer = []
    
    # Status와 Id 기록하는 리스트
    log_lis = []
    # Id, 닉네임
    user_dic = {}
    
    for i in range(len(record)):
        log = record[i].split(" ")

        # 상태 비교
        if log[0] == "Enter": # Enter
            # 해시 테이블에 아이디, 닉네임 기록 및 로그 기록
            user_dic[log[1]] = log[2]
            log_lis.append((log[0], log[1]))
            # 로그 기록
        elif log[0] == "Leave": # Leave
            log_lis.append((log[0], log[1]))
        else: # Change
            # 해시테이블에 아이디, 닉네임 기록
            user_dic[log[1]] = log[2]

    # log iterate
    for log in log_lis:
        status, id = log
        if status == "Enter":
            answer.append(f"{user_dic[id]}님이 들어왔습니다.")
        else:
            answer.append(f"{user_dic[id]}님이 나갔습니다.")
        
    return answer

"""
https://programmers.co.kr/learn/courses/30/lessons/42888/solution_groups?language=python3
"""
def solution(record):
    answer = []
    # 아이디, 이름 기록하는 해시 테이블
    namespace = {}
    printer = {
        'Enter':'님이 들어왔습니다.',
        'Leave': '님이 나갔습니다.'
        }

    for r in record:
        rr = r.split(" ")
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        log = r.split(" ")
        if log[0] != "Change":
            answer.append(namespace[log[1]] + printer[log[0]])

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))

result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]