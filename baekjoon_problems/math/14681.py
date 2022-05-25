"""
if, else를 사용해서 코드를 분기할 수 있는지
"""

x = int(input())
y = int(input())

if x > 0:
    if y > 0: print(1)
    else: print(4)
else:
    if y > 0: print(2)
    else: print(3)