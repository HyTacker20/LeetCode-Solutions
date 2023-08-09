from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        for s1 in range(len(s) // 2):
            s[s1], s[-(s1 + 1)] = s[-(s1 + 1)], s[s1]
