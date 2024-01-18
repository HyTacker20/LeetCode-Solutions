class Solution:
    cache = [1, 1]

    def climbStairs(self, n):
        if n < len(Solution.cache):
            return Solution.cache[n]
        else:
            Solution.cache.append(self.fibonacci(n - 1) + self.fibonacci(n - 2))
            return Solution.cache[n]


