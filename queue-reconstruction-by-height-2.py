from typing import List
import heapq

"""
처음 접근

규칙을 파악하지 않고 단지 정렬을 수행한 후 현재 원소를 결과 변수의 첫 번째 원소부터 비교해 나가며
조건이 만족할 때 해당 인덱스에 넣으려고 했음 -> 코드로 작성도 못함..

문제의 핵심

k는 자신의 키보다 큰 사람들의 수를 나타내므로 이를 이용하여 규칙을 찾는게 중요한 포인트라고 생각
큰 키부터 차례대로 접근하면서 결과의 k 인덱스에 값을 넣으면 원하는 결과를 도출할 수 있었음
뒤는 생각하지 않고 자신에게 필요한 조건(정렬 후 큰 키부터 추출)을 사용하여 탐욕적으로 접근해야함
따라서 우선순위 큐를 이용해 큰 키부터 값을 가져올 수도 있고 정렬을 수행해 큰 키부터 값을 가져올 수도 있음
"""

# people을 규칙에 맞게 재정렬하라.
class Solution:
    # 규칙을 찾아 우선순위큐를 활용하여 문제 풀이
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        # 키 역순, 인덱스 삽입
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        result = []
        # 키 역순, 인덱스 추출
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1] , [-person[0], person[1]])

        return result

    """
    https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89345/Easy-concept-with-PythonC%2B%2BJava-Solution
    
    1. people에서 가장 키가 큰 그룹을 찾고 정렬하여 subarray로 만든다. 왜냐하면, 그들보다 키가 큰 그룹이 없기에
    각 사람들의 인덱스는 그의 k value와 같은 인덱스가 될 것이다.

    2. 두 번째로 키큰 그룹(그리고 나머지)도 계속해서 subarray로 넣는다.

    Example)
    input : [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    subarray after step 1 : [[7,0], [7,1]]
    subarray after step 2 : [[7,0], [6,1], [7,1]]
    """

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 예외처리
        if not people: return []

        # obtain everyone's info
        # key = height, value = k - value, index in original array
        peopledict, height, res = {}, [], []

        for i in range(len(people)):
            p = people[i]
            # 현재 키가 있다면(같은 키 그룹이 있다는 의미)
            if p[0] in peopledict:
                peopledict[p[0]] += (p[1], i),
            else:
                peopledict[p[0]] = [(p[1], i)]
                height += p[0],

        # 큰 키부터 정렬
        height.sort(reverse=True) # here are different heights we have

        # sort from the tallest group
        for h in height:
            peopledict[h].sort()
            for p in peopledict[h]:
                # k 인덱스에 person 정보 넣기
                res.insert(p[0], people[p[1]])

        return res

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        # height는 내림차순, k는 오름차순으로 정렬
        for p in sorted(people, key=lambda x: (-x[0], x[1])):
            res.insert(p[1], p)

        return res

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
solution = Solution()
print(solution.reconstructQueue(people))