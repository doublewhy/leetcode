class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        Input: List[int], an array of unique integers
        Output: List[List[int]], an array of all possible subsets (powerset)
        Assumptions:
            - Subsets should be unique
            - Subsets can be in any order

        e.g. nums = [0]
        [[], [0]]

        e.g.: nums = [1, 2]
        [[], [1], [2], [1, 2]]

        e.g.: nums = [1, 2, 3]
        [[], [1], [2], [2, 1], [3], [3, 1], [3, 2], [3, 2, 1]]

        Time = O(n * 2^n)
        Space = O(n * 2^n)
        '''
        subsets = [[]]

        for num in nums:
            subsets += [subset + [num] for subset in subsets]

        return subsets
