from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        checked = []
        for n in range(length):
            if numbers[n] not in checked:
                checked.append(numbers[n])
                x1 = target - numbers[n]
                for m in range(length - 1, n, -1):
                    if numbers[m] == x1:
                        return [n + 1, m + 1]
