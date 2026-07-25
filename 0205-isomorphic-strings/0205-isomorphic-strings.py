class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        stot = {}
        ttos  = {}
        for c1 ,c2 in zip(s,t):
            if c1 in stot:
                if stot[c1] != c2:
                    return False
            else:
                stot[c1] = c2
            if c2 in ttos:
                if ttos[c2] != c1:
                    return False
            else:
                ttos[c2] = c1
        return True