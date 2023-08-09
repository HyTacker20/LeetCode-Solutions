from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, i, n = len(nums), 0, 0
        while n < l:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                n += 1
            else:
                i, n = i + 1, n + 1
