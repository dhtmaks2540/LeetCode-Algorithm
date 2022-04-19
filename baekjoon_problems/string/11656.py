"""
문자열 S가 주어졌을 때, 모든 접미사를 사전순으로 정렬한 다음 출력하라
접미사는 뒤에서부터 차례대로 접근하는 문자를 말한다.

문자열을 뒤에서부터 interation 하면서 문자열의 슬라이싱 기능을 사용해 접미사들을 뽑아낸다.
그 후 정렬을 사용해 오름차순으로 정렬하고, 이를 출력하면 된다.
"""

s = input()
# 접미사를 저장할 리스트
array = []
# 문자의 길이
n = len(s)

for index in range(n - 1, -1, -1):
    array.append(s[index:n])
    
# 정렬 수행
array.sort()

for x in array:
    print(x)