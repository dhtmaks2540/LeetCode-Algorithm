import collections

"""

돌 stones의 개수를 모두 파악한 후, 보석 jewels의 각 요소가 있는지 확인하는 방식으로 풀이하고자함
리스트(배열 - 스택), 데크와 같은 자료구조는 인덱스를 사용하여 값에 접근
하지만 해시 테이블(해시 맵)은 키를 사용하여 값에 접근하는 구조이기에 
돌을 키로하고 값은 그 빈도 수로 하는 딕셔너리에 자료를 저장하고 jewels는 그 딕셔너리에 존재하는지 여부를
사용하여 개수를 파악함

"""

class Solution:
    # defaultdict 사용
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = collections.defaultdict(int)

        # 돌의 개수 파악
        for stone in stones:
            dict[stone] += 1

        result = 0

        # 보석의 개수 파악
        for jewel in jewels:
            # 존재하지 않는 키의 경우에도 KeyError가 아닌 0을 출력
            result += dict[jewel]

        return result

    # Counter 사용
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = collections.Counter(stones)

        result = 0

        for jewel in jewels:
            # 존재하지 않는 키의 경우에도 KeyError가 아닌 0을 출력
            result += count[jewel]

        return result

    # dict 사용
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = {}
        count = 0

        # 돌의 빈도 수 계산
        for stone in stones:
            if stone not in dict:
                dict[stone] = 1
            else:
                dict[stone] += 1

        # 보석의 빈도 수 합산
        for jewel in jewels:
            if jewel in dict:
                count += dict[jewel]

        return count

    # 파이썬 다운 방식
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stone in jewels for stone in stones)

        


jewels = "aA"
stones = "aAAbbbb"

solution = Solution()
print(solution.numJewelsInStones(jewels, stones))   