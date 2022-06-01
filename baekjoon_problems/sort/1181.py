"""
단어가 들어오면 길이가 짧은 것부터 -> 길이가 같다면 사전 순으로 정렬하라

우선 단어순으로 정렬한 후, 문자열의 길이에 따라 다시 한번 정렬을 수행한다.
"""

import sys

# 단어의 개수
N = int(sys.stdin.readline().strip())
array = set()
for _ in range(N):
    array.add(sys.stdin.readline().strip())
    
# 사전순 정렬
list_array = sorted(list(array))
# 길이 순 정렬
list_array.sort(key=lambda word: (len(word)))

for value in list_array:
    print(value)