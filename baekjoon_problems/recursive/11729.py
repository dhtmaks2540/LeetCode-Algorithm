"""
하노이의 탑 이동 횟수가 최소가 되도록 출력하라

https://study-all-night.tistory.com/6

하노이의 탑 알고리즘은 아래와 같은 과정을 수행한다.

1단계 : n-1개의 원판을 1번 막대에서 2번 막대로 옮긴다(가장 큰 마지막 막대를 냅두고 이동)
2단계 : 남은 1개의 원판을 1번 막대에서 3번 막대로 옮긴다
3단계 : 다시 n-1개의 원판을 2번 막대에서 3번 막대로 옮긴다
"""

# 원판의 개수
N = int(input())
result = []
    
def hanoi(from_loc, to_loc, n):
    # 원판이 한 개면 그냥 옮기기
    if n == 1:
        result.append((from_loc, to_loc))
        return
    
    # 빈 원반의 번호
    # from, to, empty는 각 1, 2, 3 중 하나이고 서로 다르므로 from+to+empty=1+2+3=6이고, from과 to를
    # 우변으로 이항하면 empty = 6 - from - to 를 얻는다.
    empty = 6 - from_loc - to_loc 
    
    hanoi(from_loc, empty, n - 1) # 1 단계
    result.append((from_loc, to_loc)) # 2 단계
    hanoi(empty, to_loc, n - 1) # 3 단계
    
hanoi(1, 3, N)
print(2**(N) - 1)
for x in result:
    print(x[0], x[1])