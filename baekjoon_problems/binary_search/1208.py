"""
https://hyeo-noo.tistory.com/128

문제를 DFS를 사용해서 풀이하려고 했는데, 시간복잡도 안에 문제를 풀이할 수 없었다. 따라서
힌트를 보던 도중 DP로 풀이할 수 있을듯해 규칙을 찾으며 점화식을 도출하려고 했는데,
점화식 또한 도출하지 못했다.. ㅠㅠ 도저히 답을 찾을 수 없어서 해답을 찾던 도중 이분 탐색을
사용해서 풀이하는 것을 찾았다.

우선 수열의 길이가 40이라고 가정하고 20번째 수열부터 40번째 수열(이를 right 수열이라고 가정)
까지의 모든 부분수열의 합을 구한다. 이 시간복잡도는 O(2^20)에 해당한다.
그리고 right 부분 수열의 합을 sum 이라고 한다면 right 수열을 탐색하면서 sum 값이 몇 번 나왔는지
map 자료구조를 사용해 저장한다.

right 부분수열을 통해서 딕셔너리를 채웠다면 0번 수열부터 19번째 수열까지(left 수열이라고 가정)의
모든 부분수열의 합을 구한다. 수열을 탐색할 때마다 cnt 값을 map[S-sum] 만큼 더한다.
left 수열의 부분수열의 합이 sum인 경우에 map[S-sum]이 존재한다면 해당 map값(right 수열에서 구한 값)
과 현재 left 수열의 sum을 더하면 S가 된다는 것이다(두 수의 합을 구하는 방식).

다만 S가 0인 경우에는 left, right 부분수열 모두 공집합인 경우가 하나 존재하기 때문에 구한 cnt 값에서
1을 빼준게 정답이 된다.

"""

import sys
import collections

# 정수의 개수, 목표값
N, S = map(int, sys.stdin.readline().strip().split(" "))
array = list(map(int, sys.stdin.readline().strip().split(" ")))
sub_sum = collections.defaultdict(int)
cnt = 0

# 수열의 길이 // 2(mid) 인덱스부터 
# 모든 부분 수열을 계산하여 맵(딕셔너리)에 기록
def rightSeq(mid, sum):
    # 마지막 인덱스에 도달했다면
    if mid == N:
        # 현재까지 부분수열의 합을 키로 딕셔너리에 저장
        sub_sum[sum] += 1
        return
    
    rightSeq(mid + 1, sum + array[mid])
    rightSeq(mid + 1, sum)

# 0번 인덱스부터 수열의 길이 // 2 인덱스 전까지의
# 모든 부분 수열을 계산하여 수열을 모두 탐색할 때마다 cnt의 값을
# map[S - sum] 만큼 더해준다.

# left 수열의 부분수열의 합이 sum인 경우에 map[S - sum]이 존재한다면
# 해당 map(right 수열에서 구한 값)과 현재 left 수열의 sum을 더하면
# S가 된다.
def leftSeq(st, sum):
    global cnt
    
    if st == N // 2:
        cnt += sub_sum[S - sum]
        return
    
    leftSeq(st + 1, sum + array[st])
    leftSeq(st + 1, sum)
    
rightSeq(N // 2, 0)
leftSeq(0, 0)

print(cnt - 1) if not S else print(cnt)
    
