# Website: Leetcode
# Problem: 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/


class Solution:
    def fib(self, n: int) -> int:
        '''
        :type N: int, the index of Fibonacci number
        :rtype: int, the Nth Fibonacci number

        F(0) = 0, F(1) = 1
        F(n) = F(n - 1) + F(n - 2), for n > 1

        e.g. F(0) => 0
        e.g. F(1) => 1
        e.g. F(2) => 1 + 0 = 1
        e.g. F(3) => F(3-1) + F(3-2) = 1 + 1 = 2

        0 <= n <= 30

        Time = O(n)
        Space = O(1)
        '''
        if n < 2:
            return n

        prev1 = 1
        prev2 = 0

        for _ in range(2, n + 1):
            prev1, prev2 = prev1 + prev2, prev1

        return prev1
