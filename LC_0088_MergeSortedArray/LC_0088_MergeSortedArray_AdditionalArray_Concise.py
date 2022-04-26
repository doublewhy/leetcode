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
        p1 = p2 = 0

        # Merge two arrays by:
        #   1) Comparing elements from nums3 and nums2
        #   2) Writing smallest element to nums1
        for i in range(m + n):
            # Check for pointers to stay in boundaries
            if p1 >= m or (p2 < n and nums3[p1] > nums2[p2]):
                nums1[i] = nums2[p2]
                p2 += 1
            else:
                nums1[i] = nums3[p1]
                p1 += 1
