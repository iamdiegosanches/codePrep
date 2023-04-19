class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def backtrack(n):
            if n <= 1:
                return 1
            else:
                return backtrack(n-1) + backtrack(n-2)

        return backtrack(n)
