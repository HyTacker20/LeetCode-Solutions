class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        A = m - 1
        B = n - 1
        C = m + n - 1

        for _ in range(C):
            if B == -1 or A == -1:
                break
            if nums2[B] > nums1[A]:
                nums1.pop(C)
                nums1.insert(C, nums2[B])
                nums2.remove(nums2[B])
                C -= 1
                B -= 1
            else:
                nums1[C], nums1[A] = nums1[A], nums1[C]
                A -= 1
                C -= 1

        for i in range(len(nums2)):
            nums1[i] = nums2[i]
