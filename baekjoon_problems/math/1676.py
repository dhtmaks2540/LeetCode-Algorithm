"""
N! 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하라

파이썬의 factorial 함수를 사용하여 문제 풀이. 시간복잡도는 O(N!의 길이)

https://st-lab.tistory.com/165

뒷자리에 0이 나오는 경우는 2와 5가 곱해져 있을 때이다. 즉, 이 말은 거꾸로 말하면 소인수분해를 해서
2와 5가 존재할 경우 뒷자리는 0으로 끝난다는 것이다.

예를 들어 30은 2 * 3 * 5는 2와 5가 포함되어있다.
231400의 경우 2^3 * 5^2 * 13 * 89로 2와 3이 포함된다.

이러한 소인수분해의 성질을 이용하면 매우 쉽게 풀 수 있다.

기본적으로 팩토리얼 값을 보면 2는 5보다 작은 수여서 연속된 수를 곱하게 되면 자연스레 모든 값들의 소인수
분해들은 2의 개수가 5의 개수보다 많다. 즉, 기본적으로 5의 개수에 따라 값이 변한다.
따라서 이를 사용해 반복문을 통해 5로 나누면서 누적합을 해주면 된다.
"""

# 파이썬과 같이 숫자의 제한이 없을 경우 풀 수 있는 방법
from re import I


def solution():
    import math

    N = int(input())
    fac_num = str(math.factorial(N))

    count = 0

    for i in range(len(fac_num) - 1, -1, -1):
        if fac_num[i] == '0':
            count += 1
        else:
            break
        
    print(count)
    
def solution2():
    N = int(input())
    
    count = 0
    
    while N >= 5:
        count += N // 5
        N //= 5
        
    print(count)
    
# solution2()

def solution3():
    N = int(input())
    
    ans_2 = 0
    ans_5 = 0
    
    for i in range(1, N + 1):
        j = i
        while j % 2 == 0:
            j //= 2
            ans_2 += 1
        j = i
        while j % 5 == 0:
            j //= 5
            ans_5 += 1
            
    print(min(ans_2, ans_5))
    
# solution3()