class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cSet = set()
        ans = 0
        j = 0
        for i in range(len(s)):
            while s[i] in cSet:
                cSet.remove(s[j])
                j += 1
            cSet.add(s[i])
            ans = max(ans, len(cSet))

        return ans
