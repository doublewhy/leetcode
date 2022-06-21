# Source: Leetcode
# Problem: 209. Minimum Size Subarray Sum
# Difficulty: Medium
# https://leetcode.com/problems/minimum-size-subarray-sum/


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        :type nums: list[int]
                        1 <= nums.length <= 10^5
                        1 <= nums[i] <= 10^5
        :type target: int, 1 <= target <= 10^9
        :rtype int: the minimal length of a contiguous subarray, of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

        Example 1:
            Input: target = 7, nums = [2,3,1,2,4,3]
            Output: 2

        Example 2:
            Input: target = 4, nums = [1,4,4]
            Output: 1

        Example 3:
            Input: target = 11, nums = [1,1,1,1,1,1,1,1]
            Output: 0

        Brute force approach:
            enumerate each possible subarray (start):
                if sum(subarray) >= target:
                    take the min of current min length so far and the length of current subarray

            Time: O(n^3)
            Space: O(n)

        Brute force approach optimized:
            enumerate each possible subarray (start):
                add next element to the sum
                if sum of subarray >= target:
                    take the min of current min length so far and the length of current subarray

            Time: O(n^2)
            Space: O(n)
        '''

        min_length = len(nums) + 1

        for start in range(len(nums)):

            curr_sum = 0

            for end in range(start, len(nums)):
                curr_sum += nums[end]

                if curr_sum >= target:
                    min_length = min(min_length, end - start + 1)

        if min_length > len(nums):
            return 0
        return min_length

