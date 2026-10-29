class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        se = {}
        te = {}

        for i in s:
            if i not in se:
                se[i] = 1
            else:
                se[i] = se[i] + 1

        for m in t:
            if m not in te:
                te[m] = 1
            else:
                te[m] = te[m] + 1 


        return se == te 
        

        