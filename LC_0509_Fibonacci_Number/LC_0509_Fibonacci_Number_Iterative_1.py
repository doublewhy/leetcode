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

        Time O(n)
        Space O(n)
        '''
        fib_nums = {0: 0, 1: 1}

        for i in range(2, n + 1):
            fib_nums[i] = fib_nums[i-1] + fib_nums[i-2]

        return fib_nums[n]
