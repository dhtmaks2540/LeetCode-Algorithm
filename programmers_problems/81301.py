"""
숫자와 알파벳이 주어질 때 모두 숫자로 변경해라.

숫자 영단어를 맵에 키는 영단어로, 값은 숫자로 하여 미리 저장해둔다. 그 후 현재 글자가
숫자라면 그대로 사용하면되고, 현재 글자가 문자라면 무슨 문자인지 판별한 후에 숫자로 변경하여
사용하면 된다. 문자열의 최대 길이가 50이고, 시간제한이 10초이므로 충분히 시간안에 풀이할 수 있다.

"""


def solution(s):
    answer = ""
    
    num_dic = {
        "zero" : '0',
        "one" : '1',
        "two" : '2',
        "three" : '3',
        "four" : '4',
        "five" : '5',
        "six" : '6',
        "seven" : '7',
        "eight" : '8',
        "nine" : '9'
    }
    
    index = 0
    
    while index < len(s):
        # 현재 글자가 숫자라면 
        if s[index].isdigit():
            answer += s[index]
            index += 1
        # 현재 글자가 문자라면
        else:
            num = ""
            while index < len(s) and not s[index].isdigit():
                num += s[index]
                index += 1
                
                # 현재 글자가 숫자로 변경된다면 변경 후 빠져나가기
                if num in num_dic:
                    answer += num_dic[num]
                    break
        
    return answer

s = "2three45sixseven"
solution(s)