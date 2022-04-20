"""
10진법의 수 N이 주어지면, 이 수를 B진법으로 바꿔 출력하라

결과와 나머지 변수를 가지고, 현재 숫자에 진수를 계속해서 나누면서 해당 값이 10이상인지('A', 'B' 등)
아닌지를 분기하며 결과 변수에 계속해서 추가해주면된다. 이를 0보다 클 경우에만 해준다면 10 진수의
숫자를 N진법의 숫자로 변경할 수 있다
"""

def solution1():
    num, base = map(int, input().split(" "))
    # 결과
    answer = ""
    # 나머지
    remainder = 0

    while num > 0:
        remainder = num % base
        
        # 진수로 나누었는데 나머지가 10보다 작다면 해당 숫자 바로 append
        if remainder < 10:
            answer = str(remainder) + answer
        # 10보다 크다면
        else:
            answer = chr(remainder - 10 + ord('A')) + answer
        
        num //= base
        
    print(answer)
    
def solution2():
    # 10진수를 n진수로 변환
    def convert_notation(n, base):
        T = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        q, r = divmod(n, base)
        return convert_notation(q, base) + T[r] if q else T[r]
    
    num, base = map(int ,input().split(" "))
    print(convert_notation(num, base))
    
solution2()