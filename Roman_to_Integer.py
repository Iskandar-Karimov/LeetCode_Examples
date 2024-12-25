class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {"I":1, "V":5, "X":10, "L": 50, "C":100, "D":500, "M":1000}
        total_num = 0
        for i in range(len(s)):
            if i !=0:
                if symbols[s[i]] == symbols["V"] or symbols[s[i]] == symbols["X"]:
                    if symbols[s[i-1]] == symbols["I"]:
                        total_num -= 2
                if symbols[s[i]] == symbols["L"] or symbols[s[i]] == symbols["C"]:
                    if symbols[s[i-1]] == symbols["X"]:
                        total_num -= 20
                if symbols[s[i]] == symbols["D"] or symbols[s[i]] == symbols["M"]:
                    if symbols[s[i-1]] == symbols["C"]:
                        total_num -= 200
            total_num += symbols[s[i]]
        return total_num
