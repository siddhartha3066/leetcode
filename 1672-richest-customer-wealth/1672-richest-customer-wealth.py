class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wel = 0
        for cus in accounts:
            cur_wel = 0
            for bak in cus:
                cur_wel +=bak
            if cur_wel > wel:
                wel = cur_wel
        return wel
