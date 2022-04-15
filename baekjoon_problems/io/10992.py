n = int(input())

# 마지막 줄만 2 * n - 1, 나머지는 2개

for i in range(1, n + 1):
    # 공백
    for j in range(n - i):
        print(" ", end="")
    # 별
    if i == n or i == 1:
        for j in range(2 * i - 1):
            print("*", end="")
    else:
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * i - 2:
                print("*", end="")
            else:
                print(" ", end="")
    print()