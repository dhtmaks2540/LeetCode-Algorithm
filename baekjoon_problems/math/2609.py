"""
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하라

공약수 -> 두 수 이상의 여러 수의 공통된 약수를 의미
최대공약수(GCD) -> 두 수 이상의 여러 수의 공약수 중 최대인 수

* gcd(a,b) = 1이면, 두 수 a,b는 서로소(coprime) 관계에 있다고 표현

공배수 -> 두 수 이상의 여러 수의 공통된 배수
최소공배수(LCM) -> 두 수 이상의 여러 수의 공배수 중 최소인 수

https://mathbang.net/204
"""
a, b = map(int, input().split(" "))

# 최대 공약수
gcd = min(a, b)

# 작은 값부터 1까지 iteration
for i in range(gcd, 0, -1):
    # 현재 수로 두 수가 나누어 떨어진다면 최대 공약수에 해당
    if a % i == 0 and b % i == 0:
        gcd = i
        break

# 최소 공배수는 지수 * 나머지에 해당
lcm = gcd * (a // gcd) * (b // gcd)
print(gcd)
print(lcm)