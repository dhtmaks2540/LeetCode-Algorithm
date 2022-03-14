from typing import List


class Solution:
    """
    접근방법
    
    먼저 무조건 아이템을 한 번씩은 iteration 해야한다고 생각함(현재의 금액을 판단하기 위해서)
    그래서 브루드 포스에서는 prices를 iterate하며 현재 price 이후의 아이템을 또 다시 iterate하는데
    현재의 price보다 더 작은 값이 있으면 할인 후 안쪽 반복문을 break하는 방법으로 접근
    시간 복잡도는 O(n^2)
    
    Stack을 이용한 방법은 이전에도 풀이했던 방법으로 위와 똑같이 아이템을 한 번씩 iteration하는데
    이 때, 현재의 아이템은 stack에 넣는다.
    그리고 만약 스택에 아이템이 있고 가장 마지막에 저장된 값이 현재의 값보다 크거나 같으면 discount할 수 있는 상황이므로
    스택에서 아이템을 pop하고 discount 하는 방식으로 풀이.
    시간 복잡도는 O(n)
    
    현재 문제는 배열 또는 스택과 관련된 문제라고 나와있는데, 리스트(배열)에 값들을 
    문제의 조건에 맞게 하도록 배열의 기능을 통해 풀이하거나 스택을 이용하였으므로 위와 관련된 문제라고 생각
    
    """
    # 브루드 포스로 문제 풀이(시간 복잡도 O(n^2))
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        
        # iterate prices
        for i in range(n):
            # 현재의 아이템 이후 인덱스부터
            for j in range(i + 1, n):
                # 금액이 작거나 같다면
                if prices[i] >= prices[j]:
                    prices[i] -= prices[j]
                    break
                
        return prices
    
    # 스택을 이용하여 문제 풀이
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        
        for index, price in enumerate(prices):
            # 스택에 마지막에 저장된 값이 현재의 값보다 크거나 같은 동안에
            while stack and stack[-1][1] >= price:
                # 저장된 값 pop
                now_index, now_price = stack.pop()
                # 현재의 값만큼 할인
                prices[now_index] -= price
                
            stack.append((index, price))
            
        return prices
    
prices = [8,4,6,2,3]
solution = Solution()
print(solution.finalPrices(prices))