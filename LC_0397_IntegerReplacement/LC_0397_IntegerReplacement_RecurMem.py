class Solution:
    def integerReplacement(self, n: int) -> int:
        '''
        :type n: int, 1 <= n <= 2^31 - 1
        :rtype: int, the minimum number of operations needed for n to become 1

        If n is even, replace n with n / 2.
        If n is odd, replace n with either n + 1 or n - 1.

        e.g. f(8) => 3
        8 => 4 => 2 => 1

        e.g. f(7) =>
        7 -> 8 -> 4 -> 2 -> 1 => 4
         \
          6 -> 3 -> 4 -> 2 -> 1 => 5
                \
                 2 -> 1 => 4

        base case: n = 1 => 1
        recursive cases: n % 2 == 0 => f(n / 2)
                         n % 2 == 1 => min(f(n + 1), f(n - 1))

        Time O(log n), Space O(log n)
        '''

        global cache

        # Base case
        if n in cache:
            return cache[n]

        # Recursive cases
        if n % 2 == 0:
            cache[n] = 1 + self.integerReplacement(n / 2)
        else:
            cache[n] = (1 + min(self.integerReplacement(n + 1),
                        self.integerReplacement(n - 1)))
        return cache[n]

cache = {1: 0}
