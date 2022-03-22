"""
https://jokerldg.github.io/algorithm/2021/03/21/multitap.html

플러그를 빼는 최소의 횟수를 구하라가 문제의 핵심이며 그리디 알고리즘 유형이 된다.

그리디하게 접근하는 문제

멀티탭에 플러그를 꽃을 때 경우의 수는 세 가지가 존재
1. 멀티탭에 해당 기기가 꽃혀있는 경우
2. 멀리탭에 빈 곳이 남았을 경우
3. 플러그에 빈 곳이 없는 경우

1,2번의 경우 콘센트를 뺄 필요가 없으므로 continue

3번의 경우 콘센트를 빼야하는데 어떤 콘센트를 뺴야하는지를 그리디하게 접근해야 한다.
    * 멀티탭의 현재 위치부터 마지막까지 가져온 후 멀티탭 안에 플러그에 있는 값이 있다면 멀티탭의
    인덱스 값을 가져오고, 없다면 구멍의 최대 개수 + 1을 하여 101을 넣어준다.
    * 가져온 인덱스를 가지고 비어있는 위치의 인덱스를 가져와서 플러그를 뽑아준 뒤 다음 전기용품을 넣어준다.

    * 그리디하게 접근하면 이후에 단 한번도 쓰지 않을 기기를 빼거나 제일 마지막에 쓰일 기기를 빼는 것이 최적
    * 위에서 찾은 기기를 플러그에서 빼고 사용 예정인 기기를 꽃는다.

그리디 알고리즘을 생각했으면 그리디 하게 문제를 풀 수 있는 조건을 잘 파악하자.
이 문제의 경우 플러그가 빈 곳어 없는 경우 그리디 하게 접근해야 하는 포인트인데
해당 문제에서 최적의 조건은 앞으로 사용하지 않을 기기나 가장 멀리 있는 기기를 뽑는게 가장 적게 뽑는
방법에 해당한다. 따라서 이를 코드로 구현하면 된다. !!!! 그리디로 접근하는 포인트와 가장 좋은 것을
선택하는 방법을 코드로 구현하는 것을 생각하자 !!!!
"""

import sys

sys.stdin = open("input.txt", "rt")

# 멀티탭 구멍의 개수, 전기 용품의 총 사용 횟수
N, K = map(int, input().split())
# 사용할 전기용품 목록
multitap = list(map(int, input().split()))
# 정답 변수
answer = 0
# 플러그
plug = []

for i in range(K):
    # 이미 꽃혀있는 경우
    if multitap[i] in plug:
        continue
    # 플러그에 빈 곳이 있는 경우
    if len(plug) < N:
        plug.append(multitap[i])
        continue
    
    multitap_idxs = [] # 다음 멀티탭의 값을 저장
    hasplug = True

    # 현재 플러그에 꽃혀있는 기기 탐색
    for j in range(N):
        # 멀티탭 안에 플러그 값이 있다면
        if plug[j] in multitap[i:]:
            # 멀티탭 인덱스 위치 값 가져오기
            multitap_idx = multitap[i:].index(plug[j])
        else:
            multitap_idx = 101
            hasplug = False

        # 인덱스에 값을 넣어준다.
        multitap_idxs.append(multitap_idx)

        # 없다면 종료
        if not hasplug:
            break

    # 플러그를 뽑는다(더 멀리 있는 플러그를 뽑아낸다)
    plug_out = multitap_idxs.index(max(multitap_idxs))
    del plug[plug_out] # 플러그에서 제거
    plug.append(multitap[i]) # 플러그에 멀티탭 값 삽입
    answer += 1 # 뽑았으므로 1 증가

print(answer)