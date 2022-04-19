"""
문자열이 주어졌을 때, ROT13 으로 암호화한 다음 출력하라

주어진 조건에 맞게 현재 문자에서 13칸을 미룬 문자로 변경하는 문제이다. 이를 위해 파이썬에서
제공하는 isalpha() 함수를 통해서 문자를 확인하고, 대문자인지 소문자인지 확인하며 각각 'Z'와 'z'
인덱스를 넘어서는지 확인하고, 넘어서면 이를 다시 'A', 'a'부터 시작하도록 해주면 된다. 이는 ord
함수를 통해서 각 문자를 유니코드 값으로 변경한 후, 다시 chr 함수를 통해 문자로 돌려주는 식으로
구현하면 된다.
"""

array = list(input())
# 문자 iteration
for index, x in enumerate(array):
    # 알파벳일 경우에만 암호화
    if x.isalpha():
        # 대문자일 경우
        if x.isupper():
            ord_index = ord(x) + 13
            if ord_index > ord('Z'):
                ord_index = ord_index - ord('Z') + ord('A') - 1

            array[index] = chr(ord_index)
        # 소문자일 경우
        else:
            ord_index = ord(x) + 13
            if ord_index > ord('z'):
                ord_index = ord_index - ord('z') + ord('a') - 1
                
            array[index] = chr(ord_index)
            
for x in array:
    print(x, end="")