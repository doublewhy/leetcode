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

        Brute force approach:
            enumerate each possible subarray (start):
                add next element to the sum
                if sum of subarray >= target:
                    take the min of current min length so far and the length of current subarray

            Time: O(n^2)
            Space: O(n)

        Sliding window approach:
            initialize variables:
                left that points to the start of the window
                current sum = 0
                min length so far to len of array + 1
            traverse the array (it is a right pointer that points to the end of the window):
                add element at the end pointer to current sum
                while current sum is greater than or equal to target:
                    take the min of min length so far and current length of the window
                    shrink the window

            Time complexity: O(n)
            Space complexity: O(1)

          [2,3,1,2,4,3]
        lp   ^
        rp       ^
        cs 2 5 6 6 6 3
        ml 7 7 7 4 3 2
        '''

        min_length = len(nums) + 1
        curr_sum = start = 0

        # expand the window to the right
        for end in range(len(nums)):
            curr_sum += nums[end]

            while curr_sum >= target:

                # update the min length seen so far
                min_length = min(min_length, end - start + 1)

                # shrink the window by removing the leftmost element
                curr_sum -= nums[start]
                start += 1

        # return 0 if no subarray exist that satisfies our condition
        if min_length > len(nums):
            return 0
        return min_length


