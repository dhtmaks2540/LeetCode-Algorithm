# 주사위 눈
a, b, c = map(int, input().split(" "))

# 세 눈이 모두 같다면
if a == b and b == c:
    print(10000 + a * 1000)
# 두 눈이 같다면
elif a == b or a == c or b == c:
    if a == b:
        print(1000 + a * 100)
    elif a == c:
        print(1000 + a * 100)
    elif b == c:
        print(1000 + b * 100)
# 세 눈이 모두 다르다면
else:
    print(max(a, b, c) * 100)