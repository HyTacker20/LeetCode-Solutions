class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            x = target - nums[i]
            for j in range(len(nums)):
                if j == 0 or i == j:
                    continue
                if x == nums[j]:
                    return [i, j]


print(Solution.twoSum(None, nums=[2, 7, 11, 15], target=9))
print(Solution.twoSum(None, nums=[3, 2, 4], target=6))

print(list(range(1, 1)))
