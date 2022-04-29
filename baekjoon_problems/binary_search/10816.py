"""
각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지 출력하라

해당 문제는 10815번과 비슷하지만 같은 개수를 출력하는 문제이다.
계수 정렬은 똑같이 사용하면 되지만, 이분 탐색은 Upper Bound와 Lower Bound를 사용해서 풀이할 수
있다. Lower Bound와 Upper Bound에 대한 자세한 내용은 https://st-lab.tistory.com/267 참조!
"""

# 계수 정렬 사용
# 시간 복잡도는 O(n + m)
def solution1():
    import sys

    # 숫자 카드의 개수
    N = int(sys.stdin.readline().strip())
    # 숫자 카드 정수
    numbers = list(map(int, sys.stdin.readline().strip().split(" ")))
    
    # 확인할 숫자의 개수
    M = int(sys.stdin.readline().strip())
    # 확인할 숫자
    check_numbers = list(map(int, sys.stdin.readline().strip().split(" ")))
    
    counts = [0] * 20000001
    
    for number in numbers:
        counts[number] += 1
        
    for check_number in check_numbers:
        print(counts[check_number], end=" ")

solution1()

# 이분 탐색을 사용하여 문제 풀이(Lower Bound, Upper Bound)
# 시간 복잡도는 O(nlogn + mlogn)
def solution2():
    import sys

    # 숫자 카드의 개수
    N = int(sys.stdin.readline().strip())
    # 숫자 카드 정수
    numbers = list(map(int, sys.stdin.readline().strip().split(" ")))
    
    # 확인할 숫자의 개수
    M = int(sys.stdin.readline().strip())
    # 확인할 숫자
    check_numbers = list(map(int, sys.stdin.readline().strip().split(" ")))
    
    # 정렬
    numbers.sort()
    
    def lower_binary_search(start, end, target):
        while start <= end:
            mid = start + (end - start) // 2
            
            # 상한값 줄이기
            if numbers[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
                
        return start - 1
    
    def upper_binary_search(start, end, target):
        while start <= end:
            mid = start + (end - start) // 2
            
            if numbers[mid] > target:
                end = mid - 1
            # 하한값 늘리기
            else:
                start = mid + 1
                
        return start - 1
    
    start, end = 0, N - 1
    
    for check_number in check_numbers:
        result = upper_binary_search(start, end, check_number) \
            - lower_binary_search(start, end, check_number)
            
        print(result, end=" ")
        
solution2()
        
# 이분 탐색 라이브러리 사용
def solution3():
    import sys
    import bisect 

    # 숫자 카드의 개수
    N = int(sys.stdin.readline().strip())
    # 숫자 카드 정수
    numbers = list(map(int, sys.stdin.readline().strip().split(" ")))
    
    # 확인할 숫자의 개수
    M = int(sys.stdin.readline().strip())
    # 확인할 숫자
    check_numbers = list(map(int, sys.stdin.readline().strip().split(" ")))
    
    # 정렬
    numbers.sort()
    
    for check_number in check_numbers:
        left_index = bisect.bisect_left(numbers, check_number)
        right_index = bisect.bisect_right(numbers, check_number)
        
        print(right_index - left_index, end=" ")
    
solution3()