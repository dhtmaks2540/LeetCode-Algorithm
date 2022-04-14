import sys

# 정수의 개수
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split(" ")))
# 오름차순 정렬
numbers.sort()
print(numbers[0], numbers[-1])