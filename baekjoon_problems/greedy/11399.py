"""
돈을 인출하는데 필요한 시간의 합의 최솟값을 출력하라

사람의 수가 N이므로 완전 탐색을 수행하는 경우 N^2의 연산을 N번 수행해야하므로 O(N^3)에 해당한다.
따라서 절대 완전 탐색으로는 풀이할 수 없다. 따라서 그리디하게 접근하여 어떤 조건을 활용하면
한번의 탐색으로 시간의 합이 최소가 되도록 풀이하였다. 예제에서 돈을 인출하는데 걸리는 시간이
적은 사람 먼저 돈을 인출하도록 했더니 시간의 합이 최소가 되었다. 즉, SJF를 사용하면 시간의 합을
최소로 만드는 알고리즘이 되는 것이다.

따라서 오름차순으로 정렬을 수행한 후 시간을 누적해나가며 정답 변수에 더해서 풀이했다.
시간복잡도는 정렬을 수행하는데 O(NlogN), 탐색하는데 O(N)이므로 O(NlogN + N) = O(N(logN + 1))이 된다.
"""

import sys

# 사람의 수
N = int(sys.stdin.readline().strip())
# 돈을 인출하는데 걸리는 시간
times = list(map(int, sys.stdin.readline().strip().split(" ")))

# 오름차순 정렬 수행
times.sort()

sum_time = 0
answer = 0

for time in times:
    sum_time += time
    answer += sum_time
    
print(answer)