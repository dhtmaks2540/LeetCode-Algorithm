"""
연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력하라

https://nnnlog.tistory.com/65

접두사 합으로 구간의 합을 O(수의 개수)의 시간복잡도로 우선 구한 후 직접 모든 구간을 탐색하며
M으로 나누어 떨어지는지 확인하면 O(N * (N / 2))의 시간 복잡도가 걸리는데 이는 O(N^2)으로 계산하면
수의 개수가 최대 1,000,000이므로 시간 제한 1초안에 절대 풀이할 수 없다. 따라서 다른 방법을
생각해야 한다.

해당 문제는 수식을 통해 풀이하는 문제이다. 구간합은 sum[j] - sum[i - 1] = 목표값이 되는 문제인데
현재 문제에서는 M으로 나누어 떨어지는 값을 찾으라 했으므로 (sum[j] - sum[i - 1]) % M = 0인 값을
찾아야 한다. 이를 풀어보면 sum[j] % M = sum[i - 1] % M 이라는 식이 된다. 이를 사용해서
나머지의 개수를 누적해 저장하고, 저장된 개수에서 임의의 두 개의 값을 뽑아 위 식을 만족하는
값을 더해주면 된다. 그런데 여기서 나머지가 0이라는 것은 위와 같은 수식이 필요 없이 혼자서
sum[i] % M = 0이라는 것을 만족하는 것이므로 이를 먼저 더해주고 식을 수행하면 된다.
"""

import sys

# 수의 개수, 나누어 떨어지는 수
N, M = map(int, sys.stdin.readline().strip().split(" "))
array = list(map(int, sys.stdin.readline().strip().split(" ")))
sum_value = 0
mod_cnt = [0] * (M)

for i in range(N):
    # 1부터 i 까지의 누적합에 M을 나눈 나머지
    sum_value = (sum_value + array[i]) % M
    print(sum_value)
    # 나머지 개수 누적
    mod_cnt[sum_value] += 1

# 나머지가 0인 값은 0~i번째의 값의 합이 M으로 나누어 떨어진다는 의미이므로 우선 더함
answer = mod_cnt[0]

for i in range(M):
    # 현재의 개수에서 2개를 뽑는 조합 공식 = nC2를 풀이하면 아래와 같은 수식을 만족
    answer += mod_cnt[i] * (mod_cnt[i] - 1) // 2
    
print(answer)