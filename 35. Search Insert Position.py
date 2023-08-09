from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while True:
            mid = start + (end - start) // 2

            if start > end:
                return mid + 1

            if nums[mid] == target:
                return mid

            if target < nums[mid]:
                end = mid - 1

            else:
                start = mid + 1
