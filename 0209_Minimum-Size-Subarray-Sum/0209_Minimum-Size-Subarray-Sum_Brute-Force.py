# Source: Leetcode
# Problem: 209. Minimum Size Subarray Sum
# Difficulty: Medium
# https://leetcode.com/problems/minimum-size-subarray-sum/


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        :type target: int, 1 <= target <= 10^9
        :type nums: list[int]
                    1 <= nums.length <= 10^5
                    1 <= nums[i] <= 10^5
        :rtype: int, the minimal length of a contiguous subarray of which the sum is greater than or equal to target

        Example 1:
            Input: target = 7, nums = [2,3,1,2,4,3]
            Output: 2

        Example 2:
            Input: target = 4, nums = [1,4,4]
            Output: 1

        Example 3:
            Input: target = 11, nums = [1,1,1,1,1,1,1,1]
            Output: 0

        Example 4:
            Input: target = 3, nums = [3]
            Output: 1

        Example 5:
            Input: target = 15, nums = [1,2,3,4,5]
            Output: 5


        Brute Force:
            enumerate all possible contiguous subarrays, starting from the smallest length of 1 till n
                check every subarray if the sum of subarray is greater than or equal to target
                    return the length of the subarray

            Time O(n^3), Space O(n)
        '''
        # generate size of subarrays
        for size in range(1, len(nums) + 1):

            # enumerate all possible contiguous subarrays
            for start in range(len(nums) - size + 1):

                # generate a subarray
                subarray = nums[start:start + size]

                # check if the sum of subarray is greater than or equal to target
                if sum(subarray) >= target:
                    return len(subarray)

        # no such subarray exist
        return 0

