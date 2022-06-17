"""
수포자가 문제를 찍는 방법과 정답지가 주어졌을 때, 수포자 중 가장 많은 정답을 맞춘 사람을 출력하라

해당 문제는 수포자들이 각각 찍은 방법과 정답지를 비교하며 맞은 개수를 체크하는 방법으로 모두 완전
탐색을 통해 수행할 수 밖에 없다. 따라서 정답지의 길이보다 더 크게 수포자들이 찍는 방법을 문자열로
만든 후, 정답지를 순회하며 정답을 채점하고 가장 많이 맞춘 사람을 출력하면 된다.

모든 경우를 탐색하는 완전 탐색에 대해 파악하는 문제인듯하다. 다만, 완전 탐색을 수행할 때는 중간중간
연산을 최대한 간결하게 만들어 시간 복잡도를 줄이는 것이 중요한 포인트인것 같다.
"""

def solution(answers):
    answer = []
    
    answers = list(map(str, answers))
    len_answers = len(answers)
    
    first_man = "12345"
    second_man = "21232425"
    third_man = "3311224455"
    
    # 정답지의 길이 맞추기
    first_man *= (len_answers // len(first_man) + 1)
    second_man *= (len_answers // len(second_man) + 1)
    third_man *= (len_answers // len(third_man) + 1)
    
    # 각 수포자들이 정답을 맞춘 횟수
    first_man_cnt = 0
    second_man_cnt = 0
    third_man_cnt = 0
    
    # 정답지 순회하며 채점하기
    for index in range(len_answers):
        if first_man[index] == answers[index]:
            first_man_cnt += 1
        
        if second_man[index] == answers[index]:
            second_man_cnt += 1
        
        if third_man[index] == answers[index]:
            third_man_cnt += 1
            
    max_cnt = -1
            
    # 최고 점수자 출력
    for index, num in enumerate([first_man_cnt, second_man_cnt, third_man_cnt]):
        if num > max_cnt:
            answer.clear()
            answer.append(index + 1)
            max_cnt = num
        elif num == max_cnt:
            answer.append(index + 1)
    
    return answer

answers = [5, 5, 5, 1, 4, 1]
print(solution(answers))