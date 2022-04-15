n = int(input())

for i in range(1, n + 1):
    # 공백
    for j in range(n - i):
        print(" ", end="")
    # 별
    for k in range(2 * i - 1):
        print("*", end="")
    # 공백
    # for j in range(n - i):
    #     print(" ", end="")
    print()