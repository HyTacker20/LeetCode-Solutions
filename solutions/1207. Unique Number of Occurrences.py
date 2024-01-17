class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        unique_occurrences = []
        for num in set(arr):
            num_occurrence = arr.count(num)
            if num_occurrence in unique_occurrences:
                return False

            unique_occurrences.append(num_occurrence)

        return True
