class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [[] for _ in range(numRows)]
        i = 0
        while i < len(s):
            j = 0
            while j < numRows and i < len(s):
                ans[j].append(s[i])
                j += 1
                i += 1
                    
            j = numRows - 2
            while j > 0 and i < len(s):
                ans[j].append(s[i])
                j -= 1
                i += 1

        result = ""
        for row in ans:
            result += "".join(row)

        return result
