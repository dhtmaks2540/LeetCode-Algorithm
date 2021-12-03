import collections

def numJewelsInStones(jewels, stones):
    # 딕셔너리
    dict = {}

    # jewels에 변수 딕셔너리로 저장
    for jewl in jewels:
        dict[jewl] = 0

    # stones 이터레이터 하며
    for stone in stones:
        # 키가 존재하면 값 증가
        if stone in dict:
            dict[stone] += 1

    return sum(list(dict.values()))

def numJewelsInStones(jewels, stones):
    freqs = {}
    count = 0

    # 돌(stone)의 빈도 수 계산
    for char in stones:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1

    # 보석(jewels)의 빈도 수 합산
    for char in jewels:
        if char in freqs:
            count += freqs[char]

    return count

# defaultdict 이용
def numJewelsInStones(jewels, stones):
    freqs = collections.defaultdict(int)
    count = 0

    # 비교 없이 돌(S)의 빈도 계산
    for char in stones:
        freqs[char] += 1

    # 비교 없이 보석(J)의 빈도 계산
    for char in jewels:
        count += freqs[char]

    return count

# Counter 활용
def numJewelsInStones(jewels, stones):
    freqs = collections.Counter(stones) # 돌 빈도 수 계산
    count = 0

    # 비교 없이 보석 빈도수 합산
    for char in jewels:
        count += freqs[char]

    return count

# 파이썬 다운 방식
def numJewelsInStones(jewels, stones):
    return sum(s in jewels for s in stones)

jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))