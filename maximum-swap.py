# 최대 한번 변경하여 최댓값 반환
class Solution:
    """
    https://leetcode.com/problems/maximum-swap/discuss/185982/Straightforward-O(n)-python
    
    뒤에서부터 max 값을 찾는다. 만약 현재의 값이 max 값보다 작으면, 후보가 될 수 있다. 만약 현재의 값이
    max 값보다 크다면, max 값을 갱신한다. 만약 현재의 값이 max 값과 동일하다면, 아무 것도 하지 않는다.
    왜냐하면 마지막으로 나타난 max의 값으로 변경해야 최대값이 되기 떄문이다. 만약 다른 숫자가 max 값보다
    작다면 우리는 후보를 업데이트 하는데, 앞에서 부터 변경하는 것이 더 큰 값을 주기 때문이다.
    """

    def maximumSwap(self, num: int) -> int:
        num = [int(x) for x in str(num)]
        max_idx = len(num) - 1
        xi = yi = 0
        # 뒤에서부터 이터레이션
        for i in range(len(num) - 1, -1, -1):
            # 만약 현재의 값이 max 값보다 크다면 인덱스 갱신
            if num[i] > num[max_idx]:
                max_idx = i
            # 현재의 값이 max 값보다 작다면
            elif num[i] < num[max_idx]:
                # 최소 인덱스 갱신
                xi = i
                # 맥스 인덱스 저장
                yi = max_idx
        # 자리 변경
        num[xi], num[yi] = num[yi], num[xi]
        return int("".join([str(x) for x in num]))

num = 22341345
solution = Solution()
print(solution.maximumSwap(num))