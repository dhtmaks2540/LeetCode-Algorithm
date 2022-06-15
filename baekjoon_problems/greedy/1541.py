"""
숫자와 +, -로 이루어진 문자열이 주어졌을 때, 적절히 괄호를 쳐 숫자를 최소로 만들어라

위와 같은 문자열이 주어졌을 때 숫자를 최소로 만드는 방법은 -가 주어졌을 때마다 괄호를 치면 된다.
이는 -가 주어진 시점부터 모든 숫자를 음수로 처리하면 성립한다. 그 이유는 -가 나온 후 또 -가 나오면
계속해서 음수로 처리하면 되고, +가 나오면 괄호로 묶기 때문에 그 또한 음수로 처리하면 되기 때문이다.
따라서 -가 나오기 전까지는 +로 모든 숫자를 처리하고, -가 나온 시점부터는 해당 숫자를 음수로 처리하면
정답을 출력할 수 있다. 현재 문제는 그리디 알고리즘을 사용한 문제로 값을 최소로 만들기 위해서
-가 나온 시점부터 모든 값을 음수로 처리하는 방법을 선택한 것이다. 이는 뒤의 결과는 생각하지 않고
이와 같은 결과를 선택해도 정답이 출력되기에 그리디 알고리즘을 사용할 수 있는 것이다. 

이 문제에서 얻어가는 것은 그리디 알고리즘의 조건을 만드는 방법인듯하다.

"""

import sys

array = sys.stdin.readline().strip()
prev_oper = '+'
index = 0
answer = 0

while index < len(array):
    # 현재 문자가 숫자라면
    if array[index].isdigit():
        num = ""
        # 숫자 모두 뽑아내기
        while index < len(array) and array[index].isdigit():
            num = num + array[index]
            index += 1
        
        # 현재 저장된 연산이 +라면
        if prev_oper == '+':
            answer += int(num)
        # 현재 저장된 연산이 -라면
        else:
            answer += -(int(num))
    # 현재 문자가 연산이라면
    else:
        # 현재 숫자가 -라면
        if array[index] == '-':
            prev_oper = '-'
                
        index += 1

print(answer)