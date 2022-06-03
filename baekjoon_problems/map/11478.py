"""
문자열이 주어지면 서로 다른 연속된 부분 문자열의 개수를 출력하라.

서로 다른 연속된 부분 문자열은 문자열을 두 번 순회하면서 나타낼 수 있고, 그 값들의 기록은
set을 이용하여 기록한다. set은 해시함수를 사용해서 주어진 값을 해시 함수를 통해 변경한 후
현재 set에 없다면 기록하는 구조로, 중복되는 값을 가지지 않는 자료구조이다. 이를 통해
서로 다른 문자열의 개수를 출력하면 풀이할 수 있다.

시간복잡도는 주어진 문자열을 두 번 순회하는 것이므로 O(N^2)이고 N의 최대 길이가 
1,000이므로 최대 1,000,000개의 연산이 수행된다. 시간복잡도가 1초이므로 충분히 풀이할 수 있다.
"""

array = input()
# Set을 이용해 중복되는 값 제거
answer = set()

# 첫 번째 원소부터 
for i in range(len(array)):
    # i + 1 번째 원소부터
    for j in range(i + 1, len(array) + 1):
        answer.add(array[i:j])
        
print(len(answer))