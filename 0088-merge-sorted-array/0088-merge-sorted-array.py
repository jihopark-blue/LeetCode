class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # 0 먼저 제거
        for _ in range(n):
            nums1.pop()

        nums1.extend(nums2)
        nums1.sort()