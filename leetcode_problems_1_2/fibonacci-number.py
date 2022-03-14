import collections

class Solution:
    dp = collections.defaultdict(int)
    
    # 메모이제이션 - 하향식
    def fib(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 0

        def recursive_fibo(n):
            if n == 1 or n == 2:
                return 1
            
            if dp[n] != 0:
                return dp[n]

            dp[n] = recursive_fibo(n - 1) + recursive_fibo(n - 2)
            
            return dp[n]

        if n == 0:
            return 0
        else:
            return recursive_fibo(n)

    # 메모이제이션(defaultdict) - 하향식
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dp[n] 

    # 타뷸레이션 - 상향식
    def fib(self, n: int) -> int:
        self.dp[0] = 0
        self.dp[1] = 1

        for i in range(2, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]

        return self.dp[n]  

    # 두 변수만을 이용해 공간 절약
    def fib(self, n: int) -> int:
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x + y
        
        return x
    

solution = Solution()
print(solution.fib(3))