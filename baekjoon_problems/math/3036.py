"""
링의 개수와 각 링의 반지름이 주어질 때, 첫 번째 링을 한 바퀴 돌리면 나머지 링은 몇 바퀴 돌아가는지
구하라

예제로 주어진 입력과 출력을 보면 첫 번째 링을 분자로 하고 나머지 링들을 분모로 설정한 바퀴 수만큼
돈다는 것을 파악할 수 있다. 이는 두 수의 최대공약수를 구한 뒤 나누는 것과 마찬가지로 유클리드 호제법
을 사용하여 풀이할 수도 있다.
"""

def solution1():
    import sys

    # 링의 개수
    N = int(sys.stdin.readline().strip())
    array = list(map(int, sys.stdin.readline().strip().split(" ")))

    for i in range(1, N):
        for j in range(array[i], 0, -1):
            if array[0] % j == 0 and array[i] % j == 0:
                print(f"{array[0] // j}/{array[i] // j}")
                break
            
def solution2():
    import sys
    
    def GCD(a, b):
        while b != 0:
            remainder = a % b
            a = b
            b = remainder
            
        return a
    
    # 링의 개수
    N = int(sys.stdin.readline().strip())
    array = list(map(int, sys.stdin.readline().strip().split(" ")))
    
    for i in range(1, N):
        gcd_value = GCD(array[0], array[i])
        print(f"{array[0] // gcd_value}/{array[i] // gcd_value}")
        
solution2()