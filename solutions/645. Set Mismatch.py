class Solution:

    def findErrorNums(self, nums: list[int]) -> list[int]:
        nums.sort()
        right_list = []
        expected_sum = int((len(nums) * (len(nums) + 1) / 2))
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                right_list.append(nums[i])
                right_list.append(nums[i] + (expected_sum - sum(nums)))

        return right_list
