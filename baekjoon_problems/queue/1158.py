"""
요세푸스 순열을 구하라

https://infinitt.tistory.com/213

인덱스와 count를 하나씩 증가시키며 비교할 생각만하여 계산의 효율성이 나오지 않았다.. 하지만
아래와 같이 한 번에 K - 1 만큼 증가시키며 인덱스를 증가시키면 계산의 복잡도가 확 줄기에 
훨씬 시간복잡도가 줄어들게 된다. 따라서 인덱스를 증가시킬때 하나하나 비교하는 것이 아니라 
될 수 있으면 계산은 줄이는것이 중요한 포인트이다.
"""

def solution():
    # N명의 사람, K번째
    N, K = map(int, input().split(" "))
    answer = []
    index = 0 # 제거될 인덱스 번호
    # 사람
    array = [i for i in range(1, N + 1)]
    
    for _ in range(N):
        index += K - 1
        if index >= len(array):
            index = index % len(array)
            
        answer.append(str(array.pop(index)))
    
    print("<", end="")
    for index, x in enumerate(answer):
        if index != len(answer) - 1:
            print(x, end=", ")
        else:
            print(x, end="")
    print(">", end="")
    
solution()