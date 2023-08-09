from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for n in range(0, len(nums)):
            nums[n] = nums[n] ** 2
        nums.sort()
        return nums
