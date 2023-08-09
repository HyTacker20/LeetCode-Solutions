# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n

        while True:
            mid = start + (end - start) // 2

            if isBadVersion(mid):
                end = mid - 1
                if not isBadVersion(mid - 1) and isBadVersion(mid + 1):
                    return mid
            else:
                start = mid + 1
