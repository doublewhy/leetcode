class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Constraints:
            - Do not return anything, modify nums1 in-place instead.

        Solution complexity:
            Time: O(n + m)
            Space: O(n + m)
        """

        # Create an additional array
        nums3 = nums1[:m]

        # Initialize pointers for arrays
        i = p1 = p2 = 0

        # Merge two arrays by:
        #   1) Comparing elements from nums3 and nums2
        #   2) Writing smallest element to nums1
        while p1 < m and p2 < n:
            if nums3[p1] > nums2[p2]:
                nums1[i] = nums2[p2]
                p2 += 1

            else:
                nums1[i] = nums3[p1]
                p1 += 1
            i += 1

        # Add leftover elements from nums3
        while p1 < m:
            nums1[i] = nums3[p1]
            p1 += 1
            i += 1

        # Add leftover elements from nums2
        while p2 < n:
            nums1[i] = nums2[p2]
            p2 += 1
            i += 1
