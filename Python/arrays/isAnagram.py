class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        dS, dT = {}, {}

        for i in range(len(s)):
            dS[s[i]] = 1 + dS.get(s[i], 0)
            dT[t[i]] = 1 + dT.get(t[i], 0)
        return dS == dT

 # Second solution
 class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        return ''.join(sorted(s)) == ''.join(sorted(t))
 
