import sys
import math

# 에라토스테네스의 체를 사용한 소수 판별
MAX_VALUE = 123456 * 2
prime_num = [True] * (MAX_VALUE + 1)

for i in range(2, int(math.sqrt(MAX_VALUE)) + 1):
    if prime_num[i]:
        j = 2
        while i * j <= MAX_VALUE:
            prime_num[i * j] = False
            j += 1
prime_num[1] = False
            
while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    
    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if prime_num[i]:
            cnt += 1
            
    print(cnt)