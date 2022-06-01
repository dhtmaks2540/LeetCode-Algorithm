"""
666이 포함된 문자열의 순서를 계산해서 N 번째 숫자를 출력하라

브루트 포스로 숫자를 증가시키며 666이 포함되어 있는 경우 count를 증가시켜서 풀이했다.

https://st-lab.tistory.com/103 <- 규칙을 찾아서 풀이하는 방법도 있다.
"""

# 브루트 포스를 사용
def solution1():
    N = int(input())
    # 몇 번째인지를 나타내는 변수
    cnt = 1
    value = 666

    while cnt != N:
        value += 1
        
        # 666이 포함되어있다면 카운트 증가
        if '666' in str(value):
            cnt += 1
            
    print(value)
    
solution1()