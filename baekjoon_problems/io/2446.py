n = int(input())

for i in range(n, 0, -1):
    # 공백
    for j in range(n - i):
        print(" ", end="")
    # 별
    for j in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(2, n + 1):
    # 공백
    for j in range(n - i):
        print(" ", end="")
    # 별
    for j in range(2 * i - 1):
        print("*", end="")
    print()