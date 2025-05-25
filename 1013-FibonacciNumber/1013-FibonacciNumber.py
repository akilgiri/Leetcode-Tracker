# Last updated: 5/25/2025, 1:08:14 PM
class Solution:
    # def fib(self, n: int) -> int:
    #     if n == 0 or n == 1:
    #         return n
    #     else:
    #         return self.fib(n-1) + self.fib(n-2)
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a+b

        return b
        

        