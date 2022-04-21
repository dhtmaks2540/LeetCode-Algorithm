"""
10진법의 수를 입력받아 -2진수를 출력하라

똑같이 진수 계산법을 사용하면 된다. 어차피 나머지는 0 ~ N - 1의 양수로 나오게 되어있다. 문제에서도
-2진수로 나타낸 수가 1 또는 0으로 이루어져 있다. 이를 사용해서 만약 -13이라는 10진수를 -2진수로 
변경한다면 아래와 같은 과정을 겪는다.

-13 = (-2) * 7 + 1
7 = (-2) * (-3) + 1
-3 = (-2) * 2 + 1
2 = (-2) * (-1) + 0
-1 = (-2) * 1 + 1
1 = (-2) * 0 + 1

따라서 1101111이라는 값이 나오게 된다. 이러한 조건을 사용해서 아래와 같이 두 가지 방식으로
풀 수 있다.
"""

def solution1():
    import math
    
    # 10진법으로 표현된 수
    N = int(input())
    answer = ""
    remainder = 0

    # 0이 아니라면
    if N != 0:
        # 0이 될때까지
        while N != 0:
            # 나머지 계산
            remainder = abs(N % -2)
            answer = str(remainder) + answer
            # 올림 처리(-6.5 -> -7)
            N = math.ceil(N / -2)
            
        print(answer)
    else:
        print("0")
        
def solution2():
    # 10진법으로 표현된 수
    N = int(input())
    answer = ""
    
    # 예외처리
    if N == 0:
        print(0)
    else:
        while N != 0:
            # 나누어 떨어진다면
            if N % -2 == 0:
                answer = '0' + answer
                N = N // -2
            # 나누어 떨어지지 않는다면
            else:
                answer = '1' + answer
                N = N // (-2) + 1
                
    print(answer)