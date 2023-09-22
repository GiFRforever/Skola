from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0

        for n in nums2:
            if n < nums1[0]:
                nums1.insert(0, n)
            elif n > nums1[-1]:
                nums1.append(n)
            else:
                for i in range(len(nums1)):
                    if nums1[i] >= n:
                        nums1.insert(i, n)
        del nums2
        if len(nums1) % 2 == 0:
            return (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2
        else:
            return nums1[len(nums1) // 2]


print(Solution().findMedianSortedArrays([1, 3], [2]))
print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
