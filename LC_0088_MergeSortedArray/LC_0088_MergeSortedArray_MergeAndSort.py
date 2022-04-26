class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Constraints:
            - Do not return anything, modify nums1 in-place instead.

        Solution complexity:
            Time: O((n + m) log (n + m))
            Space: O(n)
        """

        # Replace all 0 at the end of nums1 with elements from nums2
        for i in range(n):
            nums1[i + m] = nums2[i]

        # Sort nums1
        nums1.sort()
