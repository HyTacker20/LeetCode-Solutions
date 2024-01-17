class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        m = 1

        for n in range(1, len(nums)):
            if nums[n] != nums[n - 1]:
                nums[m] = nums[n]
                m += 1
        return m
