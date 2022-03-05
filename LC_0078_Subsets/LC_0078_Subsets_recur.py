class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        type nums: List[int]
            - ints are unique
            - maybe sorted, maybe not
        rtype: List[List[int]],  all possible subsets (the power set)
            - must not contain duplicate subsets (order doesn't matter)
            - the solution in any order

        e.g. nums = []
        >>> [[]]

        e.g. nums = [1]
        >>> [[], [1]]

        e.g. nums = [1, 2]
        [[], [1], [2], [1, 2]]

        e.g. nums = [1, 2, 3]
        [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

        base case: len(nums) == 0 => [[]]
        recursive: subsets(nums[:-1]) + nums[-1]

        Time = O(n * 2^n)
        Space = O(n * 2^n)
        '''
        if len(nums) == 0:
            return [[]]
        else:
            powerset = self.subsets(nums[:-1])
            for i in range(len(powerset)):
                powerset.append(powerset[i] + [nums[-1]])
            return powerset
