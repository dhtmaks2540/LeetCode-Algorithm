"""
시간 제한이 0.15이고 수의 범위가 10억이므로 직접 for문을 돌리며 비교하면 문제를 절대 풀이할 수 없다.
따라서 상수시간 O(1)내로 문제를 풀이해야한다. 따라서 문제를 푸는 수식을 생각하고 이를 사용해 풀이했다.

일단 달팽기가 정상에 도달하면 더 이상 떨어지지 않는다고 하므로 우리가 올라가야 하는 높이는 
(V - B)이다. 이 높이를 하루동안 올라가는 높이로 나누어서 딱 떨어지는 경우에는 낮에 모두 오르고
밤에 떨어져도 상관이 없는 값이다. 하지만 나누어 떨어지지 않는 경우에는 그 다음날 아침에도 한번 올라야
하는 값이므로 이를 올림을 사용해서 올려주도록 풀이한다. 즉, 만약 값이 4.0이 나오면 4일로 처리하고,
4.2가 나온다면 올림을 통해 5일로 처리해주는 방식이다.

https://st-lab.tistory.com/75

1번째날 이동거리 : A - B
2번째날 이동거리 : A - B
...
마지막날 이동거리 : A보다 작거나 같은 숫자

이동횟수를 count라고 한다면 (A - B)(count - 1) + A >= V 라는 수식이 유도된다.
전개한 후 count로 정리하면 count >= (V - B) / (A - B)가 나오게 되고
나누어 떨어진다면 (V - B) / (A - B)가 답이고, 나누어 떨어지지 않는다면 올림 처리를 해서 풀이

"""

import math

# 낮에 올라가는 높이, 밤에 떨어지는 높이, 나무 높이
A, B, V = map(int, input().split(" "))
day = math.ceil((V - B) / (A - B))
print(day)