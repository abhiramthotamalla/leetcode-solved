class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_arr = nums1 + nums2
        return median(merged_arr)