"""
S의 start 인덱스의 문자부터 end 인덱스의 문자까지 주어진 문자가 몇 번 나오는지 출력하라.

현재 문제를 문자와 구간이 주어질 때마다 구하게 되면 문자열의 길이의 최대는 200,000이고 질문의 수의
최대는 200,000이므로 주어진 시간안에 절대 풀이할 수 없다. 그 이유는 질문이 주어질 때마다 최대 문자열
의 길이를 확인하게 되면 시간 복잡도가 O(200,000 * 200,000)이기 때문이다. 따라서 문자열은 한번만
주어지기에 미리 구간합을 계산하고 구간이 주어지면 계산된 구간합을 사용해 정답을 출력해야 한다.
우선 a 부터 z 까지 저장하기 위한 리스트를 하나 선언해준다. 그 후 주어진 문자열을 순회하며
알파벳은 소문자만 나온다고 하였으므로, 현재 문자의 인덱스를 현재 문자 - a를 계산한 값으로 지정한다.
그렇게 되면 a는 0에 z는 26에 저장된다. 그리고 이 리스트를 구간합에 copy하여 계속해서 누적해준다.
그리고 구간합 start와 end가 나오면 이전에 숫자로 주어진 구간합을 계산하듯이 prefix[end] - prefix[start]
를 해주는데 이전의 문제들과는 달리 인덱스를 0번부터 가지게 되므로 start를 1빼지않고 end를 1더해서 
풀이하면 문자가 계속해서 누적되어 있으므로 문자가 총 몇 번 나오는지 출력할 수 있다.

현재 문제는 1차원 배열을 선언한 후 copy를 통해 계속해서 누적했지만, 2차원 배열을 선언하여 문제를
풀이할 수도 있다.(https://m.blog.naver.com/hongjg3229/221667140860)

"""

import sys

# 문자열
S = sys.stdin.readline().strip()
# 문자를 기록하기 위한 리스트
values = [0] * 26
# 구간합
prefixSum = [values.copy()]

# 구간합 누적
for i in range(len(S)):
    values[ord(S[i]) - ord('a')] += 1
    prefixSum.append(values.copy())
    
# 질문의 수
q = int(sys.stdin.readline().strip())

for _ in range(q):
    ch, start, end = sys.stdin.readline().strip().split(" ")
    # 문자의 개수 출력
    print(prefixSum[int(end) + 1][ord(ch) - ord('a')] - prefixSum[int(start)][ord(ch) - ord('a')])