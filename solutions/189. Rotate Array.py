from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> list[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums

if __name__ == '__main__':
    solution = Solution()
    # print(solution.rotate([1, 2, 3, 4, 5, 6, 7], 1))
    # print(solution.rotate([1, 2, 3, 4, 5, 6, 7], 2))
    print(solution.rotate([1, 2, 3, 4, 5, 6, 7], 3))
    # print(solution.rotate([1, 2, 3, 4, 5, 6, 7], 4))
    # print(solution.rotate([1, 2, 3, 4, 5, 6, 7], 5))
    # print(solution.rotate([1, 2, 3, 4, 5, 6, 7], 6))
    # print(solution.rotate([1, 2, 3, 4, 5, 6, 7], 7))
    # print(solution.rotate([1, 2, 3, 4, 5, 6, 7], 8))
