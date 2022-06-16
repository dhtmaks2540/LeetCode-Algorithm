"""
우선 주어진 가로와 세로의 범위는 1억 이하의 자연수로 완전 탐색 코드를 작성하기도 어렵겠지만
작성한다고 쳐도 O(가로 * 세로)의 시간 복잡도를 가지므로 절대 좋은 알고리즘 코드가 아니다. 따라서
뭔가 다른 방법으로 접근해야 하는데 그림을 보다보면 뭔가 반복되는 패턴이 보이게 된다. 그래서 이를 사용하려
했지만  어떤식으로 접근해야 할지를 몰라서 풀지 못했다...

https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A9%80%EC%A9%A1%ED%95%9C-%EC%82%AC%EA%B0%81%ED%98%95-in-python
https://taesan94.tistory.com/55

두 블로그 모두 주어진 패턴을 분석해 이를 코드로 나타내고 사용해서 정답을 도출한 것이다. 만약
이와 같이 큰 범위와 그림 등을 주면 패턴을 분석해 정답으로 도출하는 과정을 가져야겠다.

우선 예시로 주어진 W:8, H:12 라는 값은 그래프를 보면 알겠지만 (0, 0)부터 시작해서
(2, 3), (4, 6), (6, 9), (8, 12) 좌표를 지나간다. 즉, x = 2, y = 3씩 값이 증가되고 있는 것인데
주어진 숫자 8, 12에서 2와 3이 나오기 위해서는 각 수에 4라는 값을 나눈 것이며 이는 지나온 좌표의 개수에 해당한다.
그리고 8과 12에서 4라는 숫자는 최대 공약수 또는 최소 공배수로 접근할 수 있는데 4라는 값은 두 수의
최대 공약수에 해당하다. 이제 다른 예시를 통해 이 접근이 맞는지 무조건 검증을 해야 한다.

블로그를 보면 w : 7, h : 14를 예시로 들었는데 해당 그래프에서 좌표는 (1, 2), (2, 4), (3, 6),
(4, 8), (5, 10), (6, 12), (7, 14)를 통과하게 된다. 좌표의 개수는 7개가 나오고 (1,2)는 7과 14의
각 수에 7이라는 숫자를 나눈 것이다. 그리고 이 7은 위와 같이 7과 14의 최대 공약수이므로 위의
접근 방식이 맞다는 의미가 된다.

이를 통해 우리가 알 수 있는 점은 동일한 패턴을 가진 사각형이 생기며,
최대 공약수로 해당 패턴이 몇 번 반복되는지, 패턴의 좌표를 구할 수 있게 된다. 이를 사용해서
사용하지 못하는 블록의 개수를 파악해보면 된다.

다만 최대 공약수가 1인 경우는 다른 상황이 발생하는데 최대 공약수가 1이면은 위의 예시와 같이
좌표를 지나지 않는다. 이를 첫 번째 블로그의 예시에서 보면 알 수 있는데, w = 2, h = 3일때
잘라지는 사각형의 개수는 h로 생각하면 총 h만큼 잘라지고, w로 생각하면 총 w만큼 잘라진다. 다만
두 개 모두 첫 번째 칸이 겹치기에 w + h - 1 만큼 잘라진다고 생각하면 된다. 

그리고 최대 공약수가 1보다 크면 위의 블록이 최대 공약수만큼 반복되게 되며, 잘라지는 사각형의 수도
위와 같게 된다. 따라서 식은 g(최대 공약수) * ((w // g) + (h // g) - 1)이 되고 이를 분배하면
최종적으로 w + h - g라는 식이 사용하지 못하는 사각형의 개수가 된다.

이제 최종적으로 사용할 수 있는 사각형의 개수는 w * h - (w + h - g)가 된다.
"""

from math import gcd

def solution(w,h):
    return w * h - (w + h - gcd(w, h))

w = 8
h = 12
print(solution(w, h))