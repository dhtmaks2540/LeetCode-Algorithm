"""
조합을 출력하는 문제로 주어진 n개의 숫자 중 6개의 조합을 만드는 문제이다.

"""

# 라이브러리 사용
def solution1():
    import sys
    import itertools

    while True:
        values = list(map(int, sys.stdin.readline().strip().split(" ")))
        if values[0] == 0:
            break
        
        # 수의 개수, 수
        k, nums = values[0], sorted(values[1:])
        
        for combi in list(itertools.combinations(nums, 6)):
            for x in combi:
                print(x, end=" ")
            print()
        print()
        
# DFS 사용
def solution2():
    import sys
    
    def dfs(index, path):
        if len(path) == 6:
            answer.append(path)
            return
        
        for i in range(index, k):
            dfs(i + 1, path + [nums[i]])
    
    while True:
        values = list(map(int, sys.stdin.readline().strip().split(" ")))
        if values[0] == 0:
            break
        
        # 수의 개수, 수
        k, nums = values[0], sorted(values[1:])
        answer = []
        
        dfs(0, [])
        for values in answer:
            for value in values:
                print(value, end=" ")
            print()
        print()
        
solution2()