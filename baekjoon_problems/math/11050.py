"""
https://st-lab.tistory.com/159#%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

이항 계수는 말 그대로 '두개의 항(이항)을 전개하여 계수로 나타낸 것'이다.
쉽게 말하면, (a + b)^n을 전개하였을 때 계수를 의미한다는 것이다.

예를들어 (a + b)^2 = a^2 + 2ab + b^2이고, 계수는 {1,2,1}
(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3이고, 게수는 {1,3,3,1}
이와 같이 전개하다보면 파스칼의 삼각형이 나온다.

이러한 이항 계수는 n승에 대해 전개하면 다음과 같은 '항'이 나온다(계수는 쓰지 않고 항만 쓸 경우)
(a + b)^n = {a^nb^0, a^n-1b^1, a^n-2b^2, ⋯ , a^n-rb^r, ⋯ , a^2b^n-2. a^1b^n-1, a^0b^n}
이를 식으로 표현하자면 (a + b)^n에 대해 전개했을 때, a^n-rb^r에 대한 계수가 나온다.

항을 구하는 방식은 위와 같고 이제 계수를 구하는 방법을 알아야 한다.
(a + b)^n 에서 계수를 찾는다는 말은 a와 b가 조합되어 나온 값이 된다는 것이다. 예를 통해 알아보겠다.

(a + b)^3을 전개할 때 b에 번호를 붙여서 보도록 하겠다.

(a + b)^3 = (a + b)(a + b)(a + b)
→ (a + b1)(a + b2)(a + b3)
→ a^3 + (b1 + b2 + b3)a^2 + (b1b2 + b2b3 + b3b1)a + b1b2b3

이 식을 해석해보면 아래와 같다.
a^3항은 {b1, b2, b3} 중에서 한 개도 뽑지 않는다. 즉, 0개를 뽑는다.
a^2항은 {b1, b2, b3} 중에서 한 개씩 뽑아서 모두 더한 값이다.
a^1항은 {b1, b2, b3} 중에서 두 개씩 뽑아 곱한 뒤 모두 더한 값이다.
a^0항은 {b1, b2, b3} 중에서 세 개를 뽑아 모두 곱한 값이다.

즉, b가 n개 있을 때 이들중에 r개를 뽑는다는 것이다. 따라서 조합 공식이라고 볼 수 있다.
한마디로 계수는 nCr이 되는 것이다.

a^3 항은 b들 중 한 개도 뽑지 않으니 3C0 이 되는 것이고,
a^2 항은 b들 중 한 개씩 뽑는 것이니 3C1 이 되는 것이고,
a^1 항은 b들 중 두 개씩 뽑는 것이니 3C2 가 되는 것이고,
a^0 항은 b들 중 세 개 뽑는 것이니 3C3 이 된다.

조합 nCr의 식 = (n! / (r! * (n - r)!))
"""

# 팩토리얼을 사용하여 풀이
def solution1():
    def factorial(N):
        if N <= 1:
            return 1
        
        return N * factorial(N - 1)
    
    N, K = map(int, input().split(" "))
    
    print(int(factorial(N) / (factorial(K) * factorial(N - K))))
    
# 팩토리얼 하나로 합치기
def solution2():
    def BC(N, K):
        # 2번 성질
        if N == K or K == 0:
            return 1
        
        return BC(N - 1, K - 1) + BC(N - 1, K)
    
    N, K = map(int, input().split())
    print(BC(N, K))
    
# 다이나믹 프로그래밍을 황용
def solution3():
    N, K = map(int, input().split())
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    
    def BC(N, K):
        # 이미 풀었던 sub문제일 경우 값을 재활용
        if dp[N][K] > 0:
            return dp[N][K]
        
        # 2번 성질
        if N == K or K == 0:
            dp[N][K] = 1
            return dp[N][K]
        
        # 1번 성질
        dp[N][K] = BC(N - 1, K - 1) + BC(N - 1, K)
        
        return dp[N][K]
    
    print(BC(N, K))
    
# solution1()
# solution2()
# solution3()