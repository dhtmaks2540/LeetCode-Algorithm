"""
접근방법

조건을 잘 파악한 후 배열에 조건을 대입하여 풀이했다.
최대 순위라는 것은 단지 zero_count가 다 맞춘 순위이고
최저 순위라는 것은 단지 현재 맞춘 것만 순위로 치는 것이므로
아래와 같이 풀이하였다.

"""

def solution(lottos, win_nums):
    # 순위를 기록하기 위한 해시 테이블
    lank = {
        6:1,
        5:2,
        4:3,
        3:4,
        2:5,
        1:6,
        0:6
    }
    
    result = 0
    zero_count = 0
    
    # 로또 번호를 iterate하며
    for number in lottos:
        # 만약 번호를 맞췄다면
        if number in win_nums:
            result += 1
        # 번호가 지워진 숫자라면
        elif number == 0:
            zero_count += 1
    
    # 최고 순위는 zero_count를 더하고, 최저는 그 숫자 그대
    return [lank[result + zero_count], lank[result]]