class Solution:
    def tribonacci(self, n: int) -> int:

        @cache
        def backtracking(n: int):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            else:
                return  backtracking(n-3) + backtracking(n-2) + backtracking(n-1)
                
        return backtracking(n)
