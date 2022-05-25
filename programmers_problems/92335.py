import math

def solution(n, k):
    answer = 0
    # 10진수 -> k 진수로
    change_n = change(n, k)
    stack = [""]
    
    for i in range(len(change_n)):
        # 현재 값이 0이 아니라면
        if change_n[i] != '0':
            # 최근 값에 계속해서 추가
            stack[-1] += change_n[i]
        else: # 현재 값이 0이라면
            stack.append("")
            
    for x in stack:
        # 공백이 아니고 현재 값이 소수라면
        if x and isPrime(int(x)):
            answer += 1
    
    return answer

# 10진수를 n진수로 변경하는 코드
# 10진수 이하이므로 'A', 'B' 등의 값을 처리하는 코드는 X
def change(n, k):
    value = ""
    remainder = 0
    
    # n이 0이 될때까지
    while n:
        # 나머지 계산
        remainder = n % k
        # 결과 변수에 더해주기
        value = str(remainder) + value
        n //= k
        
    return value

def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

n = 437674
k = 3
result = solution(n, k)
print(result)