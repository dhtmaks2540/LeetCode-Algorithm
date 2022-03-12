# 신고 결과 받기

import collections

"""
해시 테이블을 사용하여 접근한 이유

우선 사람에 따른 신고자들을 저장하기 위해서 key, value 형식으로 저장할 필요가 있어 해시 테이블을 사용했다
또한, 신고에 성공한 사람들도 기록하기 위해 이 또한 해시 테이블을 사용했다
"""


def solution(id_list, report, k):
    report_dic = collections.defaultdict(list)
    report_num = collections.defaultdict(int)
    
    # id 리스트 기록
    for id in id_list:
        report_dic[id]
        report_num[id]
        
    # 신고 기록 
    for value in report:
        # 신고한 사람, 신고받은 사람
        from_person, to_person = value.split(" ")
        # 신고한 사람이 같은 사람을 두 번 이상 중복 신고하지 않았다면
        if from_person not in report_dic[to_person]:
            report_dic[to_person].append(from_person)
            
    for _, value in report_dic.items():
        # k번 이상 신고 당함
        if len(value) >= k:
            for from_person in value:
                report_num[from_person] += 1
                
    return list(report_num.values())