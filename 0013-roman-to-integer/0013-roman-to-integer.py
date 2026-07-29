class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000
        }
        total = 0
        for x in range(len(s)):
            if x< len(s)-1 and roman[s[x]]<roman[s[x+1]]:
                total -= roman[s[x]]
            else:
                total += roman[s[x]] 
        return total
